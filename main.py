import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "what time is it" in data:
        speak(ctime())

    if "weather" in data:
        data = data.split(" ")
        time = data[2]
        location = data[4]
        speak("Hold on Dave, I will show you the weather " + time + " in " + location + ".")
        os.system("google-chrome https://www.google.com/search?source=hp&q=weather+"+location+"+"+time)
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Dave, I will show you where " + location + " is.")
        os.system("google-chrome https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization

time.sleep(2)
speak("Hi Dave, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)

