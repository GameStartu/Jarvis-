import pyttsx3
from pywhatkit.main import take_screenshot
import pywhatkit
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import instaloader
import wikipedia
# import mediapipe
import webbrowser
import PyPDF2
import kill
import pywhatkit as kit
import smtplib
import sys
import time
import timer
import pyjokes
import requests
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

MASTER = "KISHOR"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[len(voices)-1].id)

# text  to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("say that again  please...")
        return"none"
    query = query.lower()
    return query


def pdf_Reader():
    book = open('py3.pdf', 'rb')
    pdfReader = PyPDF2.pdfFilereader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in thiss book (pages")
    speak("sir please enter the page number i have to read sir")
    pg = int(input("please enter the page number:  "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

# to wish


def wish():

    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning sir , its {tt}!")

    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon sir, its {tt}")

    else:
        speak(f"good evening sir, its {tt}")

    speak("Inatializing JARVIS........")
    speak("I am JARVIS sir . please tell me how may help you")

# to send email


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'YOUR PASSWORD')
    server.sendmail('your email id', to, content)
    server.close()


def TaskExecution():
    wish()
    while True:
        # if 1:

        query = takecommand().lower()
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open commnand prompt" or "open CMD" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitkey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllwindows()

        elif "ip address" or "what is my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif"open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open whatsapp" in query:
            speak("sir, to who should i send messange")
            cm = takecommand().lower()
            webbrowser.open(f"www.whatsappweb.com")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+91_To_number_you_want_to_send",
                            "this is testing protocol", 2, 25)
            time.sleep(120)
            speak("meassage has been sent")

        elif "play song on youtube" in query:
            speak("which song do you want me to play")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            kit.playonyt("speak")

        elif"email to kishor" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "kishorbusari@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to kihor ")

            except Exception as e:
                print(e)
                speak("sorry sir , I am not able to  send  email")

        elif "open vs code" in query:
            npath = "C:\\Users\\svs\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)

        elif "open typing master" in query:
            npath = "C:\Program Files (x86)\TypingMaster10\tmaster.exe"
            os.startfile(npath)

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes ?")
            timing = takecommand()
            timing = timing.replace("minutes',")
            timing = timing.replace("minute',")
            timing = timing.replace("for',")
            timing = float(timing)
            timing = timing*60
            speak(f'I will remind you in {timing}seconds')
            time.sleep(timing)
            speak('Your time has been finished sir')

        elif " close notepad" in query:
            speak("okay sir, closing notepad")
            os.sysytem("Taskkill /f /im notepad.exe")

        elif "close vs code" in query:
            speak('okay sir, closing vs code')
            os.system9("Taskkil /f /im vscode.exe")

        elif "close goggle" in query:
            speak("ok sir, closing google..")
            os.system("Taskkill /f /im google.exe")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("sutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,setSuspendState 0,1,0")

        elif"switch the window " in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "where i am" in query or "where we are " in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'-json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(
                    f"sir i am not sure, but i think we are in  {city} city of {country} country")
            except Exception as e:
                speak(
                    "sorry sir, Due to network issue i am not able to find where we are.")
                pass

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please  enter the username correctly.")
            name = input("Enter user name:")
            webbrowser.open("www.instagram.com/{name}")
            speak(f"sir here  is the profile  of the user {name}")
            time.sleep(5)
            speak("sir would you  like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,  pofile_pic_only=True)
                speak(
                    "I am doen sir , profile picture is saved to our main folder . now i am ready ")
            else:
                pass

        elif"take screenshot" in query or "take a screenshot" in query:
            speak("sir ,please tell me the name for this screenshot file")
            name = takecommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak(
                "i am done sir , the screenshot is saved in our main folder.now i am ready for next command")

        elif"read pdf" in query:
            pdf_Reader()

        elif"no thanks" in query:
            speak("thanks for using me sir,have a great day..")
            sys.exit()

        elif "hello " in query or "hey " in query:
            speak("hello sir,may i help you with something")

        elif "How are you" in query:
            speak("I am fine sir, what about you.")

        elif "also good" in query or "fine " in query:
            speak("that's great to hear that sir....")

        elif "thank you " in query or "thanks" in query:
            speak("it's my pleasure sir...")

        elif "you can sleep " in query or "sleep now" in query:
            speak("okay sir, i am going to sleep sir you can call me anytime")
            break

        elif 'hi' in query or 'hello' in query:
            speak('Hello sir,how may i help you?')
