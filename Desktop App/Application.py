import json
from sys import argv, exit
from pyperclip import copy
from PyQt6 import QtWidgets, QtGui
from GUIMain import Ui_Project
from GUIDashboard import UI_Dashboard
import subprocess
import MachineLearning as ML
import pandas as pd
import webbrowser
from GUIDefinition import UIDefinition
from GUIGuide import UIGuide
from GUIDWH import UIDWH
from GUISchema import UISchema


class App:
    def __init__(self):
        # The GUI App
        self.app = QtWidgets.QApplication(argv)
        # GUI Main window
        self.Application = QtWidgets.QMainWindow()
        self.ui = Ui_Project()
        self.ui.setupUi(self.Application)
        # get the configuration parameters
        conf = open('Configs.json', 'r')
        self.parameters = json.load(conf)
        # Set up the insights window
        self.ui_dashboard = QtWidgets.QWidget()
        # Set up the data definition window
        self.ui_definition = QtWidgets.QWidget()
        # Set up the data DWH window
        self.ui_dwh = QtWidgets.QWidget()
        self.ui_schema = QtWidgets.QWidget()
        # Set up the data definition window
        self.ui_guide = QtWidgets.QWidget()
        # Connect buttons with behaviour
        self.connect()
        # Show the GUI
        self.show()

    def show(self):
        self.Application.show()
        exit(self.app.exec())

    def connect(self):
        # Each menu item copies its value
        self.ui.yahoo.triggered.connect(
            lambda: copy('alghaly_m@yahoo.com')
        )
        self.ui.alghaly.triggered.connect(
            lambda: copy('alghaly')
        )
        self.ui.phon_number.triggered.connect(
            lambda: copy('+201002929690')
        )
        self.ui.telegram.triggered.connect(
            lambda: copy('al_ghay')
        )
        self.ui.al_ghaly.triggered.connect(
            lambda: copy('al_ghay')
        )
        self.ui.docs.clicked.connect(
            self.open_docs
        )
        self.ui.predict.clicked.connect(
            self.predict
        )
        self.ui.dashboard.clicked.connect(
            self.pbi
        )
        self.ui.define.clicked.connect(
            self.data_definition
        )
        self.ui.insights.clicked.connect(
            self.insights
        )
        self.ui.dwh.clicked.connect(
            self.dwh
        )
        self.ui.guide.triggered.connect(
            self.guide
        )

    def open_docs(self):
        try:
            path = self.parameters["docs_path"]
            subprocess.Popen([path], shell=True)
        except:
            self.error()

    def predict(self):
        try:
            test = self.parameters['ml_test']
            data = pd.read_csv(test)
            labels = ML.predict(data)
            data['subscribed'] = labels
            data.to_csv('predictions.csv')
        except:
            self.error()

    def pbi(self):
        try:
            link = self.parameters['dashboard']
            chrome_path = self.parameters['chrome_path']
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    chrome_path))
            webbrowser.get('chrome').open(link)
        except:
            self.error()

    def data_definition(self):
        self.ui_definition = QtWidgets.QWidget()
        definition = UIDefinition()
        definition.setupUi(self.ui_definition)
        self.ui_definition.show()

    def insights(self):
        self.ui_dashboard = QtWidgets.QWidget()
        insights = UI_Dashboard()
        insights.setupUi(self.ui_dashboard)
        x, y, w, h = self.Application.geometry().getRect()
        self.ui_dashboard.setGeometry(x - 243, y + 50, 1222, 675)
        self.ui_dashboard.show()

    def dwh(self):
        self.ui_schema = QtWidgets.QWidget()
        self.ui_dwh = QtWidgets.QWidget()
        dwh = UIDWH()
        schema = UISchema()
        dwh.setupUi(self.ui_dwh)
        schema.setupUi(self.ui_schema)
        self.ui_dwh.show()
        self.ui_schema.move(50, 150)  # Set the window position
        self.ui_schema.show()

    def guide(self):
        self.ui_guide = QtWidgets.QWidget()
        guide = UIGuide()
        guide.setupUi(self.ui_guide)
        self.ui_guide.show()

    @staticmethod
    def error():
        try:
            error_message = QtWidgets.QMessageBox()
            error_message.setWindowIcon(QtGui.QIcon('images/error.png'))
            error_message.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error_message.setText("An error has occurred.")
            error_message.setInformativeText("Please try again or contact administrator.")
            error_message.setWindowTitle("Error")
            error_message.show()
            error_message.exec()
        except:
            pass


GUI = App()
