import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir!")
    else:
        speak("Good evening Sir!")
    speak("Hello sir, I am your assistant Please tell me how may i help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except  Exception as e:
        # print(e)
        print("Say that again Please........")
        return "None"
    return query
if __name__ == "__main__":
    speak("Let's  have   some    fun   ")
    wishme()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia..............")
            query == query.replace("wikipedia", "")
            results = wikipedia.summary(f'{query}', sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "birthday" in query:
            speak("searching for todays birthdays..............")
            speak("heyy vaidehi its your birthday....wishing you a very happy birthday")
            query = query.replace("birthday", "")
        elif "open youtube" in query:
            speak("Opening youtube for you..............")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'C:\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'turn off' in query:
            speak("Turning off your computer")
            os.system("shutdown /s /t 1")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("Shreya")
            print("My friends call me Shreya")
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by M I T A D T university")
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
