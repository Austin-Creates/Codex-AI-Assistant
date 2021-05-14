import pyttsx3
import speech_recognition as sr
import datetime
import calendar
import webbrowser
import pywhatkit
import wikipedia
import pyjokes
import smtplib
from email.message import EmailMessage



# method to accept and recognize commands given by Austin
def acceptCommands():
    # create speech_recognition
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-us')
            print("User:", Query)
        except Exception as e:
            print(e)
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.date.today()
    speak(calendar.day_name[day.weekday()])
    '''Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)'''


def tellTime():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    output = "Your current local time is " + current_time
    speak(output)
    '''time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")'''


def welcome():
    speak('Hello User! I am Codex your desktop assistant. How can i help you??')

def Take_query():
    welcome()
    while (True):
        query = acceptCommands().lower()
        if "open youtube" in query:
            speak("Opening youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "open scratch" in query:
            speak("Opening scratch")
            webbrowser.open("https://scratch.mit.edu")

        elif "open school web" in query:
            speak("Opening Manage back")
            webbrowser.open("https://agakhan.managebac.com/student")

        elif "how old are you" in query:
            speak("I never give my age!")

        elif "open browser" in query:
            speak("Opening Google Chrome ")
            webbrowser.open("www.google.com")
            continue

        elif "codex" in query:
            speak("Yes user! What can I do for you??")
            continue

        elif "library" in query:
            speak("Opening Z-library")
            webbrowser.open("https://z-lib.org/")

        elif "what day is it" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif "goodbye" in query:
            speak("Good Bye User!")
            exit()

        elif "thank you" in query:
            speak("You're welcome User, what else can I do for you??")

        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "your name" in query:
            speak("I am Codex. An AI Desktop Assistant!")
            continue

        elif 'search web' in query:
            pywhatkit.search(query)
            speak("Searching Result in Google!" + query)
            continue

        elif 'play' in query:
            speak('playing ' + query)
            pywhatkit.playonyt(query)
            continue

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            continue

        elif 'send me an email' in query:
            speak("Ask my brother Swift to help you! He is an Email Bot")

        else:
            speak("Sorry User! I didn't get that!")


if __name__ == '__main__':
    Take_query()

