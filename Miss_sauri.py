import pyttsx3
import speech_recognition as sr

import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
                speak("Good Morning!")

        elif hour>=12 and hour<18:
                speak("Good Afternoon!")

        else:
                speak("Good Evening!")

        speak("Hi, I am your virtual assistant miss,saouri")
        speak("How can i help you")

def stop():
        speak("ok bye, I hope we will met soon !")
        r.pause_threshold = 0.3

def takeCommand():
        #it take speech input and return string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 0.5
                audio = r.listen(source)
        try:
                print("Recognizing...")
                query = r.recognize_google(audio, language = 'en-in')
                print(f"User said: {query}\n")
        
        except Exception as e:
                #print(e) #show exception error detail
                print("Say that again please...")
                #speak("Say that again please...")
                return "None"
        return query
def action(): # for excute commands
         #while True:
        if 1:
                query = takeCommand().lower()

                #Logic for excution of task based on query

                if 'wikipedia' in query:
                        speak("Searching wikipedia...")  
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences = 2)
                        speak("According to wikipedia")
                        speak(results)

                elif 'youtube' in query:
                        webbrowser.open("youtube.com")
                elif 'google' in query:
                        webbrowser.open("google.com")
                elif 'search' in query:
                        webbrowser.open("google.com")
                elif 'knowledge hub' in query:
                        webbrowser.open("wikipedia.com")
                elif 'my blog' in query:
                        webbrowser.open("saurabhritu.wordpress.com")
                elif 'play music' in query:
                        music_dir = 'C:\\Users\\Saurabh Ritu\\Music'
                        songs = os.listdir(music_dir)
                        #print(songs)
                        os.startfile(os.path.join(music_dir,songs[2]))
                elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"The time is {strTime}")
                elif "open dev" in query:
                        codepath = "C:\Program Files (x86)\Dev-Cpp\devcpp.exe"
                        os.startfile(codepath)
                elif "chrome" in query:
                        os.system("start chrome.exe")
                elif "stop" in query:
                        stop()
                else:
                        print("I didn't get that")
                        #speak("I didn't get that")
                        #print("Say that again please")
                        #speak("can you speak again ?")
                action()

if __name__ == "__main__":
        wishMe()
        if 1:
                action()

      