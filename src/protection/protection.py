import getpass
import os

import src.protection.crypto as crypto
import src.protection.system_info as system_info

_IMAGE_NAME = "image"
_IMAGE_NAME_SAVE = "image.png"
_FILE_NAME = "key.dat"


def _get_root_path():
    user = getpass.getuser()
    return f"{os.getenv('SystemDrive')}\\Users\\{user}\\.myapp"


def is_activated() -> bool:
    root_path = _get_root_path()

    if not (os.path.exists(root_path)
            and os.path.isfile(f"{root_path}\\{_FILE_NAME}") and os.path.isfile(f"{root_path}\\{_IMAGE_NAME_SAVE}")):
        return False

    with open(f"{root_path}\\{_FILE_NAME}", "r") as f:
        key = f.readline()

    text = crypto.decrypt(f"{root_path}\\{_IMAGE_NAME_SAVE}", key)

    return text == system_info.get_system_info()


def activate(image_name: str = _IMAGE_NAME):
    root_path = _get_root_path()
    files = list(filter(lambda file: file.startswith(image_name), os.listdir()))
    if not files:
        raise FileNotFoundError(f"Не удалось найти файл с названием {image_name}]", False, image_name)

    image_name = files[0]

    text = system_info.get_system_info()
    balance = 1
    key = os.getenv("KEY")
    img = crypto.encrypt(image_name, text, key, balance)

    if not os.path.exists(root_path):
        os.mkdir(root_path)

    img["image"].save(f"{root_path}\\{_IMAGE_NAME_SAVE}", "PNG")

    with open(f"{root_path}\\{_FILE_NAME}", "w") as file:
        file.write(f"{balance}${img['count']}${key}")
