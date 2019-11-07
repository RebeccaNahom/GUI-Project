# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 823)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushBtnSelect = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtnSelect.setGeometry(QtCore.QRect(20, 710, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBtnSelect.setFont(font)
        self.pushBtnSelect.setToolTip("")
        self.pushBtnSelect.setStyleSheet("border-style: solid;\n"
"border-radius: 7px;\n"
"font: 16pt \"Ink Free\";\n"
"color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:2px;")
        self.pushBtnSelect.setObjectName("pushBtnSelect")
        self.pushBtnRun = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtnRun.setGeometry(QtCore.QRect(230, 710, 161, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushBtnRun.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(34)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBtnRun.setFont(font)
        self.pushBtnRun.setToolTip("")
        self.pushBtnRun.setStyleSheet("border-style: solid;\n"
"background-color: rgb(0, 255, 0);\n"
"color:\"[enabled=\\\"true\\\"]\"\"{ color: grey }\"\"[enabled=\\\"false\\\"]\"\"{ color: black }\";\n"
"border-radius: 7px;\n"
"font: 34pt \"Ink Free\";\n"
"border-width:2px;\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushBtnRun.setObjectName("pushBtnRun")
        self.pushBtnRefreshLogs = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtnRefreshLogs.setGeometry(QtCore.QRect(720, 700, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBtnRefreshLogs.setFont(font)
        self.pushBtnRefreshLogs.setToolTip("")
        self.pushBtnRefreshLogs.setStyleSheet("border-style: solid;\n"
"border-radius: 7px;\n"
"font: 16pt \"Ink Free\";\n"
"color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:2px;")
        self.pushBtnRefreshLogs.setObjectName("pushBtnRefreshLogs")
        self.pushBtnStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtnStop.setGeometry(QtCore.QRect(410, 710, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(34)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBtnStop.setFont(font)
        self.pushBtnStop.setToolTip("")
        self.pushBtnStop.setStatusTip("")
        self.pushBtnStop.setStyleSheet("border-style: solid;\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;\n"
"font: 34pt \"Ink Free\";\n"
"border-width:2px;\n"
"color:\"[enabled=\\\"true\\\"]\"\"{ background-color: rgb(255, 0, 0) }\"\"[enabled=\\\"false\\\"]\"\"{ background-color: rgb(255, 215, 224) }\";\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushBtnStop.setObjectName("pushBtnStop")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 140, 171, 531))
        self.treeWidget.setStyleSheet("border-style: solid;\n"
"border-radius: 4px;\n"
"border-width:2px;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 8pt \"Ink Free\";")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(True)
        self.pushBtnSelectAll = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtnSelectAll.setGeometry(QtCore.QRect(10, 610, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBtnSelectAll.setFont(font)
        self.pushBtnSelectAll.setStyleSheet("border-style: solid;\n"
"border-radius: 7px;\n"
"font: 12pt \"Ink Free\";\n"
"border-color: rgb(0, 0, 255);\n"
"border-width:2px;\n"
"color: rgb(0, 0, 0);\n"
"color:\"[enabled=\\\"true\\\"]\"\"{ color: gray }\"\"[enabled=\\\"false\\\"]\"\"{ color: black }\"")
        self.pushBtnSelectAll.setObjectName("pushBtnSelectAll")
        self.pushBtnUnselectAll = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtnUnselectAll.setGeometry(QtCore.QRect(10, 640, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushBtnUnselectAll.setFont(font)
        self.pushBtnUnselectAll.setStyleSheet("border-style: solid;\n"
"border-radius: 7px;\n"
"font: 12pt \"Ink Free\";\n"
"border-color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:2px;\n"
"background-color:\"[enabled=\\\"false\\\"]\"\"{ color: gray }\"\"[enabled=\\\"true\\\"]\"\"{ color: black }\"")
        self.pushBtnUnselectAll.setObjectName("pushBtnUnselectAll")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 40, 511, 81))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(49)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.logText = QtWidgets.QTextEdit(self.centralwidget)
        self.logText.setGeometry(QtCore.QRect(220, 140, 661, 531))
        self.logText.setStyleSheet("border-style: solid;\n"
"font: 10pt \"Nirmala UI Semilight\";\n"
"border-radius: 4px;\n"
"border-width:2px;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.logText.setObjectName("logText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushBtnSelect.setStatusTip(_translate("MainWindow", "Open Test Files"))
        self.pushBtnSelect.setText(_translate("MainWindow", "Select Tests"))
        self.pushBtnRun.setStatusTip(_translate("MainWindow", "Run Selected Tests"))
        self.pushBtnRun.setText(_translate("MainWindow", "Run"))
        self.pushBtnRefreshLogs.setStatusTip(_translate("MainWindow", "Upload Test-Logs"))
        self.pushBtnRefreshLogs.setText(_translate("MainWindow", "Refresh Logs"))
        self.pushBtnStop.setText(_translate("MainWindow", "Stop"))
        self.pushBtnSelectAll.setText(_translate("MainWindow", "Select All"))
        self.pushBtnUnselectAll.setText(_translate("MainWindow", "Unselect All"))
        self.label.setText(_translate("MainWindow", "Test-Runner"))
