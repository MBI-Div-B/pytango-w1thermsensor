#!/usr/bin/python3 -u
import tango
from tango import (
    Database,
    DevFailed,
    AttrWriteType,
    DevState,
    DeviceProxy,
    DispLevel,
    READ,
    Attr,
)
from tango.server import class_property, device_property
from tango.server import Device, attribute, command
from w1thermsensor import W1ThermSensor  # Easy use of 1-Wire temperature sensors


# ======================================================
class TemperatureProbe(Device):
    probe_ids = device_property(dtype=(str,))

    def init_device(self):
        self.set_state(DevState.ON)
        self.info_stream("init")
        # self.debug_stream(f"List of strings = {self.probe_ids}")
        self.probe_ids = ("3c01d6077014", "3c01d607d7c6", "3c01d6075e7d")
        self.debug_stream(f"List of strings = {self.probe_ids}")

    @command
    def delete_device(self):
        self.stop_all()
        self.set_state(DevState.OFF)

    def initialize_dynamic_attributes(self):
        # create automaticly attributes and read methodes of all ports for enabled port_type
        for j, probe_id in enumerate(self.probe_ids):
            attr_dict = dict(
                name="Probe_{nr}".format(nr=probe_id), dtype=tango.DevFloat, access=READ
            )
            self.make_attribute(attr_dict)

    def make_attribute(self, attr_dict):
        props = ["name", "dtype", "access"]
        attr_dict_ = attr_dict.copy()

        # remove key-value-paar and print out value of entry k
        name, dtype, access = [attr_dict_.pop(k) for k in props]
        new_attr = Attr(name, dtype, access)
        prop = tango.UserDefaultAttrProp()
        # build attribute for all enabled ports

        for entry in attr_dict.items():
            new_attr.set_default_properties(prop)
            self.add_attribute(
                new_attr,
                r_meth=self.read_general,
            )

    def read_general(self, attr):
        # read out data
        name = attr.get_name()

        probe_id = name.split("_")[1]
        self.info_stream(probe_id)
        temperature = W1ThermSensor(40, probe_id).get_temperature()
        print(temperature)
        attr.set_value(temperature)


if __name__ == "__main__":
    TemperatureProbe.run_server()
