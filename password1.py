import random
import pyautogui
import time
chars ="abcdefghijklmnopqrstuvwxyz0123456789"
allchar = list(chars)
pwd = pyautogui.password("Enter a password")
sample_pwd = ""
while sample_pwd != pwd:
    sample_pwd = "".join(random.choices(allchar , k = len(pwd)))
    print("<====" + sample_pwd + "===>")
    time.sleep(0.2)
    if sample_pwd == pwd:
        print("The password is :" + sample_pwd)
        break
