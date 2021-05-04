from PyQt5.QtWidgets import QFileDialog, QMessageBox
from os import chdir, listdir ,path
from pygame import mixer

file = open("path.txt", "r+")

mixer.init()


def list_file(listView):
    song_list = listdir()
    for i in song_list:
        pos = 0
        listView.insertItem(pos, i)
        pos += 1


def first_try_to_list(listView):
    try:
        chdir(file.readline())
    except Exception as e:
        directory = QFileDialog.getExistingDirectory()
        chdir(directory)
        listView.clear()
        list_file(listView)
        print(e)
        file.write(directory)
    list_file(listView)


def browse(listView):
    directory = QFileDialog.getExistingDirectory()
    chdir(directory)
    listView.clear()
    list_file(listView)

    file.write(directory)
    file.seek(0)
    file.truncate()
    file.write(directory)


def list_sel(listView):
    global item
    item = listView.currentItem()
    item = item.text()


def play_music(mainwindow):
    global paused

    if paused:
        mixer.music.unpause()

        paused = False
    else:
        try:
            stop_music()
            play_it = item
            mixer.music.load(play_it)
            mixer.music.play()

        except Exception as e:
            QMessageBox.critical(mainwindow, 'Error', 'not supported format')
            print(e)


def stop_music():
    mixer.music.stop()


paused = False


def pause_music():
    global paused
    paused = True
    mixer.music.pause()


mixer.music.set_volume(1)
