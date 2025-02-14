
from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLabel


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 9, 801, 51))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_player_name_1 = QLabel(Form)
        self.label_player_name_1.setObjectName(u"label_player_name_1")
        self.label_player_name_1.setGeometry(QRect(10, 80, 281, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_player_name_1.setFont(font1)
        self.label_player_name_1.setAlignment(Qt.AlignCenter)
        self.label_player_name_2 = QLabel(Form)
        self.label_player_name_2.setObjectName(u"label_player_name_2")
        self.label_player_name_2.setGeometry(QRect(280, 80, 261, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_player_name_2.setFont(font2)
        self.label_player_name_2.setAlignment(Qt.AlignCenter)
        self.label_player_name_3 = QLabel(Form)
        self.label_player_name_3.setObjectName(u"label_player_name_3")
        self.label_player_name_3.setGeometry(QRect(560, 80, 231, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        self.label_player_name_3.setFont(font3)
        self.label_player_name_3.setAlignment(Qt.AlignCenter)
        self.label_player_points_1 = QLabel(Form)
        self.label_player_points_1.setObjectName(u"label_player_points_1")
        self.label_player_points_1.setGeometry(QRect(10, 120, 281, 41))
        self.label_player_points_1.setFont(font3)
        self.label_player_points_1.setAlignment(Qt.AlignCenter)
        self.label_player_points_2 = QLabel(Form)
        self.label_player_points_2.setObjectName(u"label_player_points_2")
        self.label_player_points_2.setGeometry(QRect(260, 120, 301, 41))
        self.label_player_points_2.setFont(font3)
        self.label_player_points_2.setAlignment(Qt.AlignCenter)
        self.label_player_points_3 = QLabel(Form)
        self.label_player_points_3.setObjectName(u"label_player_points_3")
        self.label_player_points_3.setGeometry(QRect(560, 120, 231, 41))
        self.label_player_points_3.setFont(font3)
        self.label_player_points_3.setAlignment(Qt.AlignCenter)
        self.label_player_rewards_1 = QLabel(Form)
        self.label_player_rewards_1.setObjectName(u"label_player_rewards_1")
        self.label_player_rewards_1.setGeometry(QRect(10, 180, 221, 411))
        self.label_player_rewards_1.setFont(font1)
        self.label_player_rewards_1.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_player_rewards_2 = QLabel(Form)
        self.label_player_rewards_2.setObjectName(u"label_player_rewards_2")
        self.label_player_rewards_2.setGeometry(QRect(300, 170, 211, 431))
        self.label_player_rewards_2.setFont(font3)
        self.label_player_rewards_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_player_rewards_3 = QLabel(Form)
        self.label_player_rewards_3.setObjectName(u"label_player_rewards_3")
        self.label_player_rewards_3.setGeometry(QRect(540, 170, 251, 431))
        self.label_player_rewards_3.setFont(font3)
        self.label_player_rewards_3.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"Podsumowanie", None))
        self.label_player_name_1.setText("")
        self.label_player_name_2.setText("")
        self.label_player_name_3.setText("")
        self.label_player_points_1.setText("")
        self.label_player_points_2.setText("")
        self.label_player_points_3.setText("")
        self.label_player_rewards_1.setText("")
        self.label_player_rewards_2.setText("")
        self.label_player_rewards_3.setText("")
    # retranslateUi
