#!/usr/bin/python3 -u
from tango import Database, DevFailed, AttrWriteType, DevState, DeviceProxy, DispLevel
from tango.server import device_property
from tango.server import Device, attribute, command
from w1thermsensor import W1ThermSensor   # Easy use of 1-Wire temperature sensors

# ======================================================
class temperature_probe(Device):
    
    temperature_0_id = device_property(
        dtype="str", default_value="1a23b456c789"
    )
    
    temperature_1 = attribute(
        dtype="float",
        label="Temp 1",
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
    )
    
    def init_device(self):
        self.set_state(DevState.OFF)
        
    
    @command
    def delete_device(self):
        self.stop_all()
        self.set_state(DevState.OFF)

    
    def read_temperature_0(self):
        temperature = W1ThermSensor(40, temperature_0_id).get_temperature()
        self.debug_stream(str(temperature))
        return temperature                        

        
        
if __name__ == "__main__":
    DebrisTape.run_server()
