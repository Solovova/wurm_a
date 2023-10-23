import time
from PyQt5.QtCore import QThread, pyqtSignal
from config import Config
from engine import Engine


# TreadWorker
# потоковый процесс, всегда читает log и делает подготовку данных для Engine
# Config
# читает и записывает данные в ini файл

class TreadWorker(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, window):
        QThread.__init__(self)
        self._is_running = True
        self._is_active = False
        self.window = window

        self.config = Config()
        self.logfile = open(self.config.nameLog, "r")
        self.logfile.seek(0, 2)

        self.engine = Engine(self.config)

    def run(self):
        while self._is_running:
            row = self.logfile.readline()
            while row:
                self.signal.emit(['AddLog', row])
                self.engine.log.append(row)
                row = self.logfile.readline()

            if self._is_active:
                res = self.engine.run()
                for rowres in res:
                    self.signal.emit(rowres)
            time.sleep(0.05)

        self.logfile.close()

    def stop(self):
        self._is_running = False

    def set_active(self, activate):
        if not self._is_active and activate:  # запуск
            self.config.activeOperation = self.window.comboBox_Process.currentIndex()
            self.engine.load(self.config.operationsToDo[self.config.activeOperation],
                             self.config.operationsPoint[self.config.activeOperation])
        elif self._is_active and not activate:  # остановка
            self.engine.reset()

        self._is_active = activate
        self.signal.emit(['ChangeActive'])

    def is_active(self):
        return self._is_active

    def get_coordinates(self):
        self.config.activeOperation = self.window.comboBox_Process.currentIndex()
        self.config.getCoordinates()
