import pyglet
import glob
from Tkinter import *
from pyglet.window import key
from pyglet.window import Window
from threading import Thread
from psycopg2._psycopg import Column
#from PIL.ImageOps import expand


songs=glob.glob("*.mp3")
player=pyglet.media.Player()

_volume = 1.0
_min_distance = 1.0
_max_distance = 100000000

def set_min_distance(in_distance):
        '''See `Player.min_distance`.'''
        pass

def set_max_distance(max_distance):
    '''See `Player.max_distance`.'''
    pass



def play_song(event=False):
    global player
    for i in range(len(songs)):
        source=pyglet.resource.media(songs[i])
        player.queue(source)
    player.play()
    
def pause_song(event=False):
    player.pause()

def next_song(event=False):
    player.next()

def stop_song(event=False):
	player.delete()

def seek_forward_song(event=False):
    if player.playing:
        curr_time=player.time
        curr_time=curr_time+10
        player.seek(curr_time)

def seek_backward_song(event=False):
    if player.playing:
        curr_time=player.time
        curr_time=curr_time - 10
        player.seek(curr_time)        


#def mute(event):
#    player.mute()

window=Tk()
var = DoubleVar()
w = Scale(window, from_ = 0 , to = 100 ,bd =3)
w.set(30)
w.grid(row=2,column = 3)
label = Label(window, text =  "     VOLUME")
label.grid(row=3, column=3)


window.bind("<Up>",  play_song)
play_=Button(text="play", width=10,command=play_song, activebackground='white', activeforeground='red')
play_.grid(row=1, column=1)

window.bind("<Down>",  pause_song)
pause_=Button(text="Pause", width=10, command=pause_song,activebackground='white',activeforeground='red')
pause_.grid(row=1, column=2)

window.bind("<Tab>",  next_song)
next_=Button(text="next", width=10, command=next_song,activebackground='white',activeforeground='red')
next_.grid(row=1, column=3)

window.bind("<Right>",  seek_forward_song)
seek_=Button(text="forward", width=10, command=seek_forward_song,activebackground='white',activeforeground='red')
seek_.grid(row=1, column=4)

window.bind("<Left>",  seek_backward_song)
seek_=Button(text="backward", width=10, command=seek_backward_song,activebackground='white',activeforeground='red')
seek_.grid(row=1, column=5)

window.bind("<Escape>",  stop_song)
stop_=Button(text="stop", width=10, command=stop_song,activebackground='white',activeforeground='red')
stop_.grid(row=1, column=6)


#stop_=Button(text="mute", width=5, command=mute,activebackground='white',activeforeground='red')
#stop_.grid(row=1, column=7)

#pyglet.app.run()
window.mainloop()