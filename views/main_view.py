from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        self._ui.pushButton_reset.clicked.connect(self._main_controller.reset_amount)

        # listen for model event signals
        self._main_controller.amount_changed.connect(self.on_amount_changed)
        self._main_controller.even_odd_changed.connect(self.on_even_odd_changed)
        self._main_controller.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        default_value = 41
        self._ui.spinBox_amount.setValue(default_value)
        self._main_controller.change_amount(default_value)

    @pyqtSlot(int)
    def on_amount_changed(self, value):
        self._ui.spinBox_amount.setValue(value)

    @pyqtSlot(str)
    def on_even_odd_changed(self, value):
        self._ui.label_even_odd.setText(value)

    @pyqtSlot(bool)
    def on_enable_reset_changed(self, value):
        self._ui.pushButton_reset.setEnabled(value)
