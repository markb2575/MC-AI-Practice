import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2
import pyautogui
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *

def label_func(x): return x.parent.name
learn_inf = load_learner("C:/Users/markb/OneDrive/Desktop/FCbot/GC/export.pkl")
print("loaded learner")

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

# Hold down W no matter what!

# Randomly pick action then sleep.
# 0 do nothing release everything ( except W )
# 1 hold left
# 2 hold right
# 3 Press Jump

while True:

    image = grab_screen(region=(50, 100, 799, 449))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image,(224,224))
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    #print(result[2][0].item(), result[2][1].item(), result[2][2].item(), result[2][3].item())

    #action = random.randint(0,3)
    
    # if action == "Jump" or result[2][0]>.1:
    #     print(f"JUMP! - {result[1]}")
    #     keyboard.press("space")
    #     keyboard.release("a")
    #     keyboard.release("d")
    #     time.sleep(sleepy)mmmmmm

    # if action == "Nothing":
    #     #print("Doing nothing....")
    #     keyboard.release("w")
    #     keyboard.release("a")
    #     keyboard.release("s")
    #     keyboard.release("d")
    #     time.sleep(sleepy)

    if action == "Attack":
        print(f"ATTACK! - {result[1]}")
        pyautogui.click()
        time.sleep(sleepy)

    elif action == "Forward":
        print(f"FORWARD! - {result[1]}")
        keyboard.press("w")
        keyboard.release("s")
        
        time.sleep(sleepy)

    elif action == "Backward":
        print(f"BACKWARD! - {result[1]}")
        keyboard.press("s")
        keyboard.release("w")
        
        time.sleep(sleepy)

    elif action == "Left":
        print(f"LEFT! - {result[1]}")
        keyboard.press("a")
        keyboard.release("d")
        
        time.sleep(sleepy)
    elif action == "Right":
        print(f"RIGHT! - {result[1]}")
        keyboard.press("d")
        keyboard.release("a")
        
        time.sleep(sleepy)

    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break
