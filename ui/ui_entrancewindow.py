from PySide2.QtCore import QCoreApplication, QMetaObject, QRect
from PySide2.QtGui import QFont

from PySide2.QtWidgets import QLabel, QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 551, 111))
        font = QFont()
        font.setFamily(u"Script MT Bold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 150, 712, 52))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.startButton = QPushButton(Form)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(0, 230, 801, 371))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(72)
        font2.setBold(True)
        font2.setWeight(75)
        self.startButton.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"Witaj w kole fortuny", None))
        self.label_2.setText(QCoreApplication.translate(
            "Form", u"Czy chcesz rozpocz\u0105\u0107 rozgrywke ?", None))
        self.startButton.setText(QCoreApplication.translate(
            "Form", u"tak", None))
