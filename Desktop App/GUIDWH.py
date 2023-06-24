from PyQt6 import QtCore, QtGui, QtWidgets


class UIDWH(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 618)
        Form.setMaximumSize(QtCore.QSize(1000, 100000))
        app_icon = QtGui.QIcon()
        app_icon.addPixmap(QtGui.QPixmap("images/dwh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(app_icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setEnabled(True)
        # self.scrollArea.setMinimumSize(QtCore.QSize(600, 600))
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
        Form.setWindowTitle(_translate("Guide", "Data WareHouse"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#2c067d;\">DATA WAREHOUSING</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "We have 3 main business processes:\n"
                                        "1-  Marketing Campaign (Marketing Team)\n"
                                        "2-  Transactions (Finance Team)\n"
                                        "3-  Customer Services: (Customer Support Team)\n\n\n"
                                        "We have decided to take the business to the next level\n"
                                        "Having a single source of truth."))
        self.label_9.setText(_translate("Form", '''MARKETING CAMPAIGN:
    - In this fact table we want to analyze the behavior of our clients who invest on term deposits or loans, and assess the marketing team performance, to maximize performance of our marketing campaigns.
                                        
TRANSACTIONS:
    - In this fact table we want to analyze any interaction or transaction made by or to any client.

* CUSTOMER SERVICES:
    - This fact table helps us keep track of customer satisfaction and provides ways to improve the company’s performance by responding to clients’ needs.
                                        '''))
        self.label_10.setText(_translate("Form", "For the last Data Warehousing Step\n"
                                         "We have developed bunch of SQL Queries to analyze the historical data\n"
                                         "Which lead us to some treasures\n\n"))
