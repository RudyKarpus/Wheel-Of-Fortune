from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, Qt, QTime
from PySide2.QtGui import QFont
from PySide2.QtWidgets import (QLabel, QPushButton, QPlainTextEdit,
                               QTimeEdit, QDateTimeEdit)


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 81))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 180, 801, 141))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.answerTextEdit = QPlainTextEdit(Form)
        self.answerTextEdit.setObjectName(u"answerTextEdit")
        self.answerTextEdit.setGeometry(QRect(150, 510, 521, 51))
        font2 = QFont()
        font2.setPointSize(22)
        self.answerTextEdit.setFont(font2)
        self.answerButton = QPushButton(Form)
        self.answerButton.setObjectName(u"answerButton")
        self.answerButton.setGeometry(QRect(310, 430, 191, 51))
        self.answerButton.setFont(font1)
        self.label_instruction = QLabel(Form)
        self.label_instruction.setObjectName(u"label_instruction")
        self.label_instruction.setGeometry(QRect(10, 310, 791, 111))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_instruction.setFont(font3)
        self.label_instruction.setMidLineWidth(1)
        self.label_instruction.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_category = QLabel(Form)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(0, 130, 801, 41))
        font4 = QFont()
        font4.setPointSize(16)
        self.label_category.setFont(font4)
        self.label_category.setAlignment(Qt.AlignCenter)
        self.timeEdit = QTimeEdit(Form)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setEnabled(False)
        self.timeEdit.setGeometry(QRect(310, 70, 191, 31))
        font5 = QFont()
        font5.setFamily(u"Arial Black")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.timeEdit.setFont(font5)
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(False)
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setKeyboardTracking(True)
        self.timeEdit.setCurrentSection(QDateTimeEdit.SecondSection)
        self.timeEdit.setTime(QTime(0, 0, 5))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"Runda Fina\u0142owa !!!", None))
        self.label_2.setText("")
        self.answerTextEdit.setPlainText("")
        self.answerButton.setText(QCoreApplication.translate(
            "Form", u"Odpowied\u017a", None))
        self.label_instruction.setText("")
        self.label_category.setText("")
        self.timeEdit.setDisplayFormat(QCoreApplication.translate(
            "Form", u"s", None))
    # retranslateUi
