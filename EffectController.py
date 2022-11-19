# EffectController
# - control devices (effects and instruments)
#
# Part of ElectraOne
#
# Ableton Live MIDI Remote Script for the Electra One
#
# Author: Jaap-henk Hoepman (info@xot.nl)
#
# Distributed under the MIT License, see LICENSE
#

# Ableton Live imports (TODO: remove, obsolote)
#from _Generic.util import DeviceAppointer

# Local imports
from .config import *
from .CCInfo import CCInfo
from .PresetInfo import PresetInfo
from .Devices import get_predefined_preset_info
from .ElectraOneBase import ElectraOneBase 
from .ElectraOneDumper import ElectraOneDumper
from .GenericDeviceController import GenericDeviceController

# Default LUA script to send along an effect preset. Programs the PATCH REQUEST
# button to send a special SysEx message (0xF0 0x00 0x21 0x45 0x7E 0x7E 0xF7)
# received by ElectraOne to swap the visible preset. As complex presets may have
# more than one device defined (an patch.onRequest sends a message out for
# every device), we use device.id to diversify the outgoing message.
# (Effect presets always have device.id = 1 as the first device)
#
# Also contains formatter functions used by presets generated on the fly
DEFAULT_LUASCRIPT = """
info.setText("by www.xot.nl")

function patch.onRequest (device)
  print ("Patch Request pressed");
  if device.id == 1
    then midi.sendSysex(PORT_1, {0x00, 0x21, 0x45, 0x7E, 0x7E})
  end
end

function formatFloat (valueObject, value)
  return (string.format("%.2f",value/100))
end

function formatLargeFloat (valueObject, value)
  return (string.format("%.1f",value/10))
end

function formatdB (valueObject, value)
  return (string.format("%.1f dB",value/10))
end

function formatFreq (valueObject, value)
  return (string.format("%.1f Hz",value/10))
end

function formatPan (valueObject, value)
  if value < 0 
    then return (string.format("%iL", -value))
    else return (string.format("%iR", value))
  end
end

function formatPercent (valueObject, value)
  return (string.format("%.1f %%",value/10))
end

function formatDegree (valueObject, value)
  return (string.format("%i *",value))
end

function formatSemitone (valueObject, value)
  return (string.format("%i st",value))
end

function formatDetune (valueObject, value)
  return (string.format("%i ct",value))
end

"""

class EffectController(ElectraOneBase):
    """Control the currently selected device.
    """

    def __init__(self, c_instance):
        """Initialise an effect controller.
           (Typically called only once, after loading a song.)
           - c_instance: Live interface object (see __init.py__)
        """
        ElectraOneBase.__init__(self, c_instance)
        # referrence to the currently assigned device
        # (corresponds typically to the currently appointed device by Ableton
        self._assigned_device = None
        # generic controller associated with assigned device
        self._assigned_device_controller = None
        self._assigned_device_locked = False
        # listen to device appointment changes (created by DeviceAppointer)
        self.song().add_appointed_device_listener(self._handle_appointed_device_change)
        self.debug(0,'EffectController loaded.')

    def refresh_state(self):
        """Send the values of the controlled elements to the E1
           (to bring them in sync)
        """
        if ElectraOneBase.current_visible_slot == EFFECT_PRESET_SLOT:
            # Check that a device is assigned and that assigned_device still exists.
            # (When it gets deleted, the reference to it becomes None.)
            if self._assigned_device:
                self.debug(1,'EffCont refreshing state.')
                self._assigned_device_controller.refresh_state()
                self.debug(1,'EffCont state refreshed.')
            else:
                self.debug(1,'EffCont not refreshing state (no effect selected).')
        else:
            self.debug(2,'EffCont not refreshing state (effect not visible).')
            
    # --- initialise values ---
    
    def update_display(self):
        """ Called every 100 ms; used to remove preset from E1 if no device selected
        """
        pass
    
    def disconnect(self):
        """Called right before we get disconnected from Live
        """
        self._remove_preset_from_slot(EFFECT_PRESET_SLOT)
        if self._assigned_device_controller:
            self._assigned_device_controller.remove_listeners()
        self.song().remove_appointed_device_listener(self._handle_appointed_device_change)

    # --- MIDI ---

    def build_midi_map(self, midi_map_handle):
        """Build a MIDI map for the currently selected device    
        """
        self.debug(1,'EffCont building effect MIDI map.')
        # Check that a device is assigned and that assigned_device still exists.
        # (When it gets deleted, the reference to it becomes None.)
        if self._assigned_device:
            self._assigned_device_controller.build_midi_map(midi_map_handle)
        self.debug(1,'EffCont effect MIDI map built.')
        self.refresh_state()
        
    # === Others ===

    def _get_preset_info(self, device):
        """Get the preset info for the specified device, either externally,
           predefined or else construct it on the fly.
        """
        device_name = self.get_device_name(device)
        self.debug(2,f'Getting preset for { device_name }.')
        preset_info = get_predefined_preset_info(device_name)
        if preset_info:
            self.debug(2,'Predefined preset found')
        else:
            self.debug(2,'Constructing preset on the fly...')
            dumper = ElectraOneDumper(self.get_c_instance(), device_name, device.parameters)
            preset_info = dumper.get_preset()
        # check preset integrity; any errors will be reported in the log
        error = preset_info.validate()
        if error:
            self.debug(2,f'Issues in preset found: {error}.')
        return preset_info
    
    # --- handling presets  ----
    
    def _dump_presetinfo(self, device, preset_info):
        """Dump the presetinfo: an ElectraOne JSON preset, and the MIDI CC map
        """
        device_name = self.get_device_name(device)
        # determine path to store the dumps in (created if it doesnt exist)
        path = self._ensure_in_libdir('dumps')
        # dump the preset JSON string 
        fname = f'{ path }/{ device_name }.epr'
        self.debug(2,f'dumping device: { device_name } in { fname }.')
        s = preset_info.get_preset()
        with open(fname,'w') as f:            
            f.write(s)
        # dump the cc-map
        fname = f'{ path }/{ device_name }.ccmap'
        with open(fname,'w') as f:
            f.write('{')
            comma = False                                                   # concatenate list items with a comma; don't write a comma before the first list entry
            for p in device.parameters:
                if comma:
                    f.write(',')
                comma = True
                ccinfo = preset_info.get_ccinfo_for_parameter(p)
                if ccinfo.is_mapped():
                    f.write(f"'{ p.original_name }': { ccinfo }\n")
                else:
                    f.write(f"'{ p.original_name }': None\n")
            f.write('}')

    # --- handle device selection ---
    
    def lock_to_device(self, device):
        if device:
            self._assigned_device_locked = True
            self._assign_device(device)
            
    def unlock_from_device(self, device):
        if device and device == self._assigned_device:
            self._assigned_device_locked = False
            self._assign_device(self.song().appointed_device)

    def _assign_device(self, device):
        if device != None:
            device_name = self.get_device_name(device)
            self.debug(1,f'Assigning device { device_name }')
            if device != self._assigned_device:
                self._assigned_device = device
                preset_info = self._get_preset_info(device)
                # clean up any previously assigned device controller;
                # especially remove its listeners
                # (unfortunately we cannot rely on __del__ to do this implcitly
                # when reference to old assigned_effect_controller is overwritten
                # becuase is not called immediately, but only after garbadge collect
                if self._assigned_device_controller:
                    self._assigned_device_controller.disconnect()
                # TODO: this also sets up value listeners; but preset not uploaded yet!
                self._assigned_device_controller = GenericDeviceController(self._c_instance, device, preset_info)
                if DUMP:
                    self._dump_presetinfo(device,preset_info)
                preset = preset_info.get_preset()
                # upload preset: will also request midi map (which will also refresh state)
                self.upload_preset(EFFECT_PRESET_SLOT,preset,DEFAULT_LUASCRIPT)
            else:
                self.debug(1,'Device already assigned.')
        else:
            # this does not happen (unfortunately)
            self._assigned_device = None
            self.debug(1,'Assigning an empty device.')
            # TODO: remove device preset from E1
            self._remove_preset_from_slot(EFFECT_PRESET_SLOT)

    def _handle_appointed_device_change(self):
        device = self.song().appointed_device
        if self.is_ready() and (not self._assigned_device_locked):
            self._assign_device(device)
        else:
            self.debug(1,'Device appointment ignored because E1 not ready.')
            
