import os
import sys


def _get_motherboard_serial_number() -> str:
    os_type = sys.platform.lower()
    if "win" in os_type:
        command = "wmic csproduct get uuid"
    elif "linux" in os_type:
        command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"

    return os.popen(command).read().replace("\n", "").replace("	", "").replace(" ", "")


def _get_hard_serial_number() -> str:
    os_type = sys.platform.lower()
    if "win" in os_type:
        command = "wmic diskdrive get SerialNumber"
    elif "linux" in os_type:
        command = ""

    return os.popen(command).read().replace("\n", "").replace("	", "").replace(" ", "")


def get_system_info():
    return f"{_get_motherboard_serial_number()}-{_get_hard_serial_number()}"