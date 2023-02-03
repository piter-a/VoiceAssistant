import os
import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import spotipy as sp
import credentials
import pyautogui
import cv2
import time
from spotipy.oauth2 import SpotifyOAuth
from pywinauto import Application


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

auth_manager = SpotifyOAuth(
    client_id = credentials.cid,
    client_secret = credentials.secret,
    redirect_uri = credentials.redirect_uri,
    scope = credentials.scope,
    username = credentials.user_id
)

spotify = sp.Spotify(auth_manager = auth_manager)

devices = spotify.devices()
deviceID = None

# get current device name
for i in range(len(devices['devices'])):
    if devices['devices'][i]['name'] == credentials.device_name:
        deviceID = devices['devices'][i]['id']
        break

# play song on spotify --> make function to do that using a voice command
# song_name = 'arachnophobia'
# result = spotify.search(q = song_name, type = 'track')
# uri = result['tracks']['items'][0]['uri']
# spotify.start_playback(device_id = deviceID, context_uri = uri)

# take audio input
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# listen for user query
def takeCommand():
    
    r = sr.Recognizer()
    mic = sr.Microphone(device_index = 0)

    with mic as source:
        audio = r.listen(source)

    query = r.recognize_google(audio)

    return query

# search google for user query
def googleSearch(query):
    kt.search(query)


# query = takeCommand().lower()

# if 'League of Legends' in query:
#     engine.say('Opening league of legends')
#     engine.runAndWait()
#     os.startfile(r"D:\Riot Games\League of Legends\LeagueClient.exe")

# automating mouse clicks using pyautogui
# to select role + start game in league of legends

# os.startfile(r"D:\Riot Games\League of Legends\LeagueClient.exe")

# starter function get user input etc later
def startRankedMidJgl():
    # click play button
    playbtn = pyautogui.locateOnScreen('playbtn.png', confidence = 0.7)
    pyautogui.leftClick(playbtn)

    time.sleep(1)

    # select game mode(ranked)
    ranked = pyautogui.locateOnScreen('ranked.png', confidence = 0.7)
    pyautogui.leftClick(ranked)

    time.sleep(1)

    # confirm
    confirm = pyautogui.locateOnScreen('confirm.png', confidence = 0.7)
    pyautogui.leftClick(confirm)

    time.sleep(1)

    # select jungle and mid
    # jungle
    pyautogui.leftClick(974, 842)
    pyautogui.leftClick(896, 773)

    # mid
    pyautogui.leftClick(1011, 842)
    pyautogui.leftClick(983, 773)

    pyautogui.displayMousePosition()


    time.sleep(1)

    # find match btn
    findmtch = pyautogui.locateOnScreen('findmatch.png', confidence = 0.7)
    pyautogui.leftClick(findmtch)

    # accept match
    accept = pyautogui.locateOnScreen('accept.png', grayscale = True, confidence = 0.7)

    while accept == None:
        accept = pyautogui.locateOnScreen('accept.png', grayscale = True, confidence = 0.7)

    pyautogui.click(accept)


# make a function to select primary/secondary roles using voice commands
# select game mode using voice commands

# play songs from yt



