import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


from wikipedia import exceptions


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)



def speak (audio):
    engine.say (audio)
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning sir!")

     elif hour>=12 and hour <18:
             speak ("good Afternoon sir!")
     else:
         speak("good evening sir !")

speak("I am Friday sir. tell me how can i help you")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")   
    except Exception as e:
        # print(e) 
        print ("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('debojitmisra66@gmail.com', 'by transfer 1234')
    server.sendmail('birbhumccb012@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
     if 1:
         query = takeCommand().lower()
     
     # logic for our AI
     if 'wikipedia' in query:
         speak("searching wikipedia....")
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences = 2)
         speak("according to wikipedia")
         print (results)
         speak (results)
     elif 'open youtube'in query:
         webbrowser.open("youtube.com")
     elif 'open google'in query:
         webbrowser.open("google.com")
     elif 'open stackoverflow'in query:
         webbrowser.open("stackoverflow.com")
     elif 'open whitehat Jr'in query:
         webbrowser.open("https://www.whitehatjr.com/")
    


     elif "play music" in query:
         music_dir = 'D:\\music\000om shanti om'
         songs = os .listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))
         "D:\music\000om shanti om"
     elif "the time"in query:
         strtime = datetime.datetime.now().strftime('%H:%M:%S')
         speak(f'sir, the  time is{strtime}')
     elif 'open code'in query:
         codepath="C:\\Users\\WIN10-PC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
         os.startfile(codepath)
     elif 'message to baba'in query:
         try:
             speak ('what should I send')
             content = takeCommand()
             to = 'birbhumccb012@gmail.com'
             sendEmail(to, content)
             speak('sir,Email has been sent')
         except exceptions as e:
                print(e)
                speak('sorry sir, the mesage cannot be send')






