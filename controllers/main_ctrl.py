from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from model import model

class MainController(QObject):
    def __init__(self, model) -> None:
        super().__init__()
        
        self.model = model

    amount_changed = pyqtSignal(int)
    even_odd_changed = pyqtSignal(str)
    enable_reset_changed = pyqtSignal(bool)

    @pyqtSlot(int)
    def change_amount(self, value: int):
        self.amount_changed.emit(value)
        amount_parity = model.parity(value)
        self.even_odd_changed.emit(amount_parity)
        if value: self.enable_reset_changed.emit(True)

    @pyqtSlot(bool)
    def reset_amount(self):
        self.change_amount(0)
        self.enable_reset_changed.emit(False)

# from PyQt5.QtCore import QObject, pyqtSlot


# class MainController(QObject):
#     def __init__(self, model):
#         super().__init__()

#         self._model = model

#     @pyqtSlot(int)
#     def change_amount(self, value):
#         self._model.amount = value

#         # calculate even or odd
#         self._model.even_odd = 'odd' if value % 2 else 'even'

#         # calculate button enabled state
#         self._model.enable_reset = True if value else False
