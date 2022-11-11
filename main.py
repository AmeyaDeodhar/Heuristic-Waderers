import datetime
from playsound import playsound
import os
import smtplib
import subprocess
import sys
import time
import time as ti
import webbrowser
from email.message import EmailMessage
import secrets
import clipboard
import pywhatkit as kit
import psutil
import pyautogui
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import wolframalpha
from newsapi import NewsApiClient
from requests import get
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

from Pixiefront import Ui_PIXIE

user = "Samruddhi, Chinmayi ,Pradnya And Ameya"
assistant = "Pixie"

print('Loading Your AI Personal Assistant - Pixie')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', 'voices[1].id')
engine.setProperty('rate', 170)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    pass

def idea():
    speak("What is your idea?")
    data = takeCommand().title()
    speak("You Said me to remember this idea: " + data)
    with open("data.txt", "a", encoding="utf-8") as r:
        print(data, file=r)


# You can also use a secret file and store these variables there as I am doing or If you not going to show this code to anyone that you can it here as well.
def sendEmail():
    
    senderemail = "chinmai.juikar@gmail.com"
    password = "Chinu*0201"
    email_list = {
        "Ameya": "adeodhar04@gmail.com",  # Temporary Email
        "sam": "360jadhavsam@gmail.com"
    }
    try:
        email = EmailMessage()
        speak("To whom you want to send the mail?")
        name = takeCommand().lower()
        email['To'] = email_list[name]
        speak("What is the subject of the mail?")
        email["Subject"] = takeCommand()
        email['From'] = senderemail
        speak("What should i Say?")
        email.set_content(takeCommand())
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(senderemail, password)
        s.send_message(email)
        s.close()
        speak("Email has sent")
    except Exception as e:
        print(e)
        speak("Unable to send the Email")


def news():
    newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    speak("What topic you need the news about")
    topic = takeCommand()
    data = newsapi.get_top_headlines(q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        speak(y["description"])


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")




class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()


    # to convert voice into text
    def run(self):
        self.takeExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            
        try:

            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"

        return query.lower()

    def takeExecution(self):
        wishMe()
        speak("Loading your AI Personal Assistant - Pixie")
        speak("Tell me how can I help you now")
        while True:
            self.statement = self.takeCommand()

        

            if "good bye" in self.statement or "ok bye" in self.statement or "stop" in self.statement:
                speak('Your personal assistant Pixie is shutting down,Good bye')
                sys.exit()

            if 'wikipedia' in self.statement:
                speak('Searching Wikipedia...')
                statement = self.statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                speak(results)

            elif 'open youtube' in self.statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            elif 'open google' in self.statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(5)

            elif 'message' in self.statement:
                speak("What should i send to your number")
                whatMsg = self.takeCommand().lower()
                kit.sendwhatmsg_instantly(f"+919967323028", message)

            elif 'email' in self.statement:
                sendEmail()

            elif 'open gmail' in self.statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif "weather" in self.statement:
                api_key = "8ef61edcf1c576d65d836254e11ea420"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name = self.takeCommand()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " + str(
                    current_temperature) + "\n humidity in percentage is " + str(
                    current_humidiy) + "\n description  " + str(weather_description))
                    print(" Temperature in kelvin unit = " + str(
                    current_temperature) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

                else:
                    speak(" City Not Found ")

            elif 'time' in self.statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'who are you' in self.statement or 'what can you do' in self.statement:
                speak('I am Pixie version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in self.statement or "who created you" in self.statement or "who discovered you" in self.statement:
                speak("I was built by Samruddhi, Chinmayi, Pradnya, and Ameya")
                print("I was built by Samruddhi, Chinmayi, Pradnya, and Ameya")

            elif "open stackoverflow" in self.statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")

            elif 'notepad' in self.statement:
                path = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(path)

            elif 'calc' in self.statement:
                path = "C:\\Windows\\System32\\calc.exe"
                os.system(path)

            elif 'open command prompt' in self.statement:
                os.system("Start CMD")

            elif 'news' in self.statement:
                news()
                time.sleep(6)

            elif "camera" in self.statement or "take a photo" in self.statement:
                import cv2

                cap = cv2.VideoCapture(0)
                while True:

                    ret, frame = cap.read()
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                cap.release()
                cv2.destroyAllWindows()

            elif 'Play music' in self.statement:
                mus_fol = "C:\Music"
                music = os.listdir(mus_fol)
                # rd = random.choice(music)
                for song in music:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(mus_fol, music[0]))

            elif 'ip address' in self.statement:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")

            elif 'search' in self.statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)

            elif "read" in self.statement:
                speak(clipboard.paste())

            elif "covid" in self.statement:
                c = requests.get('https://coronavirus-19-api.herokuapp.com/all').json()
                speak(
                    f'Confirmed Cases: {c["cases"]} \nDeaths: {c["deaths"]} \nRecovered {c["recovered"]}')

            elif "joke" in self.statement:
                speak(pyjokes.get_joke())

            elif "idea" in self.statement:
                idea()

            elif "do you know" in self.statement:
                ideas = open("data.txt", "r")
                speak(f"You said me to remember these ideas:\n{ideas.read()}")

            elif "screenshot" in self.statement:
                pyautogui.screenshot(str(ti.time()) + ".png").show()

            elif "cpu" in self.statement:
                speak(f"Cpu is at {str(psutil.cpu_percent())}")

            elif 'tell' in self.statement or 'pixie' in self.statement:
                speak(
                    'I will try to answer your question based on my knowledge and database. What question do you want to ask now')
                question = self.takeCommand()

                app_id = "JET279-Q7RW32GX5W"
                client = wolframalpha.Client('JET279-Q7RW32GX5W')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

            elif "close notepad" in self.statement:
                speak("Closing Notepad")
                os.system("%windir%\system32\notepad.exe")

            elif "alarm" in self.statement:
                speak("please tell the time! . for example set alarm to 5:30 pm")
                tt = takeCommand()
                tt = tt.replace("Set alarm to ", "")
                tt = tt.replace(".","")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)


            elif "Restart the System" in self.statement:
                os.system("shutdown /r /t 5")

            elif "Sleep the System" in self.statement:
                os.system("rundll64.exe powrprof.dll,SetSuspendState 0,1 0")

            elif "log off" in self.statement or "sign out" in self.statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PIXIE()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)


    def startTask(self):
        self.ui.movie = QtGui.QMovie("Images/yay-tinker-bell.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()


        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(5000)
        startExecution.start()

    def showTime(self):
        Current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = Current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)

app = QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
