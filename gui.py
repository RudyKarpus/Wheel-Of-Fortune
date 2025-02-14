from PySide2.QtWidgets import QApplication, QWidget, QStackedLayout, QFrame
from PySide2.QtWidgets import QVBoxLayout
from screens import EntranceScreen, LogInScreen, RoundScreen, FinalRoundScreen
from screens import FinalScreen
from model import Presenter
import sys


class MainWindow(QWidget):
    def __init__(self, presenter: Presenter, parent=None):
        super(MainWindow, self).__init__(parent)
        presenter.mainwindow = self
        self.presenter = presenter
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(EntranceScreen(self.presenter))
        self.stackedLayout.addWidget(LogInScreen(self.presenter))
        self.stackedLayout.addWidget(RoundScreen(self.presenter))
        self.stackedLayout.addWidget(FinalRoundScreen(self.presenter))
        self.stackedLayout.addWidget(FinalScreen(self.presenter))
        self.frame = QFrame()

        self.frame.setLayout(self.stackedLayout)
        layout = QVBoxLayout(self)
        layout.addWidget(self.frame)

    def next_layout(self):
        self.stackedLayout.setCurrentIndex(self.presenter.layoutstackholder+1)
        self.presenter.nextlayout()


def guiMain(args):
    app = QApplication(args)
    presenter = Presenter()
    window = MainWindow(presenter)
    window.resize(800, 600)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
