from typing import NamedTuple
from enum import Enum

class DeviceInfo(NamedTuple):
    type: str
    protocol: str

class Device(Enum):
    SERVER = DeviceInfo('server', 'FTP')
    CAMERA = DeviceInfo('camera', 'SCP')
    LAPTOP = DeviceInfo('laptop', 'FTP')
    DOOR = DeviceInfo('door', 'SCP')

print(Device.SERVER.value.protocol)
