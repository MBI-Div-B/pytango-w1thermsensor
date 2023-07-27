from .TemperatureProbe import TemperatureProbe


def main():
    import sys
    import tango.server

    args = ["TemperatureProbe"] + sys.argv[1:]
    tango.server.run((TemperatureProbe,), args=args)
