import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if 'W' in keys:
        return 'W'
    if 'A' in keys:
        return 'A'
    if 'S' in keys:
        return 'S'
    if 'D' in keys:
        return 'D'
    elif ' ' in keys:
        return ' '
    elif 'B' in keys:
        return 'B'
    elif 'H' in keys:
        return 'H'
    elif 'M' in keys:
        return 'M'
    else:
        return ''
