
# ElectrOne - Device definitions
#
# Ableton Live MIDI Remote Script for the Electra One
#
# Author: Jaap-henk Hoepman (info@xot.nl)
#
# Distributed under the MIT License, see LICENSE
#

# Dictionary with preset and MIDI cc mapping data for known devices
# (indexed by device.original_name)
# - The preset is a JSON string in Electra One format.
#   (The current implementation assumes that all quantized parameters
#   are 7-bit absolute CC values while all non quantized parameters are
#   14-bit absolute values)
# - The MIDI cc mapping data is a dictionary of Ableton Live original parameter
#   names with their corresponding MIDI CC values in the preset.
#

from .ElectraOneDumper import PatchInfo

DEVICES = {
'Looper': PatchInfo('{"version":2,"name":"Looper","projectId":"rPoZxhbryg2gniEI7viF","pages":[{"id":1,"name":"Page 1"}],"groups":[],"devices":[{"id":1,"name":"Generic MIDI","port":1,"channel":11}],"overlays":[{"id":1,"items":[{"label":"Stop","index":0,"value":0},{"label":"Record","index":1,"value":42},{"label":"Play","index":2,"value":85},{"label":"Overdub","index":3,"value":127}]},{"id":2,"items":[{"label":"None","index":0,"value":0},{"label":"Start Song","index":1,"value":64},{"label":"Start & Stop Song","index":2,"value":127}]},{"id":3,"items":[{"label":"Global","index":0,"value":0},{"label":"None","index":1,"value":9},{"label":"8 Bars","index":2,"value":18},{"label":"4 Bars","index":3,"value":27},{"label":"2 Bars","index":4,"value":36},{"label":"1 Bar","index":5,"value":45},{"label":"1/2","index":6,"value":54},{"label":"1/2T","index":7,"value":64},{"label":"1/4","index":8,"value":73},{"label":"1/4T","index":9,"value":82},{"label":"1/8","index":10,"value":91},{"label":"1/8T","index":11,"value":100},{"label":"1/16","index":12,"value":109},{"label":"1/16T","index":13,"value":118},{"label":"1/32","index":14,"value":127}]},{"id":4,"items":[{"label":"None","index":0,"value":0},{"label":"Follow song tempo","index":1,"value":64},{"label":"Set & Follow song tempo","index":2,"value":127}]},{"id":5,"items":[{"label":"Always","index":0,"value":0},{"label":"Never","index":1,"value":42},{"label":"Rec/OVR","index":2,"value":85},{"label":"Rec/OVR/Stop","index":3,"value":127}]}],"controls":[{"id":1,"type":"list","visible":true,"name":"STATE","color":"FFFFFF","bounds":[0,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":2},"overlayId":1}]},{"id":2,"type":"list","visible":true,"name":"SONG CONTROL","color":"529DEC","bounds":[170,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":2,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":8},"overlayId":2}]},{"id":3,"type":"fader","visible":true,"name":"SPEED","color":"C44795","bounds":[340,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":3,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc14","deviceId":1,"lsbFirst":false,"parameterNumber":6,"min":0,"max":16383}}]},{"id":4,"type":"fader","visible":true,"name":"FEEDBACK","color":"03A598","bounds":[510,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":4,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc14","deviceId":1,"lsbFirst":false,"parameterNumber":3,"min":0,"max":16383}}]},{"id":7,"type":"list","visible":true,"name":"QUANTIZATION","color":"FFFFFF","bounds":[0,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":7,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":7},"overlayId":3}]},{"id":8,"type":"list","visible":true,"name":"TEMPO CONTROL","color":"529DEC","bounds":[170,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":8,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":9},"overlayId":4}]},{"id":9,"type":"pad","mode":"toggle","visible":true,"name":"REVERSE","color":"C44795","bounds":[340,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":9,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":4,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":10,"type":"list","visible":true,"name":"MONITOR","color":"03A598","bounds":[510,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":10,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":5},"overlayId":5}]},{"id":13,"type":"pad","mode":"toggle","visible":true,"name":"DEVICE ON","color":"FFFFFF","bounds":[0,216,146,56],"pageId":1,"controlSetId":2,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":1,"onValue":127,"offValue":0},"defaultValue":"off"}]}]}'
  ,{'Device On': 1
,'State': 2
,'Feedback': 3
,'Reverse': 4
,'Monitor': 5
,'Speed': 6
,'Quantization': 7
,'Song Control': 8
,'Tempo Control': 9
})
,'Echo': PatchInfo('{"version":2,"name":"Echo","projectId":"39A2PYwx4HcVn7t38kt9","pages":[{"id":1,"name":"Echo"},{"id":2,"name":"Mod / Char"},{"id":4,"name":"Unmapped"}],"groups":[{"id":1,"pageId":1,"name":"FILTER","color":"C44795","bounds":[170,456,826,16]},{"id":2,"pageId":2,"name":"MODULATION","color":"FFFFFF","bounds":[0,104,996,16]},{"id":3,"pageId":2,"name":"GATE","color":"F49500","bounds":[0,192,486,16]},{"id":4,"pageId":2,"name":"DUCKING","color":"529DEC","bounds":[510,192,486,16]},{"id":5,"pageId":2,"name":"NOISE","color":"FFFFFF","bounds":[0,280,486,16]},{"id":6,"pageId":2,"name":"WOBBLE","color":"F45C51","bounds":[510,280,486,16]}],"devices":[{"id":1,"name":"Generic MIDI","port":1,"channel":11}],"overlays":[{"id":1,"items":[{"label":"Notes","index":0,"value":0},{"label":"Triplet","index":1,"value":42},{"label":"Dotted","index":2,"value":85},{"label":"16th","index":3,"value":127}]},{"id":2,"items":[{"label":"Pre","index":0,"value":0},{"label":"Post","index":1,"value":64},{"label":"Feedback","index":2,"value":127}]},{"id":3,"items":[{"label":"Stereo","index":0,"value":0},{"label":"Ping Pong","index":1,"value":64},{"label":"Mid/Side","index":2,"value":127}]},{"id":4,"items":[{"label":"Sine","index":0,"value":0},{"label":"Triangle","index":1,"value":25},{"label":"Saw Up","index":2,"value":51},{"label":"Saw Down","index":3,"value":76},{"label":"Square","index":4,"value":102},{"label":"Random","index":5,"value":127}]}],"controls":[{"id":1,"type":"fader","visible":true,"name":" L TIME ","color":"F45C51","bounds":[0,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":3,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":2,"type":"pad","mode":"toggle","visible":true,"name":" L SYNC ","color":"F45C51","bounds":[170,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":2,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":2,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":3,"type":"list","visible":true,"name":" L SYNC MODE ","color":"F45C51","bounds":[340,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":3,"valueId":"value"}],"values":[{"message":{"type":"cc7","parameterNumber":6,"deviceId":1},"overlayId":1,"id":"value"}]},{"id":4,"type":"fader","visible":true,"name":" L OFFSET ","color":"F45C51","bounds":[510,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":4,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":7,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":5,"type":"fader","visible":true,"name":" REVERB LEVEL ","color":"529DEC","bounds":[680,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":5,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":42,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":6,"type":"fader","visible":true,"name":" STEREO WIDTH ","color":"03A598","bounds":[850,40,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":6,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":51,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":7,"type":"fader","visible":true,"name":" R TIME ","color":"F49500","bounds":[0,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":7,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":8,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":8,"type":"pad","mode":"toggle","visible":true,"name":" R SYNC ","color":"F49500","bounds":[170,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":8,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":9,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":9,"type":"list","visible":true,"name":" R SYNC MODE ","color":"F49500","bounds":[340,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":9,"valueId":"value"}],"values":[{"message":{"type":"cc7","parameterNumber":12,"deviceId":1},"overlayId":1,"id":"value"}]},{"id":10,"type":"fader","visible":true,"name":" R OFFSET ","color":"F49500","bounds":[510,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":10,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":13,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":11,"type":"list","visible":true,"name":" REVERB LOC ","color":"529DEC","bounds":[680,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":11,"valueId":"value"}],"values":[{"message":{"type":"cc7","parameterNumber":44,"deviceId":1},"overlayId":2,"id":"value"}]},{"id":12,"type":"fader","visible":true,"name":" OUTPUT GAIN ","color":"03A598","bounds":[850,128,146,56],"pageId":1,"controlSetId":1,"inputs":[{"potId":12,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":20,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":13,"type":"pad","mode":"toggle","visible":true,"name":" LINK ","color":"F49500","bounds":[0,216,146,56],"pageId":1,"controlSetId":2,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":14,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":17,"type":"fader","visible":true,"name":" REVERB DECAY ","color":"529DEC","bounds":[680,216,146,56],"pageId":1,"controlSetId":2,"inputs":[{"potId":5,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":43,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":18,"type":"fader","visible":true,"name":" DRY WET ","color":"03A598","bounds":[850,216,146,56],"pageId":1,"controlSetId":2,"inputs":[{"potId":6,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":52,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":19,"type":"fader","visible":true,"name":" INPUT GAIN ","color":"FFFFFF","bounds":[0,304,146,56],"pageId":1,"controlSetId":2,"inputs":[{"potId":7,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":19,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":20,"type":"fader","visible":true,"name":" FEEDBACK ","color":"FFFFFF","bounds":[170,304,146,56],"pageId":1,"controlSetId":2,"inputs":[{"potId":8,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":16,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":23,"type":"list","visible":true,"name":" CHANNEL MODE ","color":"529DEC","bounds":[680,304,146,56],"pageId":1,"controlSetId":2,"inputs":[{"potId":11,"valueId":"value"}],"values":[{"message":{"type":"cc7","parameterNumber":18,"deviceId":1},"overlayId":3,"id":"value"}]},{"id":25,"type":"pad","mode":"toggle","visible":true,"name":" CLIP DRY ","color":"FFFFFF","bounds":[0,392,146,56],"pageId":1,"controlSetId":3,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":21,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":26,"type":"pad","mode":"toggle","visible":true,"name":" FEEDBACK INV ","color":"FFFFFF","bounds":[170,392,146,56],"pageId":1,"controlSetId":3,"inputs":[{"potId":2,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":17,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":31,"type":"pad","mode":"toggle","visible":true,"name":" DEVICE ON ","color":"FFFFFF","bounds":[0,480,146,56],"pageId":1,"controlSetId":3,"inputs":[{"potId":7,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":1,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":32,"type":"pad","mode":"toggle","visible":true,"name":" FILTER ON ","color":"C44795","bounds":[170,480,146,56],"pageId":1,"controlSetId":3,"inputs":[{"potId":8,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":28,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":33,"type":"fader","visible":true,"name":" LP RES ","color":"C44795","bounds":[340,480,146,56],"pageId":1,"controlSetId":3,"inputs":[{"potId":9,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":32,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":34,"type":"fader","visible":true,"name":" LP FREQ ","color":"C44795","bounds":[510,480,146,56],"pageId":1,"controlSetId":3,"inputs":[{"potId":10,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":31,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":35,"type":"fader","visible":true,"name":" HP FREQ ","color":"C44795","bounds":[680,480,146,56],"pageId":1,"controlSetId":3,"inputs":[{"potId":11,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":29,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":36,"type":"fader","visible":true,"name":" HP RES ","color":"C44795","bounds":[850,480,146,56],"pageId":1,"controlSetId":3,"inputs":[{"potId":12,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":30,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":37,"type":"pad","mode":"toggle","visible":true,"name":" MOD SYNC ","color":"FFFFFF","bounds":[0,40,146,56],"pageId":2,"controlSetId":1,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":35,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":38,"type":"list","visible":true,"name":" MOD WAVE ","color":"FFFFFF","bounds":[170,40,146,56],"pageId":2,"controlSetId":1,"inputs":[{"potId":2,"valueId":"value"}],"values":[{"message":{"type":"cc7","parameterNumber":33,"deviceId":1},"overlayId":4,"id":"value"}]},{"id":43,"type":"fader","visible":true,"name":" MOD FREQ ","color":"FFFFFF","bounds":[0,128,146,56],"pageId":2,"controlSetId":1,"inputs":[{"potId":7,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":34,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":44,"type":"fader","visible":true,"name":" MOD PHASE ","color":"FFFFFF","bounds":[170,128,146,56],"pageId":2,"controlSetId":1,"inputs":[{"potId":8,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":37,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":45,"type":"pad","mode":"toggle","visible":true,"name":" MOD 4X ","color":"FFFFFF","bounds":[340,128,146,56],"pageId":2,"controlSetId":1,"inputs":[{"potId":9,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":41,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":46,"type":"fader","visible":true,"name":" DLY < MOD ","color":"FFFFFF","bounds":[510,128,146,56],"pageId":2,"controlSetId":1,"inputs":[{"potId":10,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":39,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":47,"type":"fader","visible":true,"name":" FLT < MOD ","color":"FFFFFF","bounds":[680,128,146,56],"pageId":2,"controlSetId":1,"inputs":[{"potId":11,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":40,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":48,"type":"fader","visible":true,"name":" ENV MIX ","color":"FFFFFF","bounds":[850,128,146,56],"pageId":2,"controlSetId":1,"inputs":[{"potId":12,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":38,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":49,"type":"pad","mode":"toggle","visible":true,"name":" GATE ON ","color":"F49500","bounds":[0,216,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":22,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":50,"type":"fader","visible":true,"name":" GATE THR ","color":"F49500","bounds":[170,216,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":2,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":23,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":51,"type":"fader","visible":true,"name":" GATE RELEASE ","color":"F49500","bounds":[340,216,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":3,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":24,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":52,"type":"pad","mode":"toggle","visible":true,"name":" DUCK ON ","color":"529DEC","bounds":[510,216,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":4,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":25,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":53,"type":"fader","visible":true,"name":" DUCK THR ","color":"529DEC","bounds":[680,216,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":5,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":26,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":54,"type":"fader","visible":true,"name":" DUCK RELEASE ","color":"529DEC","bounds":[850,216,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":6,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":27,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":55,"type":"pad","mode":"toggle","visible":true,"name":" NOISE ON ","color":"FFFFFF","bounds":[0,304,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":7,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":45,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":56,"type":"fader","visible":true,"name":" NOISE AMT ","color":"FFFFFF","bounds":[170,304,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":8,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":46,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":57,"type":"fader","visible":true,"name":" NOISE MRPH ","color":"FFFFFF","bounds":[340,304,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":9,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":47,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":58,"type":"pad","mode":"toggle","visible":true,"name":" WOBBLE ON ","color":"F45C51","bounds":[510,304,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":10,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":48,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":59,"type":"fader","visible":true,"name":" WOBBLE AMT ","color":"F45C51","bounds":[680,304,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":11,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":49,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":60,"type":"fader","visible":true,"name":" WOBBLE MRPH ","color":"F45C51","bounds":[850,304,146,56],"pageId":2,"controlSetId":2,"inputs":[{"potId":12,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":50,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":61,"type":"pad","mode":"toggle","visible":true,"name":" REPITCH ","color":"529DEC","bounds":[0,392,146,56],"pageId":2,"controlSetId":3,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"id":"value","message":{"type":"cc7","deviceId":1,"parameterNumber":15,"onValue":127,"offValue":0},"defaultValue":"off"}]},{"id":109,"type":"fader","visible":true,"name":" L 16TH ","color":"FFFFFF","bounds":[0,40,146,56],"pageId":4,"controlSetId":1,"inputs":[{"potId":1,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":5,"deviceId":1,"lsbFirst":false,"min":1,"max":16},"id":"value"}]},{"id":110,"type":"fader","visible":true,"name":" R 16TH ","color":"FFFFFF","bounds":[170,40,146,56],"pageId":4,"controlSetId":1,"inputs":[{"potId":2,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":11,"deviceId":1,"lsbFirst":false,"min":1,"max":16},"id":"value"}]},{"id":111,"type":"fader","visible":true,"name":" L DIVISION ","color":"FFFFFF","bounds":[340,40,146,56],"pageId":4,"controlSetId":1,"inputs":[{"potId":3,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":4,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":112,"type":"fader","visible":true,"name":" R DIVISION ","color":"FFFFFF","bounds":[510,40,146,56],"pageId":4,"controlSetId":1,"inputs":[{"potId":4,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":10,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]},{"id":115,"type":"fader","visible":true,"name":" MOD RATE ","color":"FFFFFF","bounds":[0,128,146,56],"pageId":4,"controlSetId":1,"inputs":[{"potId":7,"valueId":"value"}],"values":[{"message":{"type":"cc14","parameterNumber":36,"deviceId":1,"lsbFirst":false,"min":0,"max":16383},"id":"value"}]}]}'
  ,{'Device On': 1
,'L Sync': 2
,'L Time': 3
,'L Division': 3
,'L 16th': 3
,'L Sync Mode': 6
,'L Offset': 7
,'R Time': 8
,'R Sync': 9
,'R Division': 8
,'R 16th': 8
,'R Sync Mode': 12
,'R Offset': 13
,'Link': 14
,'Repitch': 15
,'Feedback': 16
,'Feedback Inv': 17
,'Channel Mode': 18
,'Input Gain': 19
,'Output Gain': 20
,'Clip Dry': 21
,'Gate On': 22
,'Gate Thr': 23
,'Gate Release': 24
,'Duck On': 25
,'Duck Thr': 26
,'Duck Release': 27
,'Filter On': 28
,'HP Freq': 29
,'HP Res': 30
,'LP Freq': 31
,'LP Res': 32
,'Mod Wave': 33
,'Mod Freq': 34
,'Mod Sync': 35
,'Mod Rate': 34
,'Mod Phase': 37
,'Env Mix': 38
,'Dly < Mod': 39
,'Flt < Mod': 40
,'Mod 4x': 41
,'Reverb Level': 42
,'Reverb Decay': 43
,'Reverb Loc': 44
,'Noise On': 45
,'Noise Amt': 46
,'Noise Mrph': 47
,'Wobble On': 48
,'Wobble Amt': 49
,'Wobble Mrph': 50
,'Stereo Width': 51
,'Dry Wet': 52
})
}


# Return the predefined patch information for a device, None if it doesn't exist
def get_predefined_patch_info(device_original_name):
    # FIXME: try to read from file
    if device_original_name in DEVICES:
        return DEVICES[device_original_name]
    else:
        return None
