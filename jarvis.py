import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else: 
        speak("Good Evening sir!")

    speak("I am Jarvis, how may i assist you today?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    
    return query





if __name__ == "__main__":
    # speak("Rohit is a good boy") 
    wishMe()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    
    query = takeCommand().lower()

    if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results =wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

    elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.get(chrome_path).open("youtube.com")

    elif 'open google' in query:
            speak("opening google...")
            webbrowser.get(chrome_path).open("google.com")

    elif 'open facebook' in query:
            speak("opening facebook...")
            webbrowser.get(chrome_path).open("facebook.com")

    elif 'open stackoverflow' in query:
            speak("opening StackOverflow...")
            webbrowser.get(chrome_path).open("stackoverflow.com")
    
    elif 'open github' in query:
            speak("opening GitHub...")
            webbrowser.get(chrome_path).open("github.com")

    elif 'time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is {strTime}")

    elif 'play music' in query:
        music_dir='c:\\Users\\ROHIT\\Downloads\\Music'
        songs=os.listdir(music_dir)
        pos=random.randint(0,len(songs))
        os.startfile(os.path.join(music_dir,songs[pos]))

    elif 'open android studio' in query:
        path="F:\\Andriod Studio\\bin\\studio64.exe"
        os.startfile(path)

    elif 'open sublime text' in query:
        path=" C:\\Program Files\\Sublime Text 3"
        os.startfile(path)

    elif 'open proton vpn' in query:
        path="C:\\Program Files (x86)\\Proton Technologies\\ProtonVPN\\ProtonVPN.exe"
        os.startfile(path)

    elif 'joke' in query:
        jokes=["Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.","Dentist: “This will hurt a little , Patient:OK , Dentist: Ive been having an affair with your wife for a while now.","Two donkeys are standing at a roadside, one asks the other: So, shall we cross?The other shakes his head: No way, look at what happened to the zebra.","One of the most wonderful things in life is to wake up and enjoy a cuddle with somebody; unless you are in prison.","Google request:How to disable autocorrect in wife?","I hate people who take drugs. DEA is the worst.","Broccoli: Hey, I look like a tree.Mushroom: Wow, I look just like an umbrella.Walnut: I look exactly like a brain.Banana: Man, can we change the topic please?","Pessimist: Things just can't get any worse!Optimist: Nah, of course they can!","A snowman sniffs, Hm, funny, I smell carrots…","Scientists have now discovered how women keep their secrets. They do so within groups of 40.","Astronaut's last words: OMG guys, who farted? I have to open the window."]
        # speak(jokes[0])
        speak(random.choice(jokes))


    elif 'quit' in query:
        speak("Good Bye Sir...")
        exit()



       

   
