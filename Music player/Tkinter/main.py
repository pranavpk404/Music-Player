import tkinter.ttk as ttk
from os import chdir, listdir, getcwd
from threading import Thread
from time import sleep
from tkinter import messagebox as mg, Tk, LEFT, BOTH, GROOVE, PhotoImage, StringVar, ACTIVE, Listbox, SINGLE, END
from tkinter.filedialog import askdirectory

from pygame import mixer
from ttkthemes import ThemedStyle

root = Tk()
style = ThemedStyle(root)

style.set_theme("equilux")
root.title('Music Box')
root.config(bg="black")
root.iconbitmap("res//icon.ico")
root.geometry('660x350')
cur_path = getcwd()


file = open("path.txt", "r+")

play_list = Listbox(root, bg='#424242', fg="white", selectmode=SINGLE, border=5)


def list_file():
    song_list = listdir()
    for i in song_list:
        pos = 0
        play_list.insert(pos, i)
        pos += 1


def browse():
    directory = askdirectory()
    chdir(directory)
    play_list.delete(0, END)
    list_file()
    file.write(directory)
    file.seek(0)
    file.truncate()
    file.write(directory)

try:
    chdir(file.readline())
except:
    directory = askdirectory()
    chdir(directory)
    play_list.delete(0, END)
    list_file()
    file.write(directory)
list_file()

mixer.init()

def show_details(play_song):
    a = mixer.Sound(play_song)
    total_length = a.get_length()
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total Length" + ' - ' + timeformat

    t1 = Thread(target=start_count, args=(total_length,))
    t1.setDaemon(True)
    t1.start()


def start_count(t):
    global paused
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Current Time" + ' - ' + timeformat
            sleep(1)
            current_time += 1


def play_music():
    global paused

    if paused:
        mixer.music.unpause()

        paused = False
    else:
        try:
            var.set(play_list.get(ACTIVE))
            stop_music()
            sleep(1)
            play_it = play_list.get(ACTIVE)
            mixer.music.load(play_it)
            mixer.music.play()

            show_details(play_it)
        except Exception as e:
            mg.showerror('File not found', 'File not found')
            print(e)


def stop_music():
    mixer.music.stop()


paused = False


def pause_music():
    global paused
    paused = True
    mixer.music.pause()


mixer.music.set_volume(1)

var = StringVar()

playPhoto = PhotoImage(file=cur_path + '\\res\\play.png')
playBtn = ttk.Button(root, image=playPhoto, command=play_music)

stopPhoto = PhotoImage(file=cur_path + '\\res\\stop.png')
stopBtn = ttk.Button(root, image=stopPhoto, command=stop_music)

pausePhoto = PhotoImage(file=cur_path + '\\res\\pause.png')
pauseBtn = ttk.Button(root, image=pausePhoto, command=pause_music)

AddPhoto = PhotoImage(file=cur_path + '\\res\\find.png')
AddBtn = ttk.Button(root, image=AddPhoto, command=browse)

song_title = ttk.Label(root, font='Helvetica 12 bold', textvariable=var)

lengthlabel = ttk.Label(root, text='Total Length : --:--')

currenttimelabel = ttk.Label(root, text='Current Time : --:--', relief=GROOVE)

currenttimelabel.pack()
lengthlabel.pack(pady=5)
play_list.pack(fill=BOTH)
song_title.pack(fill=BOTH)
playBtn.pack(side=LEFT, padx=40)
stopBtn.pack(side=LEFT, padx=40)
pauseBtn.pack(side=LEFT, padx=40)
AddBtn.pack(side=LEFT, padx=40)

root.mainloop()
