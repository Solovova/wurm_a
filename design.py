# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_ToDo = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_ToDo.setColumnCount(3)
        self.tableWidget_ToDo.setObjectName("tableWidget_ToDo")
        self.tableWidget_ToDo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ToDo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ToDo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ToDo.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget_ToDo, 7, 0, 1, 2)
        self.comboBox_Process = QtWidgets.QComboBox(self.tab)
        self.comboBox_Process.setObjectName("comboBox_Process")
        self.gridLayout_2.addWidget(self.comboBox_Process, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.tableWidget_Log = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_Log.setColumnCount(1)
        self.tableWidget_Log.setObjectName("tableWidget_Log")
        self.tableWidget_Log.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Log.setHorizontalHeaderItem(0, item)
        self.gridLayout_2.addWidget(self.tableWidget_Log, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.pushButton_Clear = QtWidgets.QPushButton(self.tab)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.gridLayout_2.addWidget(self.pushButton_Clear, 8, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_Save = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout_3.addWidget(self.pushButton_Save, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.pushButton_Load = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Load.setObjectName("pushButton_Load")
        self.gridLayout_3.addWidget(self.pushButton_Load, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 20, 291, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.testCV = QtWidgets.QPushButton(self.tab_4)
        self.testCV.setGeometry(QtCore.QRect(330, 20, 75, 23))
        self.testCV.setObjectName("testCV")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 231, 161))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solo"))
        item = self.tableWidget_ToDo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Задание"))
        item = self.tableWidget_ToDo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Действия"))
        item = self.tableWidget_ToDo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Данные"))
        self.label_6.setText(_translate("MainWindow", "СТОЮ"))
        item = self.tableWidget_Log.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Log"))
        self.label.setText(_translate("MainWindow", "Log:"))
        self.label_2.setText(_translate("MainWindow", "To do:"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Work"))
        self.label_3.setText(_translate("MainWindow", "Shifr+F1 : Старт/стоп процесс"))
        self.label_4.setText(_translate("MainWindow", "Shift+F2 : Старт/стоп процесс первый раз, запрашивает ключевые координаты"))
        self.label_5.setText(_translate("MainWindow", "Shift+F3 : Озвучивает состояние"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Help"))
        self.pushButton_Save.setText(_translate("MainWindow", "Save"))
        self.pushButton_Load.setText(_translate("MainWindow", "Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Config"))
        self.testCV.setText(_translate("MainWindow", "PushButton"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
