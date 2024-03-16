import pyautogui as a 
import time 
time.sleep(1)

a.press("win")

a.typewrite("Youtube")

a.press("enter")

# b=a.position()
# print(b)

a.moveTo(706,169,4)
a.leftClick(706,169)

a.typewrite('tay hai',0.2)
a.press('enter')

time.sleep(2)

a.moveTo(369,399,0.1)
a.click()
time.sleep(1) 

a.hotkey('f')
