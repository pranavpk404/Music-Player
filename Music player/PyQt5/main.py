from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QLabel, QListWidget

import resource as brain


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        def play():
            brain.play_music(MainWindow)

        def pause():
            brain.pause_music()

        def stop():
            brain.stop_music()

        def find():
            brain.browse(self.listView)

        def list_clicked():
            brain.list_sel(self.listView)


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 519)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listView = QListWidget(self.centralwidget)
        self.listView.setGeometry(QRect(0, 0, 201, 521))
        self.listView.setObjectName("listView")
        self.listView.itemClicked.connect(list_clicked)

        self.play = QPushButton(self.centralwidget)
        self.play.setGeometry(QRect(240, 20, 101, 81))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.play.setFont(font)
        self.play.setAutoFillBackground(False)
        icon = QIcon()
        icon.addPixmap(QPixmap("res/play.png"), QIcon.Normal, QIcon.Off)
        self.play.setIcon(icon)
        self.play.setIconSize(QSize(50, 50))
        self.play.setFlat(True)
        self.play.setObjectName("play")
        self.play.clicked.connect(play)

        self.pause = QPushButton(self.centralwidget)
        self.pause.setGeometry(QRect(240, 120, 101, 81))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pause.setFont(font)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("res/pause.png"), QIcon.Normal, QIcon.Off)
        self.pause.setIcon(icon1)
        self.pause.setIconSize(QSize(50, 50))
        self.pause.setFlat(True)
        self.pause.setObjectName("pause")
        self.pause.clicked.connect(pause)

        self.stop = QPushButton(self.centralwidget)
        self.stop.setGeometry(QRect(240, 220, 101, 81))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.stop.setFont(font)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("res/stop.png"), QIcon.Normal, QIcon.Off)
        self.stop.setIcon(icon2)
        self.stop.setIconSize(QSize(50, 50))
        self.stop.setFlat(True)
        self.stop.setObjectName("stop")
        self.stop.clicked.connect(stop)

        self.change_dir = QPushButton(self.centralwidget)
        self.change_dir.setGeometry(QRect(240, 320, 141, 81))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.change_dir.setFont(font)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("res/find.png"), QIcon.Normal, QIcon.Off)
        self.change_dir.setIcon(icon3)
        self.change_dir.setIconSize(QSize(50, 50))
        self.change_dir.setDefault(False)
        self.change_dir.setFlat(True)
        self.change_dir.setObjectName("change_dir")
        self.change_dir.clicked.connect(find)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        brain.first_try_to_list(self.listView)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Box"))
        MainWindow.setWindowIcon(QIcon("res\\icon.ico"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.pause.setText(_translate("MainWindow", "Pause"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.change_dir.setText(_translate("MainWindow", "Change Folder"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
