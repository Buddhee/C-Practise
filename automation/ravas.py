import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
import os
import webbrowser
import time
import pint 
import math
from PIL import Image, ImageDraw, ImageFont

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

# Define the filename for remembering messages
REMEMBER_FILE = 'remember.txt'

def talk(text):
    engine.say(text)
    engine.runAndWait()

    
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print(command)
            return command
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Speech recognition request failed: {e}")
        return ""

def greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 3 <= hour < 12:
        talk("Good morning sir")
    elif 12 <= hour < 18:
        talk("Good afternoon sir")
    else:
        talk("Good evening sir")

def create_image(command):
    try:
        talk("Sure, please tell me what you want to write on the image.")
        text_to_write = take_command()
        
        # Create a new image
        img = Image.new('RGB', (800, 600), color='white')
        draw = ImageDraw.Draw(img)
        
        # Set the font and size (using default font)
        font = ImageFont.load_default()
        
        # Set the text color
        text_color = 'black'
        
        # Calculate the position to center the text
        text_width, text_height = draw.textsize(text_to_write, font)
        x = (img.width - text_width) // 2
        y = (img.height - text_height) // 2
        
        # Draw the text on the image
        draw.text((x, y), text_to_write, font=font, fill=text_color)
        
        # Save the image
        img.save('created_image.png')
        
        talk('Image created successfully. Check the file named "created_image.png".')
    except Exception as e:
        talk("Sorry, there was an error creating the image. Please try again.")
        print(f"Error creating image: {e}")





def send_whatsapp_message(contact_name, message):
    # Open WhatsApp
    pyautogui.press("win")
    pyautogui.moveTo(871, 142, 2)
    pyautogui.click()
    pyautogui.typewrite("whatsapp", 0.5)
    pyautogui.press("enter", 2)

    # Search for the contact
    pyautogui.moveTo(294, 186, 4)
    pyautogui.click()
    pyautogui.typewrite(contact_name, 0.5)
    pyautogui.press("enter", 1)

    pyautogui.moveTo(297,271,2)
    pyautogui.click()



    # Click on the chat box
    pyautogui.moveTo(896,1043,2)
    pyautogui.click()

    # Type and send the message
    pyautogui.typewrite(message, 0.04)
    pyautogui.press("enter")

def run_jarvis():
    command = take_command()
    if 'hello' in command or 'hi' in command:
        talk('Hi boss, how are you?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'play' in command:
        song = command.replace('play', "").strip()
        talk(f'playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Current time is", current_time)
        talk(current_time)
    elif 'open' in command:
        app = command.replace('open', '').strip()
        pyautogui.press('win')
        pyautogui.typewrite(app)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        talk(f'opening {app}')
    elif 'close' in command:
        talk('closing sir')
        pyautogui.hotkey('alt', 'f4')
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is'in command  or 'tell me about'in command:
        topic = command.replace('what is', '').strip()
        information=wikipedia.summary(topic,2)
        print(information)
        talk (information)
        
    elif 'remember that' in command:
        remember_message = command.replace('remember that', '').strip()
        talk('you told me to remember that')
        with open(REMEMBER_FILE, "a") as remember:
            remember.write(remember_message + '\n')
    elif 'what do you remember' in command:
        with open(REMEMBER_FILE, 'r') as remember:
            talk('you told me to remember ' + remember.read())
    elif 'clear remember file' in command:
        with open(REMEMBER_FILE, 'w') as file:
            file.write('')
        talk('done sir...everything I remembered has been deleted')
    elif 'shutdown' in command:
        talk(' ok sir your pc will be shutting down in')
        talk('3 . 2 . 1')
        os.system('shutdown /s /t 1')
    elif 'restart' in command:
        talk('okay sir, your PC will restart in')
        talk('3 . 2 . 1')
        os.system('shutdown /r /t 1')
    elif 'search' in command:
        user_query = command.replace('search', '').lower()
        webbrowser.open(f'https://www.google.com/search?q={user_query}')
        talk('this is what I found on the internet')
    elif 'send message' in command:
        try:
            talk("Sure, please tell me the recipient's name.")
            contact_name = take_command().lower()
            talk(f"Got it. What message would you like to send to {contact_name}?")
            message = take_command()
            send_whatsapp_message(contact_name, message)
            talk(f"Message sent to {contact_name} successfully.")
        except Exception as e:
            talk("Sorry, there was an error sending the message. Please try again.")
    elif any(keyword in command for keyword in ['pause', 'stop', 'resume', 'start']):
        pyautogui.press('k')
        talk('done sir!')
    elif 'full screen' in command:
        pyautogui.press('f')
        talk('done sir!')
    elif 'theater screen' in command:
        pyautogui.press('t')
        talk('done sir!')
    elif 'create image' in command:
        create_image(command)
    elif 'convert' in command:
        topic = command.replace('convert', '').strip()
        information=wikipedia.summary(topic,1)
        print(information)
        talk (information)
    elif  'i love you' in command: 
        a=('Sorry I have a boyfriend')
        print(a)
        talk(a)
    
    elif any(keyword in command for keyword in ['exit', 'quit', 'bye']):
        talk('Bye sir...see you soon....')
        exit()
    else:
        talk("Sorry sir..I didn't get that....will you please repeat ? ")


# ... (Rest of the code remains the same)

text = 'Hello, I am Jarvis'

greeting()

while True:
    run_jarvis()
