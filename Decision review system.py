"""Radheya
   IMAGES ARE CURRENTLY BETA VERSION"""
import tkinter
import os
import PIL.Image
import PIL.ImageTk
import cv2
from functools import partial
import threading
import imutils
import time
from tkinter import filedialog
from tkinter import *

SET_WIDTH = 960
SET_HEIGHT = 510
stream = cv2.VideoCapture("THE CONJURING 3 Official Hindi Trailer (2021) _ Horror Movie.mp4")
flag = True
def play(speed):
    global flag
    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=[("Video file","*.mp4")])
    os.chdir("C:/Users/Lenovo/Downloads")
    stream = cv2.VideoCapture("clip.mp4")
def quit():
    exit()


def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("Decision _pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1.5)

    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("SPONSOR.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'out':
        decisionImg = "out.png"

    if decision == 'six':
        decisionImg = "SIX.png"

    if decision == 'four':
        decisionImg = "FOUR.png"

    if decision == 'not_out':
        decisionImg = "not_out.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=('out',))
    thread.daemon = 1
    thread.start()


def six():
    thread = threading.Thread(target=pending, args=('six',))
    thread.daemon = 1
    thread.start()


def four():
    thread = threading.Thread(target=pending, args=('four',))
    thread.daemon = 1
    thread.start()


def not_out():
    thread = threading.Thread(target=pending, args=('not_out',))
    thread.daemon = 1
    thread.start()


def exit():
    thread = threading.Thread(target=quit)
    thread.daemon = 1
    thread.start()


window = tkinter.Tk()
window.title("DRS - Decision Review System")
cv_image = cv2.cvtColor(cv2.imread("Welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()
btn = tkinter.Button(window, text="video", width=50, command=browseFiles)
btn.pack()
btn = tkinter.Button(window, text="<<Previous (Fast)", width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<<Previous (Slow) ", width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text="Next (Fast)>>", width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text="Next (Slow)>>", width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()
btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()
btn = tkinter.Button(window, text="Give Six", width=50, command=six)
btn.pack()
btn = tkinter.Button(window, text="Give Four", width=50, command=four)
btn.pack()
btn = tkinter.Button(window, text="Quit (Exit)", width=50, command=quit)
btn.pack()
window.mainloop()