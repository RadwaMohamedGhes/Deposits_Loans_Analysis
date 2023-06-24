from PyQt6 import QtCore, QtGui, QtWidgets


class UIGuide(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 618)
        Form.setMaximumSize(QtCore.QSize(1000, 100000))
        app_icon = QtGui.QIcon()
        app_icon.addPixmap(QtGui.QPixmap("images/guide.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(app_icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QtCore.QSize(600, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -572, 581, 1170))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scrollAreaWidgetContents_2.setFont(font)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_10 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Guide", "GUIDE"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#2c067d;\">WHAT IS THIS</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "This project is associated with ITI Intensive code Camp, Data Analysis Track."))
        self.label_9.setText(_translate("Form", "This project covers most of the steps that a data analyst need, \n"
                                        "Most of the technologies a data analyst needs to know are used."))
        self.label_10.setText(_translate("Form", "We have covered a lot during the project and those are just some of the steps:\n"
                                         "- Spent some time trying to understand the data, business requirements, and analysis scope.\n"
                                         "- Gained insights from the data to address questions stated on the business requirements:\n"
                                         "     - Used Python to address those questions.\n"
                                         "     - Used SQL Queries to gain insights.\n"
                                         "     - Developed Excel Dashboard to communicate those insights.\n\n"
                                         "- Built a Data warehouse for the business:\n"
                                         "     - Started by defining business processes.\n"
                                         "     - Followed the DWH Modeling steps to develop the Model (Schema).\n"
                                         "     - Implemented this model in Oracle database.\n"
                                         "     - Developed Python script to generate data into the DWH.\n"
                                         "     - Populated the data into the database.\n"
                                         "     - Used SQL Queries to gain insights from the DWH.\n"
                                         "     - Developed some recommendations based on the Analysis.\n\n"
                                         "- Built a Machine Learning model.\n"
                                         "     - The aim of the model is to help the Marketing team.\n"
                                         "     - We want to target clients who are most likely to use our services.\n"
                                         "     - We used 6 different classification models.\n"
                                         "     - We developed a Dynamic Approach for the preprocessing phase.\n"
                                         "     - We used our model to predict the outcome of the next Marketing Campaign."
                                         "\n\nWe have achieved a lot and gained tons of insights.\n"
                                         "Now is the time to communicate those insights\n"
                                         "- We developed 4 Power Bi Dashboards for 3 teams:\n"
                                         "     - Financial Team: To help maximize our revenue.\n"
                                         "     - Marketing Team: To help Maximize their performance.\n"
                                         "     - Customer Support Team: To help improve Customer Satisfaction.\n\n"
                                         "The last Dance\n"
                                         "- We have done a lot and everything is scattered.\n"
                                         "  Time to put it all together.\n"
                                         "- We built a Desktop Application to support our work.\n"
                                         "     - The App is the perfect outlet to show off what we have done.\n"))
