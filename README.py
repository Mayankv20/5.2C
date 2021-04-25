from tkinter import *

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(15, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def YELLOW():
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)

def GREEN():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

def ORANGE():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="YELLOW", variable=var, value=1,
                 command=YELLOW)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="GREEN", variable=var, value=2,
                 command=GREEN)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="ORANGE", variable=var, value=3,
                 command=ORANGE)
R3.pack(anchor=W)

label = Label(root)
label.pack()
root.mainloop()
