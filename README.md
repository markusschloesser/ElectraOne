# ElectraOne

Ableton Live MIDI Remote Script for the Electra One.

## What it does

This Ableton Live MIDI Remote script allows you to control the parameters of the currently selected device in Ableton Live using the [Electra One](https://electra.one). 

It can also be used to dump Electra One presets for Ableton Live devices with sensible default control assignments.

Finally, it also contains a mixer preset to control the track mixers, returns, master mixer and transport.

## The mixer

The mixer controls five consecutive session tracks parameters: pan, volume, mute, solo and arm. The 'prev tracks' and 'next tracks' buttons on the main page switch control to the previous five or next five tracks (never shifting left of the first or right of the last visible track). Inserted or removed tracks are automatically handled. 

The 'Main' mixer page also contains control the master pan, volume, cue volume, and solo switch. And it contains transport controls: play/stop, record, rewind, and forward.

<img main>

For each track, the level of at most six sends can be controlled (see the 'Sends' page). 

<img sends>

The return track corresponding to each send can be managed using the controls on the 'Returns' page: pan, volume, and mute.

Finally a separate 'Channel EQs' page contains controls to control the parameters of a Channel EQ device, when present *as the last device* on an audio/midi track or the master track.

All controls on all pages are synced with the values of the parameters in Live they control as soon as a selection changes, or when parameters in Live are changed through the UI or using a different controller.

## Alternative mixer designs

There is nothing specific about the design of the mixer apart from the MIDI channel, ELectra One port and CC number assignments of individual controls. This means you can freely redesign the mixer to your own needs, e.g one where tracks are layed out horizontally instead of vertically (such that all track controls are active at the same time).

The Remote Script uploads a default mixer defined in ```Devices.py```. This can be changed to suit your needs.

## How it controls the currently selected device

It looks for a preloaded preset for the selected device in ```Devices.py``` and uses that if it exists. You can add your own favourite preset layout here. The easiest way to create such a preset (to ensure that it properly interfaces with this Electra One remote script) is to modify dumps made by this script. See [below](##preset-dumps).

If no preloaded preset exists, it creates a preset on the fly. The preset is uploaded to the Electra One to the currently selected preset slot (*overwriting any preset currently present in that slot*). All controls in the preset are mapped to the corresponding parameter in the device.

<img>

When constructing presets:
- on/off parameters are shown as toggles on the Electra One. 
- other 'quantised' parameters are shown as lists on the Electra One, using the possible values reported by Ableton. (In Electra One terms, these are turned into 'overlays' added to the preset.)
- non-quantised parameters are shown as faders on the Electra One. As many faders as possible are assigned to 14bit CCs. (These CCs actually occupy *two* slots in the CC map, see below.)
- Integer valued, non-quantised, parameters are shown as integer-valued faders on the Electra One. Other faders simply show a value within the minimum - maximum CC value range.

Note that large devices with many parameters may create a preset with more than one page.

## Device preset dumps

Constructed presets can be dumped, along with associated CC mapping information for fine tuning the preset as shown on the Electra One (e.g. parameter layout, assignment over pages, colours, groups). The  updated information can be added to ```Devices.py``` to turn it into a preloaded preset.

Such a dump constructs a file ```<devicename>.json``` with the JSON preset (which can be uploaded to the [Electra Editor](Https://app.electra.one)), and a file ```<devicename>.ccmap``` listing for each named parameter the following tuple:

- the MIDI channel,
- whether it is a 14bit controler (1: yes, 0: no), and
- the CC parameter number (between 0 and 127) that controls it in the preset. ```None``` means the parameter is not/could not be mapped. 

Note that the actual CC parameter used for a 14bit control is cc_np *and* cc_no+32 (because by convention a 14bit CC value is sent using the base CC and its 'shadow' parameter 32 higher. (This means the constructed map may appear to have holes in the 32-63 and 96-127 range.)

The construction of presets is controlled by several constants defined in ```config.py```

Dumps are written in the folder ```<LOCALDIR>/dumps``` (see documentation of ```LOCALDIR``` below).


## Preloaded presets

Preloaded presets are stored in ```Devices.py```. The Python script ```makedevices``` creates this file based on all presets stored in ```./preloaded``` (using the ```<devicename>.epr``` and ```<devicename>.cmap``` it finds there).

You can copy a dumped preset in ```./dumps``` to ```./preloaded``` (renaming the ```.json``` extension to ```.epr```). Better still, upload the ```json``` patch in ```./dumps``` to the Electra Editor, change the layout, and then download it again, saving it to ```./preloaded```. Do *not* change the assigned CC parameter numbers (these should be the same in both the patch (```.epr```) and the corresponding CC-map (```.ccmap```). 

The remote script is actually completely oblivious about the actual preset it uploads to the Electra One: it only uses the information in the CC-map to map CC's to Ableton Live parameters, to decide which MIDI channel to use, and to decide whether to use 7 or 14 bit control assignments. It is up to the patch to actually have the CCs listed in the map present, have it mapped to a device with that correct MIDI channel, and to ensure that the number of bits assigned is consistent. Also, the MIDI port in the preset must correspond to what the remote script expects; so leave that value alone.

Apart from that, anything  goes. This means you can freely change controller names, specify value ranges and assign special formatter functions. Also, you can remove controls that you hardly ever use and that would otherwise clutter the interface.

 
## Warning

**This is *alpha* software.**

It was built using the [excellent resources](https://structure-void.com/ableton-live-midi-remote-scripts/) provided by Julien Bayle (StructureVoid), and Hanz Petrov's [introduction to remote scripts](http://remotescripts.blogspot.com/2010/03/introduction-to-framework-classes.html). Also the incredibly well maintained [documentation](https://docs.electra.one) for the Electra One itself was super useful.

However, official documentation from Ableton to program MIDI remote scripts is unfortunately missing. This means the code seems to work, but I don't really know *why* it works. Clearly, this is dangerous. 

**Use at your own risk!**

## Installation

Copy all Python files to your local Ableton MIDI Live Scripts folder (```~/Music/Ableton/User Library/Remote Scripts/``` on MacOS and
```~\Documents\Ableton\User Library\Remote Scripts``` on Windows) into a directory called ```ElectraOne````.

Add ElectraOne as a Control Surface in Live > Preferences > MIDI. Set the input port to ```Electr Controller (Electra Port 1)``` and the output port to ```Electr Controller (Electra Port 1)```. For both, tick the *Remote* boxes in the MIDI Ports table below. See:

[img]

A patch for any device selected (the 'Blue Hand') will automatically be constructed (or loaded), uploaded and then mapped to the Electra One

See ```~/Library/Preferences/Ableton/Live <version>/Log.txt``` for any error messages (on MacOS).

## Configuring

The behaviour of the remote script can be changed by editing ```config.py ```:

- ```LOCALDIR```determines where external files are read and written. This is first tried as a directory relative to the user's home directory; if that doesn't exist, it is interpreted as an absolute path. If that also doesn't exist, then the user home directory is used instead (and ```./dumps``` or ```./user-presets``` are not appended).
- ```DEBUG``` the amount of debugging information that is written to the log file. Larger values mean more logging. Set to ```0``` to create no log entries and to speed up the script.
- ```DUMP ``` controls whether the preset and CC map information of the  currently selected device is dumped  (to ```LOCALDIR/dumps```).

The following constants *only* influence the construction of presets 'on the fly' and do not affect preloaded presets:

- ```ORDER``` specifies whether presets that are constructed on the fly arrange parameters in the preset in alphabetical order (```ORDER_SORTED```),  simply in the order given by Ableton (```ORDER_ORIGINAL```) or in the order defined in the Ableton Live remote script framework (```ORDER_DEVICEDICT```). This is the same order as used by most other remote controllers, as this limits the shown controllers to only the most significant devices. Indeed, when selecting the latter option, any parameters not in the 'DEVICE_DICT' are not included in the JSON preset. (They 'are' included in the CC map for reference, with a mapping of ```None```, but *not* in the dumped preset; you may therefore want to use ```ORDER_SORTED``` when dumping presets.)
- ```MAX_CC7_PARAMETERS``` and ```MAX_CC14_PARAMETERS``` limits the number of parameters assigned as CC7 or CC14 parameters. If ```-1``` all parameters are included (limited by the number of available MIDI channels and CC parameter slots): this is a good setting when dumping devices and/or when setting ```ORDER = ORDER_DEVICEDICT```
- ```MIDI_EFFECT_CHANNEL``` is the first MIDI channel to use to assign device parameters controls to.
- ```MAX_MIDI_EFFECT_CHANNELS``` limits the number of MIDI channels used in a preset constructed on the fly; -1 means all MIDI channels are used. If this means that there are more parameters then available CC numbers, those parameters are not assigned.

The following constants deal with the mixer preset.
- ```MIDI_MASTER_CHANNEL```,  ```MIDI_TRACKS_CHANNEL``` and ```MIDI_SENDS_CHANNEL``` set the distinct MIDI channels to map the master, track, and sends controls to. See the [technical documentation](./DOCUMENTATION.md) for details.
- ```MAX_NO_OF_SENDS``` sets the maximum number of sends (and return tracks) present on the controller (currently 6).
- ```NO_OF_TRACKS``` sets the number of tracks present on the controller (currently 5).
- ```FORW_REW_JUMP_BY_AMOUNT```the number of beats to jump ahead or back when rewinding or moving forward.

## Current limitations

- User-defined presets not defined yet. (You *can* add them to ```Devices.py```.)
- Value handling is quite rudimentary at the moment. Values do not follow the way values are shown in Ableton (and other remote controllers like Novation RemoteSL line), like showing the actual float value, percentages, semitones etc.
- Uploading large patches is *slow*. (Best to stick to preloaded patches or setting ```ORDER = ORDER_DEVICEDICT```, which is the default.)
- The track and master equalisers in the mixer preset are not supported yet.

## Dependencies

This project depends on:

- Ableton Live 11, tested with version 11.1.1 (code relies Abelton Live supporting Python 3.6).
- Electra One firmware version 2.1.8a (to allow sending of both SysEx preset uploads and MIDI CC changes over *one* MIDI port). See [these instructions for uploading firmware](https://docs.electra.one/troubleshooting/hardrestart.html#recovering-from-a-system-freeze) that you can [download here](https://docs.electra.one/downloads/firmware.html).

## Recovering from errors

Should the Electra get bogged with presets or freeze, use this procedure for a 'factory reset'.

1. Disconnect Electra from the USB power.
2. Press and hold left middle button.
3. While keeping the button pressed, connect the USB power.
4. Keep the button pressed until the splash screen animation is completed

This procedure will remove all presets, Lua scripts, config files.

See the [section on dependencies](##dependencies) on how to update the firmware.

## Bug reports

If you encounter something you believe is a bug, please report it to me by email: [info@xot.nl](mailto:info@xot.nl). 

In the bug report please include:

- a concise description of the bug as subject,
- the firmware version your Electra One runs,
- the version of Ableton Live you are running,
- the operating system (and version) Live runs on, and 
- a longer description of the bug, including what conditions seem to cause it and how exactly the bug manifests itself. Includes the (relevant contents) of the log-file (see above). If necessary, increase ```DEBUG```, restart Live, and trigger the bug again.

Before submitting a bug report, please have a look at the [current issues](https://github.com/xot/ElectraOne/issues) to see whether your bug has already been reported on earlier. You can also monitor this page to keep track of how your bug is being resolved.
