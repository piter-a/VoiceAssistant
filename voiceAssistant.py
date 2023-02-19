import os
import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import spotipy as sp
import credentials
import pyautogui
import psutil
import pygetwindow as gw
import subprocess
import time
from spotipy.oauth2 import SpotifyOAuth
   
r = sr.Recognizer()

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

# ?????? 
# play song on spotify --> make function to do that using a voice command
# song_name = 'arachnophobia'
# result = spotify.search(q = song_name, type = 'track')
# uri = result['tracks']['items'][0]['uri']
# spotify.start_playback(device_id = deviceID, context_uri = uri)
# ?????? 

# take audio input
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# listen for user query
def takeCommand():
    with sr.Microphone(device_index = 0) as source:
        audio = r.listen(source)

    query = r.recognize_google(audio)

    return query

# search google for user query --> search google for + x
def googleSearch(query):
    googlesearch = query.split()
    googlesearch = ' '.join(googlesearch[3:])
    kt.search(query)

# play on youtube --> youtube play + vid name
def playOnYt(query):
    ytsearch = query.split()
    ytsearch = ' '.join(ytsearch[2:])
    kt.playonyt(query)

# command for playing spotify --> spotify play + song name
def playSpotify(query):
    command = query.split()
    song_name = ' '.join(command[2:])
    result = spotify.search(q = song_name, type = 'track')
    uri = result['tracks']['items'][0]['uri']
    spotify.start_playback(device_id = deviceID, context_uri = uri)

# make a function to select primary/secondary roles using voice commands (DONE)
# select game mode using voice commands (DONE)

# check if league is already running, if running open league window
# else start league (DONE)
# query = takeCommand()

# playOnYt(ytsearch)

# query = takeCommand()

def startLeague():
    # first check if the league of legends client is running
    # if it is not running then start it
    process_name = 'LeagueClient.exe'

    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            print(f"The {process_name} process is running.")
            try:
                league = gw.getWindowsWithTitle('League of Legends')[0]
                league.restore()
                print(f"{process_name} window activated.")
            except Exception as e:
                print(f"Failed to activate {process_name} window: {e}")
            break
    else:
        print(f"The {process_name} process is not running. Starting {process_name}...")
        try:
            subprocess.Popen(r"D:\Riot Games\League of Legends\LeagueClient.exe")
            print(f"{process_name} started successfully.")
        except Exception as e:
            print(f"Failed to start {process_name}: {e}")

def selectMode(query):
    gamemode = None
    playbtn = None

    while playbtn == None:
        playbtn = pyautogui.locateOnScreen('playbtn.png', confidence = 0.7)
        pyautogui.leftClick(playbtn)

    while gamemode == None:    
        if 'solo' in query:
            gamemode = pyautogui.locateOnScreen('ranked.png', confidence = 0.7)
        elif 'normal' in query or 'blind' in query:
            gamemode = pyautogui.locateOnScreen('normal.png', confidence = 0.7)
        elif 'draft' in query:
            gamemode = pyautogui.locateOnScreen('draft.png', confidence = 0.7)
        elif 'flex' in query:
            gamemode = pyautogui.locateOnScreen('flex.png', confidence = 0.7)

    pyautogui.leftClick(gamemode)
    confirm = pyautogui.locateOnScreen('confirm.png', confidence = 0.7)
    pyautogui.leftClick(confirm)

def selectRole(query):
    primary = False
    secondary = False

    while primary == False and secondary == False:
        for i in range(len(query)):
            if query[i] == 'primary':
                if query[i + 1] == 'fill':
                    pyautogui.leftClick(974, 842)
                    time.sleep(1)
                    pyautogui.leftClick(1124, 784)
                    primary = True
                    secondary = True
                elif query[i + 1] == 'top':
                    pyautogui.leftClick(974, 842)
                    time.sleep(1)
                    pyautogui.leftClick(834, 784)
                    primary = True
                elif query[i + 1] == 'jungle':
                    pyautogui.leftClick(974, 842)
                    time.sleep(1)
                    pyautogui.leftClick(888, 784)
                    primary = True
                elif query[i + 1] == 'mid':
                    pyautogui.leftClick(974, 842)
                    time.sleep(1)
                    pyautogui.leftClick(942, 784)
                    primary = True
                elif query[i + 1] == 'bot' or query[i + 1] == 'adc':
                    pyautogui.leftClick(974, 842)
                    time.sleep(1)
                    pyautogui.leftClick(996, 784)
                    primary = True
                elif query[i + 1] == 'support':
                    pyautogui.leftClick(974, 842)
                    time.sleep(1)
                    pyautogui.leftClick(1049, 784)
                    primary = True  

            elif query[i] == 'secondary':
                if query[i + 1] == 'top':
                    pyautogui.leftClick(1014, 842)
                    time.sleep(1)
                    pyautogui.leftClick(872, 784)
                    secondary = True
                elif query[i + 1] == 'jungle':
                    pyautogui.leftClick(1014, 842)
                    time.sleep(1)
                    pyautogui.leftClick(926, 784)
                    secondary = True
                elif query[i + 1] == 'mid':
                    pyautogui.leftClick(1014, 842)
                    time.sleep(1)
                    pyautogui.leftClick(980, 784)
                    secondary = True
                elif query[i + 1] == 'bot' or query[i + 1] == 'adc':
                    pyautogui.leftClick(1014, 842)
                    time.sleep(1)
                    pyautogui.leftClick(1034, 784)
                    secondary = True
                elif query[i + 1] == 'support':
                    pyautogui.leftClick(1014, 842)
                    time.sleep(1)
                    pyautogui.leftClick(1088, 784)
                    secondary = True
                elif query[i + 1] == 'fill':
                    pyautogui.leftClick(1014, 842)
                    time.sleep(1)
                    pyautogui.leftClick(1162, 784)
                    secondary = True

def findAndAccept():
    # find match btn
    findmtch = pyautogui.locateOnScreen('findmatch.png', confidence = 0.7)
    pyautogui.leftClick(findmtch)

    # accept match
    accept = pyautogui.locateOnScreen('accept.png', grayscale = True, confidence = 0.7)

    while accept == None:
        accept = pyautogui.locateOnScreen('accept.png', grayscale = True, confidence = 0.7)

    pyautogui.click(accept) 

# testing if league of legends role selection works properly

# query = takeCommand().lower()

# if 'league of legends' in query:
#     startLeague()

# speak('Starting league of legends, what game mode would you like to play?')

# mode = takeCommand().lower()

# speak(f'ok, i will choose {mode}')

# selectMode(mode)

# speak('what roles would you like to play?')

# roles = takeCommand().lower()
# roles = roles.split()

# selectRole(roles)

# speak('ok, are you ready to queue up?')

# yes_or_no = takeCommand().lower()

# if yes_or_no == 'yes':
#     findAndAccept()

# testing if youtube search and play works properly

# query = takeCommand().lower()
# playOnYt(query)




