import errno


class DeviceReportsError(Exception):
    def __init__(self, errno):
        self.code = errno

    def __str__(self) -> str:
        message = errno.errorcode[self.code]
        return f"Connection to Raspberry Pi successful, but device reports error {self.code} ({message})\nPlease ensure all header pins are securely connected!"
