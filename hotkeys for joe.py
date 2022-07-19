from global_hotkeys import *

import time

import os

from bot import click_if_exists

from time import sleep

from pyperclip import copy

from pyautogui import hotkey

from pyautogui import doubleClick

import sys

import webbrowser

is_alive = True

dfu = False

usual_sleep_time = 1

print("Good Morning!")
print("These keyboard commands are for the MagicArt 5 program:")
print(" F1 = .925 Template")
print(" F2 = 10K Template")
print(" F3 = 14K Template")
print(" F4 = Logos Template")
print(" F11 = Open SKU Search")
print(" F12 = Open MagicArt")
print(" Shift + Escape : Close Hotkeys Program")
print("Good luck, and have a nice day!")
print(".")
print(".")
print(".")
print(".")
print(".")



def open_templates():
    global dfu
    if not dfu:
        dfu = True
        
        print("Opening MagicArt")
        
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MagicArt 5\MagicART 5.lnk")
        time.sleep(usual_sleep_time + 1)

        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\fullscreen.png')

        found = click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\object property pin.png')
        if not found:
            click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\highlighted open magicart.png')
            click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\open magicart.png')
            click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\object property pin.png')
            click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\fullscreen.png')

        for i in template_list:
            hotkey("ctrl", "o")
            time.sleep(usual_sleep_time)
            copy(i)
            hotkey("ctrl", "v")
            hotkey("enter")
            time.sleep(usual_sleep_time)
            
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\Logos Template.png')
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\fit to page.png')
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\10%.png')
        
        for k in zoom_list:
            print(f"Looking for {k}...")
            click_if_exists(k)
            click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\fit to page.png')
            click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\15%.png')
            
        dfu = False
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
    global dfu
    if not dfu:
        dfu = True
        print("Silver Command Triggered...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\Silver Template.png')
        dfu = False
    print("Command Successful")

def open_10K():
    global dfu
    if not dfu:
        dfu = True
        print("10K Command Triggered...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\10K Template.png')
        dfu = False
    print("Command Successful")

def open_14K():
    global dfu
    if not dfu:
        dfu = True
        print("14K Command Triggered...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\14K Template.png') 
        dfu = False
    print("Command Successful")

def open_google():
    global dfu
    if not dfu:
        dfu = True
        print("Opening Google")
        webbrowser.open(f"https://www.google.com/")
        dfu = False
    print("Command Successful")

def open_workday():
    global dfu
    if not dfu:
        dfu = True
        print("Opening Workday...")
        webbrowser.open(f"https://www.myworkday.com/wday/authgwy/signetjewelers/login.htmld")
        dfu = False
    print("Command Successful")

def open_SKU_search():
    global dfu
    if not dfu:
        dfu = True
        print("opening SKU finder...")
        os.startfile(r'C:\Users\rcherveny\Desktop\Keyboard Commands\sku_search.py')
        dfu = False
    print("Command Successful")

def open_logos():
    global dfu
    if not dfu:
        dfu = True
        print("Logos Command Triggered...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\Logos Template.png')
        dfu = False
    print("Command Successful")

def center_allignment():
    global dfu
    if not dfu:
        dfu= True
        print("Centering Object...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\center button.png')
        dfu = False
    print("Command Successful")

def horizontal_allignment():
    global dfu
    if not dfu:
        dfu = True
        print("Alligning Horizontally...")
        click_if_exists(r'C:\Users\rcherveny\Desktop\Keyboard Commands\images\horizontal allign.png')
        dfu = False
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
    [["F9"], None, open_google],
    [["F10"], None, open_workday],
    [["F11"], None, open_SKU_search],
    [["F12"], None, open_templates],
    [["control", "shift"], None, horizontal_allignment],
    [["control", "alt"], None, center_allignment],
    [["shift", "escape"], None, exit_application],
]

register_hotkeys(bindings)

start_checking_hotkeys()

while is_alive:
    time.sleep(0.1)
