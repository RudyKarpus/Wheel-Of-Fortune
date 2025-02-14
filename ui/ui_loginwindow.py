from PySide2.QtCore import QCoreApplication, QMetaObject, QRect
from PySide2.QtGui import QFont

from PySide2.QtWidgets import QLabel, QPushButton, QPlainTextEdit


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 719, 68))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.addButton = QPushButton(Form)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(100, 210, 121, 51))
        font1 = QFont()
        font1.setPointSize(16)
        self.addButton.setFont(font1)
        self.addPlayerTextEdit = QPlainTextEdit(Form)
        self.addPlayerTextEdit.setObjectName(u"addPlayerTextEdit")
        self.addPlayerTextEdit.setGeometry(QRect(100, 110, 571, 81))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(34)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.addPlayerTextEdit.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"Wprowad\u017a imi\u0119 gracza nr. 1", None))
        self.addButton.setText(QCoreApplication.translate(
            "Form", u"Dodaj", None))
        self.addPlayerTextEdit.setPlainText(QCoreApplication.translate(
            "Form", u"...", None))
    # retranslateUi
