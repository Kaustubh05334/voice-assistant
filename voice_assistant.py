import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
from time import sleep

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
rate = speaker.getProperty('rate')
speaker.setProperty('voice', voices[2].id)
speaker.setProperty('rate', rate-10)

# function text to speech
def speak(audio):
    speaker.say(audio)
    speaker.runAndWait()

# wish the user based on the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("How may I help you today?")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

exit_commands =['thank you', 'i am done','bye','thanks for the help','work done', "that's it",'goodbye','get lost']
if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()
    while (query not in exit_commands):
       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            # path to songs directory
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {Time}")

        sleep(1)
        query = takeCommand().lower()