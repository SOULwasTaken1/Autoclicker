"""
https://github.com/SOULwasTaken1
Made by SOULisCOOL1
discord - SOUL#7093
"""

import sys
from tkinter import *
import time
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

import customtkinter
#=======================================
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
#=======================================

root = customtkinter.CTk()
root.geometry("500x300")
root.title("AutoClicker")
try:

    root.iconbitmap("autoclicker.ico")
except:
    print("image not found")

frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(pady=5,padx=10,fill="both",expand=True)


label=customtkinter.CTkLabel(frame2,text='\t\t𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦',font=('roboto',25))
label.grid(row=1,)

l1=customtkinter.CTkLabel(frame2,text="𝗧𝗢𝗚𝗚𝗟𝗘 𝗞𝗘𝗬",font=('roboto',20))
l1.grid(row=2,column=0)

e1=customtkinter.CTkButton(frame2,text="F6")
e1.grid(row=2,column=1,padx=(0,100),pady=10)

l2=customtkinter.CTkLabel(frame2,text="𝗖𝗟𝗢𝗦𝗘",font=('roboto',20))
l2.grid(row=3,column=0)

e2=customtkinter.CTkButton(frame2,text="NumLock")
e2.grid(row=3,column=1,padx=(0,100),pady=10)

l3=customtkinter.CTkLabel(frame2,text="𝗗𝗘𝗟𝗔𝗬",font=('roboto',20))
l3.grid(row=4,column=0)

entry=customtkinter.CTkEntry(frame2,placeholder_text="0.001")
entry.grid(row=4,column=1,padx=(0,100),pady=10)

l4=customtkinter.CTkLabel(frame2,text="𝗠𝗢𝗨𝗦𝗘 𝗕𝗨𝗧𝗧𝗢𝗡",font=('roboto',20))
l4.grid(row=5,column=0)

Option = customtkinter.CTkComboBox(frame2,values=["Left Click","Right Click"])
Option.grid(row=5,column=1,padx=(0,100),pady=10)


#  ======== settings ========
TOGGLE_KEY = Key.f6
END_KEY = Key.num_lock
#  ==========================


STOP = TOGGLE = False

def on_press(key):
    global STOP, TOGGLE
    if key == TOGGLE_KEY:
        if TOGGLE:
            TOGGLE = False
            print("[AutoClicker] Toggled AutoClicker - OFF")
        else:
            TOGGLE = True
            print("[AutoClicker] Toggled AutoClicker - ON")
    elif key == END_KEY:
        STOP = True
        print("[AutoClicker] Exiting")
        root.quit()


def start():
    try:
        DELAY = int(entry.get())
    except:
        DELAY = 0.0001
    button = Option.get()
    global MOUSE_BUTTON
    if button == "Left Click":
        MOUSE_BUTTON = Button.left
    elif button == "Right Click":
        MOUSE_BUTTON = Button.right

    listener = Listener(on_press=on_press)
    listener.start()
    mouse = Controller()

    while not STOP:
        if TOGGLE:
            mouse.press(MOUSE_BUTTON)
            mouse.release(MOUSE_BUTTON)
            time.sleep(DELAY)
    listener.stop()

button = customtkinter.CTkButton(root,text="START",command=start)
button.pack(pady=12,padx=(0,10))

root.mainloop()
