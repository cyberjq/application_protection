import base64

from cryptography.fernet import Fernet

from PIL import Image, ImageDraw


def encrypt(path_to_image: str, text: str, key: str, balance: int):
    img = dict()
    size = dict()
    coord = dict()

    img["image"] = Image.open(path_to_image)
    img["draw"] = ImageDraw.Draw(img["image"])
    img["pix"] = img["image"].load()

    size["width"] = img["image"].size[0]
    size["height"] = img["image"].size[1]

    text = _des_encrypt(text, key)
    binary_text = _text_to_binary(text)
    list_two = _split_count(''.join(binary_text), balance)

    coord["x"] = 0
    coord["y"] = 0
    count = 0

    for i in list_two:
        rgb = img["pix"][coord["x"], coord["y"]]

        (red, green, blue) = _balance_channel([rgb[0], rgb[1], rgb[2]], i)

        img["draw"].point((coord["x"], coord["y"]), (red, green, blue))

        if coord["x"] < (size["width"] - 1):
            coord["x"] += 1

        elif coord["y"] < (size["height"] - 1):
            coord["y"] += 1
            coord["x"] = 0

        else:
            raise OverflowError("Данные слишком длинные для данного изображения")

        count += 1

    img["count"] = count

    return img


def decrypt(path_to_image: str, key: str) -> str:
    balance = int(key.split('$')[0])
    count = int(key.split('$')[1])
    end_key = key.split('$')[2]

    img = dict()
    coord = dict()

    img["image"] = Image.open(path_to_image)
    img["width"] = img["image"].size[0]
    img["height"] = img["image"].size[1]
    img["pix"] = img["image"].load()

    coord["x"] = 0
    coord["y"] = 0
    code = ''

    i = 0
    while i < count:
        pixels = img["pix"][coord["x"], coord["y"]]

        pixel = str(bin(max(pixels[:-1])))

        if balance == 4:
            code += pixel[-4] + pixel[-3] + pixel[-2] + pixel[-1]

        elif balance == 3:
            code += pixel[-3] + pixel[-2] + pixel[-1]

        elif balance == 2:
            code += pixel[-2] + pixel[-1]

        else:
            code += pixel[-1]

        if coord["x"] < (img["width"] - 1):
            coord["x"] += 1
        else:
            coord["y"] += 1
            coord["x"] = 0

        i += 1

    outed = _binary_to_text(_split_count(code, 8))
    return _des_decrypt(''.join(outed), end_key)


def _find_max_index(array):
    max_num = array[0]
    index = 0

    for i, val in enumerate(array):
        if val > max_num:
            max_num = val
            index = i

    return index


def _balance_channel(colors, pix):
    max_color = _find_max_index(colors)
    colors[max_color] = int(_last_replace(bin(colors[max_color]), pix), 2)

    while True:
        max_sec = _find_max_index(colors)
        if max_sec != max_color:
            colors[max_sec] = colors[max_color] - 1
        else:
            break

    return colors


def _des_encrypt(text, key):
    cipher = Fernet(base64.b64encode(key.encode()))
    result = cipher.encrypt(text.encode())

    return result.decode()


def _des_decrypt(text, key):
    cipher = Fernet(base64.b64encode(key.encode()))
    result = cipher.decrypt(text.encode())
    return result.decode()


def _split_count(text, count):
    result = list()
    txt = ''
    var = 0

    for i in text:
        if var == count:
            result.append(txt)
            txt = ''
            var = 0

        txt += i
        var += 1

    result.append(txt)

    return result


def _last_replace(main_string, last_symbols):
    return str(main_string)[:-len(last_symbols)] + last_symbols


def _text_to_binary(event):
    return ['0' * (8 - len(format(ord(elem), 'b'))) + format(ord(elem), 'b') for elem in event]


def _binary_to_text(event):
    return [chr(int(str(elem), 2)) for elem in event]
