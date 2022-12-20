#import Panel
import sys
from tkinter import *
import time
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
import customtkinter

customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.geometry("500x300")
root.title("AutoClicker")
try:

    root.iconbitmap("autoclicker.ico") #bitmap icon for the GUI
except:
    print("image not found") #have the bitmap image as .ico in the same folder as the script

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=5,padx=10,fill="both",expand=True)


label=customtkinter.CTkLabel(frame,text='\t\t𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦',font=('roboto',25)) #settings title
label.grid(row=1,)

l1=customtkinter.CTkLabel(frame,text="𝗧𝗢𝗚𝗚𝗟𝗘 𝗞𝗘𝗬",font=('roboto',20)) #label for the toggle button
l1.grid(row=2,column=0)

e1=customtkinter.CTkButton(frame,text="F6") #toggle button (doesnt work)
e1.grid(row=2,column=1,padx=(0,100),pady=10)

l2=customtkinter.CTkLabel(frame,text="𝗖𝗟𝗢𝗦𝗘",font=('roboto',20)) #label for the exit button
l2.grid(row=3,column=0)

e2=customtkinter.CTkButton(frame,text="NumLock") #exit button (doesnt work)
e2.grid(row=3,column=1,padx=(0,100),pady=10)

l3=customtkinter.CTkLabel(frame,text="𝗗𝗘𝗟𝗔𝗬",font=('roboto',20)) #label for delay Entry
l3.grid(row=4,column=0)

entry=customtkinter.CTkEntry(frame,placeholder_text="0.001") #delay (in seconds)
entry.grid(row=4,column=1,padx=(0,100),pady=10)

l4=customtkinter.CTkLabel(frame,text="𝗠𝗢𝗨𝗦𝗘 𝗕𝗨𝗧𝗧𝗢𝗡",font=('roboto',20)) #label for the click mode changer
l4.grid(row=5,column=0)

Option = customtkinter.CTkComboBox(frame,values=["Left Click","Right Click"])  #click mode changer
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
        DELAY = int(entry.get()) #gets the amount of delay (in sec) you put in the GUI
    except:
        DELAY = 0.0001 #default delay if you dont put any amount
    button = Option.get()
    global MOUSE_BUTTON
    try:
        if button == "Left Click":
            MOUSE_BUTTON = Button.left
        elif button == "Right Click":
            MOUSE_BUTTON = Button.right
    except:
        MOUSE_BUTTON = Button.left #just incase the user deletes the texts in the option menu
    listener = Listener(on_press=on_press)
    listener.start()
    mouse = Controller()

    while not STOP:
        if TOGGLE:
            mouse.press(MOUSE_BUTTON)
            mouse.release(MOUSE_BUTTON)
            time.sleep(DELAY)
    listener.stop()

button = customtkinter.CTkButton(root,text="START",command=start) #start button
button.pack(pady=12,padx=(0,10))

root.mainloop()
