from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your Chromedriver executable
chrome_driver_path = '/path/to/chromedriver'

# Path to the WhatsApp contact or group
whatsapp_url = 'https://web.whatsapp.com/send?phone=1234567890'  # Replace with the recipient's number

# Message to be sent
message = 'Hello! This is an automated message from Python.'

# Initialize Chrome webdriver
driver = webdriver.Chrome(chrome_driver_path)
driver.get(whatsapp_url)

# Allow time to scan the QR code from your phone to log in
time.sleep(15)

# Locate the message input field and send the message
input_field = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
input_field.send_keys(message)
input_field.send_keys(Keys.RETURN)

# Wait for a while and then close the browser
time.sleep(5)
driver.quit()
