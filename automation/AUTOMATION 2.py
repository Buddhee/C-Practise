import pyautogui as a
import time 
time.sleep(1)
a.press("win")
a.moveTo(871,142,2)
a.click()
a.typewrite("whatsapp",0.5)
a.press("enter",2)
a.moveTo(294,186,4)
a.click()
a.typewrite("",0.5)
a.press("enter",1)
a.moveTo(308,289,1)
a.click()
a.moveTo(908,968,1)
a.click()
for i in range (0,1000):

    a.typewrite("Happy New Year🎉 ",0.04)
    a.press("enter")




