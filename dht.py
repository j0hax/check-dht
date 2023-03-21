import serial
import json
import nagiosplugin
import errno


def read_data(port, baud):
    ser = serial.Serial(port, baud)
    line = ser.readline()
    return json.loads(line)


class DeviceReportsError(Exception):
    def __init__(self, errno):
        self.code = errno

    def __str__(self) -> str:
        message = errno.errorcode[self.code]
        return f"Connection to Raspberry Pi successful, but device reports error {self.code} ({message})\nPlease ensure all header pins are securely connected!"

class DHT(nagiosplugin.Resource):
    """Domain model: digital temperature and humidity."""

    def __init__(self, port, baud):
        self.port = port
        self.baud = baud

    def probe(self):
        data = read_data(self.port, self.baud)

        # Check the error
        if data["error"] != 0:
            raise DeviceReportsError(data["error"])

        return [
            nagiosplugin.Metric("temperature", data["temperature"], uom="°C"),
            nagiosplugin.Metric(
                "onboard", data["onboard"], uom="°C", context="temperature"
            ),
            nagiosplugin.Metric("humidity", data["humidity"], uom="%", min=0, max=100),
        ]
