from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QMainWindow
from os import chdir, listdir
from pygame import mixer

from ui import Ui_MainWindow

file = open("path.txt", "r+")

mixer.init()

paused = False


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.first_try_to_list()
        self.play.clicked.connect(self.play_music)
        self.pause.clicked.connect(self.pause_music)
        self.stop.clicked.connect(self.stop_music)
        self.change_dir.clicked.connect(self.browse)
        self.listWidget.clicked.connect(self.list_sel)
        # self.horizontalSlider(self.change_volume)

        self.show()

    def list_file(self):
        song_list = listdir()
        for i in song_list:
            pos = 0
            self.listWidget.insertItem(pos, i)
            pos += 1

    def first_try_to_list(self):
        try:
            chdir(file.readline())
        except Exception as e:
            directory = QFileDialog.getExistingDirectory()
            chdir(directory)
            self.listWidget.clear()
            self.list_file()
            print(e)
            file.write(directory)
        self.list_file()

    def browse(self):
        directory = QFileDialog.getExistingDirectory()
        chdir(directory)
        self.listWidget.clear()
        self.list_file()

        file.write(directory)
        file.seek(0)
        file.truncate()
        file.write(directory)

    def list_sel(self):
        global item
        item = self.listWidget.currentItem()
        item = item.text()

    def play_music(self):
        global paused

        if paused:
            mixer.music.unpause()
            paused = False

        else:
            try:
                self.stop_music()
                play_it = item
                mixer.music.load(play_it)
                mixer.music.play()

            except Exception as e:
                QMessageBox.critical(self.centralwidget,'Error', 'not supported format')
                print(e)

    @staticmethod
    def stop_music():
        mixer.music.stop()

    @staticmethod
    def pause_music():
        global paused
        paused = True
        mixer.music.pause()

    mixer.music.set_volume(1)

    def change_volume(self):
        p = self.horizontalSlider.pos()
        print(p)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
