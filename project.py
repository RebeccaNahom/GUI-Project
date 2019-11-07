import os
import subprocess
import sys
import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QCheckBox, QTreeWidgetItemIterator
from PyQt5.QtCore import Qt, QThread
from GUI_project import Ui_MainWindow
from subprocess import Popen, PIPE, call

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(200, 200, 1000, 900)
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        self.initUI()

        self.checked = []
        self.process_id = []
        self.current_dir = ""


    def initUI(self):
        self.main.pushBtnSelect.clicked.connect(self.open_file)
        self.main.pushBtnRun.clicked.connect(self.run)
        self.main.pushBtnSelectAll.clicked.connect(self.select_all)
        self.main.pushBtnUnselectAll.clicked.connect(self.unselect_all)
        self.main.pushBtnRefreshLogs.clicked.connect(self.refresh_logs)
        self.main.pushBtnStop.clicked.connect(self.stop)


        self.setWindowTitle("Automation-Testing Run Environment ")
        QtWidgets.QTreeWidgetItem(self.main.treeWidget.setHeaderLabels(["Test Name:"]))


        self.main.pushBtnRun.toggle()
        self.main.pushBtnStop.toggle()
        self.main.pushBtnSelectAll.setEnabled(False)
        self.main.pushBtnUnselectAll.setEnabled(False)
        self.main.pushBtnStop.setEnabled(False)


    def open_file(self):
        try:
            test_files = QFileDialog.getOpenFileNames(self, directory="C:/RLN/Dev/ElevationBC/Projects/CRM_Project", filter="js(*test.js)")[0]
            # print(test_files)
            self.current_dir = os.path.dirname(test_files[0])
            # print(self.current_dir)
            for test in test_files:
                test_name = os.path.basename(test)
                cg = QtWidgets.QTreeWidgetItem(self.main.treeWidget, [test_name])
                cg.setCheckState(0, Qt.Unchecked)
                self.main.pushBtnSelectAll.setEnabled(True)
                # print(test_name)
            # print(test_files)
        except Exception as e:
            print('error in open_file: ' + str(e))


    # WORKS
    # def threads(self):
    #     for i in range(0, len(self.checked)):
    #         test_text = self.checked[i]
    #         process = subprocess.Popen(["node", self.current_dir + "/" + test_text], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
    #                                    shell=True, universal_newlines=True, start_new_session=False)
    #         # stderr, stdout = process.communicate()
    #         self.process.append({"id": process.pid})
    #         print(self.process)
    #         self.logs()
    # t = threading.Thread(target=self.threads)
    # t.start()


    def command_for_run(self):
        command = "node "
        # print(self.checked)
        for i in range(0, len(self.checked)):
            if i != 0:
                command += f"&& node {self.current_dir}/{self.checked[i]} "
            else:
                command += f"{self.current_dir}/{self.checked[i]} "
        # print(command)
        return command


    def find_checked(self):
        iterator = QTreeWidgetItemIterator(self.main.treeWidget)
        # print(iterator)
        while iterator.value():
            item = iterator.value()
            if item.checkState(0):
                self.checked.append(item.text(0))
            iterator += 1


    def run(self):
        try:
            self.find_checked()
            # print(self.checked)
            process = subprocess.Popen(self.command_for_run(), shell=True, universal_newlines=True, start_new_session=False)
            self.process_id.append({"id": process.pid})
            # print(self.process_id)
            self.main.pushBtnRun.setEnabled(False)
            if not self.main.pushBtnRun.isEnabled():
                self.main.pushBtnStop.setEnabled(True)
                self.main.treeWidget.setEnabled(False)
                self.main.pushBtnUnselectAll.setEnabled(False)
                self.main.pushBtnSelectAll.setEnabled(False)
        except Exception as e:
            print('error in run: ' + str(e))
        # print(self.checked)


    def select_all(self):
        iterator = QTreeWidgetItemIterator(self.main.treeWidget)
        while iterator.value():
            item = iterator.value()
            item.setCheckState(0, QtCore.Qt.Checked)
            iterator += 1
            self.main.pushBtnSelectAll.setEnabled(False)
            self.main.pushBtnUnselectAll.setEnabled(True)


    def unselect_all(self):
        iterator = QTreeWidgetItemIterator(self.main.treeWidget)
        while iterator.value():
            item = iterator.value()
            item.setCheckState(0, QtCore.Qt.Unchecked)
            iterator += 1
            self.main.pushBtnSelectAll.setEnabled(True)
            self.main.pushBtnUnselectAll.setEnabled(False)


    def refresh_logs(self):
        try:
            today_time = datetime.date.today()
            log_path = f'{self.current_dir}/log/{str(today_time)}-results.log'
            # print(log_path)
            f = open(log_path, "r")
            self.main.logText.setText(f.read())
        except Exception as e:
            print('error in refresh logs: ' + str(e))


    def stop(self):
        try:
            for p in self.process_id:
                pid = p["id"]
                subprocess.Popen("taskkill /F /T /PID %i" % pid, shell=True)
            self.main.pushBtnRun.setEnabled(True)
            self.main.treeWidget.setEnabled(True)
        except Exception as e:
            print('error in stop: ' + str(e))


def run():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())


run()

# convert to exe:
#pyinstaller -F -w project.py

#pyuic5 GUI_project.ui -o GUI_project.py
# PyInstaller --onefile -n gui --distpath project.py

