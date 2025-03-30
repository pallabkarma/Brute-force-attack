import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
allchar = list(chars)

pwd = pyautogui.password("Enter a password") 
sample_pwd = ""

while sample_pwd != pwd:
    sample_pwd = "".join(random.choices(allchar, k=len(pwd)))  
    print("<====" + sample_pwd + "===>")
  

    if sample_pwd == pwd: 
        print("The password is: " + sample_pwd)
        break 
