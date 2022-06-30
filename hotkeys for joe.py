from global_hotkeys import *

import time

import os

from bot import click_if_exists

from time import sleep

from pyperclip import copy

from pyautogui import hotkey

from pyautogui import doubleClick

import sys

is_alive = True

dont_fuck_up = False

print("Good Morning!")
print("These keyboard commands are for the MagicArt 5 program.")
print("Ctrl + 1 : .925 Template")
print("Ctrl + 2 : 10K Template")
print("Ctrl + 3 : 14K Template")
print("Ctrl + 4 : Logos Template")
print("Ctrl + 5 : Close Hotkeys Program")
print("Good luck, and have a nice day!")

#https://stackoverflow.com/questions/4606919/in-python-try-until-no-error

usual_sleep_time = 1

def open_templates():
    global dont_fuck_up
    if not dont_fuck_up:
        dont_fuck_up = True
        
        print("Opening MagicArt")
        
        #opening MagicArt program
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MagicArt 5\MagicART 5.lnk")
        time.sleep(usual_sleep_time + 1)

        #making MagicArt fullscreen
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\fullscreen.png')

        #minimizing object property box
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\object property pin.png')
        
        #process to open templates
        for i in template_list:
            hotkey("ctrl", "o")
            time.sleep(usual_sleep_time)
            copy(i)
            hotkey("ctrl", "v")
            hotkey("enter")
            time.sleep(usual_sleep_time)
            
        #zoom for Logos Template
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\Logos Template.png')
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\fit to page.png')
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\10%.png')
        
        #zoom for K Templates
        for k in zoom_list:
            print(f"Looking for {k}...")
            click_if_exists(k)
            click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\fit to page.png')
            click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\15%.png')
            
        dont_fuck_up = False
    print("Command Successful")

template_list = [
    ".925 Template",
    "10K Template",
    "14K Template",
    "Logos Template",]

zoom_list = [
    r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\Silver Template.png',
    r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\10K Template.png',
    r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\14K Template.png',]



def open_silver():
    global dont_fuck_up
    if not dont_fuck_up:
        dont_fuck_up = True
        print("Silver Command Triggered...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\Silver Template.png')
        dont_fuck_up = False
    print("Command Successful")

def open_10K():
    global dont_fuck_up
    if not dont_fuck_up:
        dont_fuck_up = True
        print("10K Command Triggered...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\10K Template.png')
        dont_fuck_up = False
    print("Command Successful")

def open_14K():
    global dont_fuck_up
    if not dont_fuck_up:
        dont_fuck_up = True
        print("14K Command Triggered...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\14K Template.png') 
        dont_fuck_up = False
    print("Command Successful")

def open_logos():
    global dont_fuck_up
    if not dont_fuck_up:
        dont_fuck_up = True
        print("Logos Command Triggered...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\Logos Template.png')
        dont_fuck_up = False
    print("Command Successful")

def center_allignment():
    global dont_fuck_up
    if not dont_fuck_up:
        dont_fuck_up = True
        print("Centering Object...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\center button.png')
        dont_fuck_up = False
    print("Command Successful")

def horizontal_allignment():
    global dont_fuck_up
    if not dont_fuck_up:
        dont_fuck_up = True
        print("Alligning Horizontally...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\horizontal allign.png')
        dont_fuck_up = False
    print("Command Successful")

def exit_application():
        print("Exiting Application. Have a good day!")
        global is_alive
        stop_checking_hotkeys()
        is_alive = False
        

bindings = [
    [["F2"], None, open_silver],
    [["F3"], None, open_10K],
    [["F4"], None, open_14K],
    [["F5"], None, open_logos],
    [["control", "b"], None, horizontal_allignment],
    [["control", "alt"], None, center_allignment],
    [["shift", "escape"], None, exit_application],
    [["F12"], None, open_templates],
]

register_hotkeys(bindings)

start_checking_hotkeys()

while is_alive:
    time.sleep(0.1)
