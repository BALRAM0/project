import datetime
import time
import webbrowser
import os
    
import pyttsx3
import requests , json 
import speech_recognition as sr 
import wikipedia
import pyjokes 
import requests
from bs4 import BeautifulSoup
# from playsound import playsound





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    # playsound("abc.mp3")
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning Sir ")
        print("Hello,Good Morning Sir ")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon Sir ")
        print("Hello,Good Afternoon Sir ")
    else:
        speak("Hello,Good Evening Sir ")
        print("Hello,Good Evening Sir ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            state = r.recognize_google(audio)
            print("User said:{}\n".format(state))

        except :
            speak("Sorry, please say that again")
            
            return "None"
        return state


print("Loading your AI personal assistant friday")
speak("Loading your AI personal assistant friday")
wishMe()
if __name__ == '__main__':
        while True:
            speak("Tell me how can I help you now?")
            statement = takeCommand().lower()
            if statement == 0:
                continue

            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('your personal assistant friday is shutting down,Good bye')
                print('Your personal assistant friday is shutting down,Good bye')
                break
            
            elif 'how are you' in statement:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in statement or "good" in statement:
                speak("It's good to know that your fine")
                time.sleep(5)
                        
            elif "what's your name" in statement or "What is your name" in statement:
                speak("My friends call me")
                speak('friday')
                print("My friends call me FRIDAY")
                time.sleep(5)
                
            elif 'is love' in statement:
                speak("It is 7th sense that destroy all other senses")
                time.sleep(5)
                
            elif "who are you" in statement:
                speak("I am your virtual assistant created by Balram")
                time.sleep(5)
                
            elif 'joke' in statement:
                joke=pyjokes.get_joke()
                speak('joke')
                print('joke')
                time.sleep(5)

            elif 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                time.sleep(5)
                
            elif 'open youtube' in statement or 'youtube'in statement :
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("Opening YOUTUBE ")
                time.sleep(5)

            elif 'open google' in statement or 'google chrome'in statement or 'open browser' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Default Brouser is opening now")
                time.sleep(5)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/")
                speak("Opening Mail Services ")
                time.sleep(5)
            
            elif 'time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The Time is {strTime}")

                time.sleep(6)
                
            elif "don't listen" in statement or "pause" in statement:
                speak("friday is sleeping now....... See You SOON sir")
                print("friday is sleeping now.......")
                a=input("Enter Any KEY TO Awake")
                continue
                
            elif "where is" in statement or "location" in statement or "search location" in statement :
                if "where is" in statement:
                    statement = statement.replace("where is", "")
                elif "location" in statement:
                    statement = statement.replace("location", "")
                elif "search location" in statement:
                    statement = statement.replace("search location", "")
                location = str(statement)
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.co.in/maps/search/"+location)
                time.sleep(5)
            
            elif "will you be my gf" in statement or "will you be my bf"in statement:  
                speak("I'm not sure about, may be you should give me some time")
                print("I'm not sure about, may be you should give me some time")
                time.sleep(3)

            elif "how are you" in statement:
                speak("I'm fine, glad you me that")
                print("I'm fine, glad you me that")
                time.sleep(3)

            elif "i love you" in statement:
                speak("It's hard to understand")
                print("It's hard to understand")
                time.sleep(5)
                
            elif 'search' in statement:
                statement = statement.replace("search", "")
                assert isinstance(statement)
                assert isinstance(statement)
                webbrowser.open_new_tab(statement)
                time.sleep(5)
                
            elif 'weather' in statement:
                city = "yamunanagar,haryana"


                url = "https://www.google.com/search?q="+"weather"+city
                html = requests.get(url).content


                soup = BeautifulSoup(html, 'html.parser')
                temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

                data = str.split('\n')
                time = data[0]
                sky = data[1]


                listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
                strd = listdiv[5].text


                pos = strd.find('Wind')
                other_data = strd[pos:]
                print("Temperature is", temp)
                speak("Temperature is"+temp)
                print("Time: ", time)
                speak("Time: "+time)
                print("Sky Description: ", sky)
                speak("Sky Description: "+sky)
                print(other_data)
                speak(""+other_data)

            
            elif 'spotify' in statement or 'play music' in statement or 'open spotify' in statement:
                speak("opening spotify please login first to listen music")
                webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M")            
                time.sleep(5) 

        

    

