
from keyauth import api
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
import configparser
import ctypes
config = configparser.ConfigParser()
config.read('Jeden.ini')
os.system('color b')
os.system('title Fluxsploit V6.3 - Loading')
os.system('mode con cols=47 lines=15')
os.system('cls')
print("              \n            Made By, Fluo & Reubeu\n  _                     _ _                   \n | |                   | (_)                  \n | |     ___   __ _  __| |_ _ __   __ _       \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |      \n | |___| (_) | (_| | (_| | | | | | (_| |_ _ _ \n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, (_|_|_)\n                                   __/ |      \n                                  |___/       \n")

def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')
    elif platform.system() == 'Linux':
        os.system('clear')
        sys.stdout.write('\x1b]0;Python Example\x07')
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\\e[3J'")
        os.system('echo - n - e "\x1b]0;Python Example\x07"')
        return None


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), 'rb')
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

#keyauthapp = api('Fluo V5', 'YxDZlbZ7VT', '2e593d443a36cd3c15689fee8c8662d3a91cfa84331a7d64446979c1787444e0', '1.0', getchecksum(), **('name', 'ownerid', 'secret', 'version', 'hash_to_check'))

#def answer():
   # key = config.get('License', 'license_key')
   # keyauthapp.license(key)

#answer()
time.sleep(1)
print('Settings successfully loaded')
serial_port = config.get('Serial', 'port')
serial_baudrate = config.getint('Serial', 'baudrate')
time.sleep(1)
print('Connecting to arduino ...')
time.sleep(1)
import win32api
import serial
import cv2
import os
from mss import mss
import numpy as np
import keyboard
import win32console
import win32gui
from win32console import GetConsoleWindow
import sys
import configparser
import threading
import winsound
time_between_shot = config.getfloat('Tr1ggerb0t', 'time_between_shot')
tr1gger_fov = config.getint('Tr1ggerb0t', 'fov')
fov = config.getint('4imass1st', 'fov')
center = fov / 2
hide = config.get('Hotkey', 'hide')
destroy = config.get('Hotkey', 'destroy')
reload_config = config.get('Hotkey', 'reload_config')
X_speed = config.getfloat('4imass1st', 'Xspeed')
Y_speed = config.getfloat('4imass1st', 'Yspeed')
Xspeed = X_speed
Yspeed = Y_speed
CustomOffSet = config.getfloat('4imass1st', 'offset')
colorup = np.array(config.get('Color', 'colorup').split(','), dtype=np.uint8)
colordown = np.array(config.get('Color', 'colordown').split(','), dtype=np.uint8)
aimhotkey01 = int(config.get('Hotkey', '4imass1st01'), 0)
aimhotkey02 = int(config.get('Hotkey', '4imass1st02'), 0)
triggerhotkey01 = int(config.get('Hotkey', 'tr1gger01'), 0)
sct = mss()
connect = serial.Serial(serial_port, serial_baudrate)
screenshot = sct.monitors[1]
left = int(screenshot['width'] / 2 - fov / 2)
top = int(screenshot['height'] / 2 - fov / 2)
screenshot['left'] = left
screenshot['top'] = top
screenshot['width'] = fov
screenshot['height'] = fov
region = {
    'left': left + fov // 2 - tr1gger_fov,
    'top': top + fov // 2 - tr1gger_fov,
    'width': tr1gger_fov,
    'height': tr1gger_fov }
os.system('cls')
os.system('color b')
os.system('title Fluxsploit V6.3 - ON')
os.system('mode con cols=66 lines=18')
os.system('cls')
print("  ______ _                      _       _ _    __      __    __  \n |  ____| |      Made by       | |     (_) |   \\ \\    / /   / /  \n | |__  | |_  Fluo & Reubeu __ | | ___  _| |_   \\ \\  / /   / /_  \n |  __| | | | | \\ \\/ / __| '_ \\| |/ _ \\| | __|   \\ \\/ /   | '_ \\ \n | |    | | |_| |>  <\\__ \\ |_) | | (_) | | |_     \\  /    | (_) |\n |_|    |_|\\__,_/_/\\_\\___/ .__/|_|\\___/|_|\\__|     \\(_)    \\___/ \n                         | |                                   \n                         |_|\n                         ")
print('                          Hide = {}'.format(hide))
print('                        Destroy = {}'.format(destroy))
print('                     Reload Config = {}'.format(reload_config))
print('')

def update_config():
    global running_status, fov, X_speed, Y_speed, CustomOffSet, colorup, colordown, aimhotkey01, aimhotkey02, triggerhotkey01, running_status
    os.system('color b')
    running_status = False
    config.read('Jeden.ini')
    fov = config.getint('4imass1st', 'fov')
    X_speed = config.getfloat('4imass1st', 'Xspeed')
    Y_speed = config.getfloat('4imass1st', 'Yspeed')
    CustomOffSet = config.getfloat('4imass1st', 'offset')
    colorup = np.array(config.get('Color', 'colorup').split(','), dtype=np.uint8)
    colordown = np.array(config.get('Color', 'colordown').split(','), dtype=np.uint8)
    aimhotkey01 = int(config.get('Hotkey', '4imass1st01'), 0)
    aimhotkey02 = int(config.get('Hotkey', '4imass1st02'), 0)
    triggerhotkey01 = int(config.get('Hotkey', 'tr1gger01'), 0)
    print('\n\n\nSuccessfully reloaded config!')
    running_status = True
    print('\x1b[F\x1b[K', '', **('end',))
    print('\x1b[3F', '', **('end',))

keyboard.add_hotkey(reload_config, update_config)

def play_sound():
    frequency = 1000
    duration = 100
    winsound.Beep(frequency, duration)

console = GetConsoleWindow()

def toggle_console():
    console_state = win32gui.IsWindowVisible(console)
    if console_state:
        win32gui.ShowWindow(console, 0)
    else:
        win32gui.ShowWindow(console, 1)
        return None

keyboard.add_hotkey(hide, toggle_console)
console1 = GetConsoleWindow()

def close_program():
    os.kill(os.getpid(), 9)

keyboard.add_hotkey(destroy, close_program)
toggle_4imass1st = False

def toggled_4imass1st():
    global toggle_4imass1st
    toggle_4imass1st = not toggle_4imass1st

keyboard.add_hotkey(config.get('Hotkey', '4imass1st_togglekey'), toggled_4imass1st)
toggle_tr1ggerb0t = False

def toggled_tr1ggerb0t():
    global toggle_tr1ggerb0t
    toggle_tr1ggerb0t = not toggle_tr1ggerb0t

keyboard.add_hotkey(config.get('Hotkey', 'tr1ggerb0t_togglekey'), toggled_tr1ggerb0t)

def mousemove_x(x):
    if x < 0:
        x = x + 256
        pax = [
            int(x)]
    connect.write(pax)


def mousemove_y(y):
    if y < 0:
        y = y + 256
        pax = [
            int(y)]
    connect.write(pax)

running_status = True

def print_status():
   # if running_status:
     #   None(None, print, **'\x1b[F\x1b[F' if toggle_4imass1st else '' if toggle_tr1ggerb0t else ('end',))
        time.sleep(1)
        #continue
       # return None

status_thread = threading.Thread(print_status, **('target',))
status_thread.daemon = True
status_thread.start()
if toggle_4imass1st:
    if win32api.GetAsyncKeyState(aimhotkey01) < 0 or win32api.GetAsyncKeyState(aimhotkey02) < 0:
        img = np.array(sct.grab(screenshot))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, colorup, colordown)
        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(mask, kernel, 5, **('iterations',))
        thresh = cv2.threshold(dilated, 60, 255, cv2.THRESH_BINARY)[1]
        (contours, hierarchy) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) != 0:
            min_contour = min(contours, (lambda c: cv2.boundingRect(c)[1]), **('key',))
            (x, y, w, h) = cv2.boundingRect(min_contour)
            diff_y = int((y + w / 4 - center) + CustomOffSet)
            diff_x = int(x + w / 2 - center)
            y = diff_y * Yspeed
            x = diff_x * Xspeed
            mousemove_x(x)
            mousemove_y(y)
            if toggle_tr1ggerb0t and win32api.GetAsyncKeyState(triggerhotkey01) < 0:
                img = np.array(sct.grab(region))
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, colorup, colordown)
                if np.sum(mask) > 0:
                    connect.write(bytes([
                        0,
                        0,
                        ord('c')]))
                    time.sleep(time_between_shot)
                    if toggle_4imass1st and toggle_tr1ggerb0t:
                        Yspeed = Y_speed * 2
                        Xspeed = X_speed * 2
                    else:
                        Yspeed = Y_speed
                        Xspeed = X_speed
             #   else:
            #        return None
