import sys
import winsound
from PyQt5 import QtWidgets
from PIL import ImageGrab
import keyboard
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui
from design import Ui_MainWindow
from TreadWorker import TreadWorker


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget_ToDo.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_Log.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_ToDo.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_ToDo.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_ToDo.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Log.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.initThreads()
        self.pushButton_Clear.clicked.connect(self.click_clear)
        self.pushButton_Save.clicked.connect(self.click_save)
        self.pushButton_Load.clicked.connect(self.click_load)
        self.testCV.clicked.connect(self.clickTestCV)

    def initThreads(self):
        self.treadWorker = TreadWorker(self)
        self.treadWorker.signal.connect(self.signal_tread_worker)
        self.treadWorker.start()
        self.comboBox_Process.addItems(self.treadWorker.config.operations)
        if getattr(self.treadWorker.config, 'activeOperation', -1) != -1:
            self.comboBox_Process.setCurrentIndex(self.treadWorker.config.activeOperation)

        self.comboBox_Char.addItems(self.treadWorker.config.characters)
        if getattr(self.treadWorker.config, 'activeCharacter', -1) != -1:
            self.comboBox_Char.setCurrentIndex(self.treadWorker.config.activeCharacter)

    def clickTestCV(self):
        tx1 = self.treadWorker.config.pointHelth_tx1
        ty1 = self.treadWorker.config.pointHelth_ty1
        tx2 = self.treadWorker.config.pointHelth_tx2
        ty2 = self.treadWorker.config.pointHelth_ty2

        im = ImageGrab.grab(bbox=(tx1, ty1, tx2, ty2))

        green = 0
        for x in range(tx1, tx2):
            rgb = im.getpixel((x - tx1, 1))
            if rgb[1] > 100:
                green = green + 1
            print(rgb[0], rgb[1], rgb[2])

        # img1.save("ttt.jpg")
        qim = ImageQt(im)
        pix = QtGui.QPixmap.fromImage(qim)
        self.label_7.setPixmap(pix)

        self.textEdit_2.setPlainText(str(green / (tx2 - tx1) * 100))

    def click_load(self):
        self.treadWorker.config.save()
        text = open('config.ini').read()
        self.textEdit.setPlainText(text)

    def click_save(self):
        if self.textEdit.toPlainText() == '':
            return
        with open('config.ini', 'w') as yourFile:
            yourFile.write(str(self.textEdit.toPlainText()))
        self.treadWorker.reloadConfig()

    def click_clear(self):
        self.tableWidget_Log.setRowCount(0)
        self.tableWidget_ToDo.setRowCount(0)

    def change_active(self) -> None:
        self.comboBox_Process.setDisabled(self.treadWorker.is_active())
        self.pushButton_Save.setDisabled(self.treadWorker.is_active())
        self.pushButton_Load.setDisabled(self.treadWorker.is_active())
        if self.treadWorker.is_active():
            self.label_6.setText('РАБОТАЮ')
        else:
            self.label_6.setText('СТОЮ')
            winsound.Beep(300, 200)

    def signal_tread_worker(self, data) -> None:
        if data[0] == 'AddToDo':
            self.add_to_do(data)
        elif data[0] == 'AddLog':
            self.AddLog(data[1])
        elif data[0] == 'ChangeActive':
            self.changeActive()
        elif data[0] == 'Stop':
            self.treadWorker.set_active(False)

    def add_to_do(self, data):
        self.tableWidget_ToDo.insertRow(0)
        for i in range(3):
            if type(data[i + 1]) == type([]):
                cell = ''.join(data[i + 1])
            else:
                cell = data[i + 1]
            self.tableWidget_ToDo.setItem(0, i, QtWidgets.QTableWidgetItem(cell))

    def AddLog(self, text):
        self.tableWidget_Log.insertRow(0)
        self.tableWidget_Log.setItem(0, 0, QtWidgets.QTableWidgetItem(text))


def hetKeySF1(treadWorker):
    treadWorker.set_active(not treadWorker._isActive)


def hetKeySF2(treadWorker):
    if treadWorker.is_active():
        return
    treadWorker.get_coordinates()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()

    keyboard.add_hotkey('shift+F1', hetKeySF1, args=(window.treadWorker,), suppress=True, trigger_on_release=True)
    keyboard.add_hotkey('shift+F2', hetKeySF2, args=(window.treadWorker,), suppress=True, trigger_on_release=True)

    window.show()
    app.exec_()

    window.treadWorker.config.save()
    window.treadWorker.stop()

    keyboard.clear_all_hotkeys()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
