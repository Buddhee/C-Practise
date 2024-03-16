import pyautogui as a 
import time 
time.sleep(2)

#1) #For typing 

# b=("Hello , how are you?")
# a.typewrite(b,0.1)

#2) #Hotkeys 

# a.hotkey("ctrl","c")
# a.hotkey("ctrl","v")

#3)#Use of single button 

# a.press("win")
# a.press("win")
# a.press("enter")

#4)Know the position

b=a.position()
print(b)

#5) move the cursor 

# a.moveTo(1738,24,2)
# a.doubleClick()
