from PyQt6 import QtCore, QtGui, QtWidgets


class UIDefinition(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 618)
        Form.setMaximumSize(QtCore.QSize(1000, 100000))
        app_icon = QtGui.QIcon()
        app_icon.addPixmap(QtGui.QPixmap("images/define.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(app_icon)
        self.verticalLayout = QtWidgets.QGridLayout(Form)
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
        Form.setWindowTitle(_translate("Guide", "Data Definition"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#2c067d;\">BANKING SYSTEM</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "- We have 31,647 rows & 18 Columns.\n- The data does not have NULLS, but it has missing values.\n"
                                        "- IDs are unique and Age ranges from 18 to 95 with a mean value of 40.\n"
                                        "- We have 11 different Jobs and 206 missing jobs.\n"
                                        "- We have (Married, Single, and Divorced) clients.\n"
                                        "- We have Primary, Secondary, and College education\n"
                                                "  with 1314 missing values.\n"
                                        "- The default column is a perfect Yes | No column.\n"))
        self.label_9.setText(_translate("Form", "- The balance column ranges from -8k to 102k"
                                        " with a mean value of 1360,\n  and after"
                                        "a deep investigation it appears that negative values are normal here.\n"
                                        "- Housing & Loan are perfect Yes | No Columns.\n"
                                        "- Contact column has two values (Cellular and telephone)\n  with 9k missing values.\n"
                                        "- Day & Month columns are perfect 31 | 12 columns\n"))
        self.label_10.setText(_translate("Form", "- The duration column ranges from 0 to 4920 seconds\n  with a mean value of 4minutes.\n"
                                         "- Campaign column ranges from 1 to 63.\n"
                                         "- P days column have 25924 values of -1.\n"
                                         "- Previous column ranges from 0 to 275 with 25924 zeros.\n"
                                         "- P outcome column has 27k missing values.\n"
                                         "- Subscribed column is a perfect Yes | No column.\n"))
