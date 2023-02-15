import typing

from PyQt6 import QtGui


class IntValidator(QtGui.QValidator):

    def __init__(self):
        super().__init__()

    def validate(self, s: str, pos: int) -> typing.Tuple[QtGui.QValidator.State, str, int]:
        if not s.isdigit():
            if s == "" and pos == 0:
                return QtGui.QValidator.State.Acceptable, s, pos

            return QtGui.QValidator.State.Invalid, s, pos

        number = int(s)
        if pos == 1 and number == 0:
            return QtGui.QValidator.State.Invalid, s, pos

        return QtGui.QValidator.State.Acceptable, s, pos