#!/usr/bin/env python3
import serial
import json
import argparse
import nagiosplugin


def read_data(port, baud):
    ser = serial.Serial(port, baud)
    line = ser.readline()
    return json.loads(line)


class DHT(nagiosplugin.Resource):
    """Domain model: digital temperature and humidity."""

    def __init__(self, port, baud):
        self.port = port
        self.baud = baud

    def probe(self):
        data = read_data(self.port, self.baud)
        return [
            nagiosplugin.Metric(
                "onboard", data["onboard"], uom="°C", context="temperature"
            ),
        ]


def main():
    parser = argparse.ArgumentParser(
        description="Nagios Plugin to monitor DHT22/AM2302 data",
        epilog="(c) Johannes Arnold 2023. This software is published under the terms of the GNU GPLv3. For the companion project to this plugin, see https://github.com/j0hax/dht22",
    )

    parser.add_argument(
        "-p",
        "--port",
        default="/dev/ttyACM0",
        help="the serial file to read from",
    )

    parser.add_argument(
        "-b", "--baud", default=115200, help="baudrate of the serial port"
    )

    parser.add_argument(
        "-w",
        "--warning",
        metavar="TEMP",
        default=30,
        help="return warning if air temperature is outside TEMP",
    )

    parser.add_argument(
        "-c",
        "--critical",
        metavar="TEMP",
        default=40,
        help="return critical if air temperature is outside TEMP",
    )

    parser.add_argument(
        "--humidity-warning",
        metavar="PERCENT",
        default=40,
        help="return warning if humidity is outside PERCENT",
    )

    parser.add_argument(
        "--humidity-critical",
        metavar="PERCENT",
        default=50,
        help="return critical if humidity is outside PERCENT",
    )

    args = parser.parse_args()

    check = nagiosplugin.Check(
        DHT(args.port, args.baud),
        nagiosplugin.ScalarContext(
            "temperature", args.warning, args.critical, fmt_metric="{value} °C"
        ),
        nagiosplugin.ScalarContext(
            "humidity",
            args.humidity_warning,
            args.humidity_critical,
            fmt_metric="{value}%",
        ),
    )

    check.main()


if __name__ == "__main__":
    main()
