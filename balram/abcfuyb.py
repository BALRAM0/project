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
from playsound import playsound
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()





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
