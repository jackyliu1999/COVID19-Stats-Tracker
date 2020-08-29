import speech_recognition as sr #pip install SpeechRecognition, #pip install pipwin, pipwin install pyaudio
import pyttsx3 as p #pip install pyttsx3
from Functions import *

textToSpeech = p.init()
voices = textToSpeech.getProperty("voices") #array of default text to speech voices
textToSpeech.setProperty("voice", voices[1].id) #voice of id 1
textToSpeech.setProperty('rate',120) #slows down voice
print("Welcome to Coronaverse, please state your command")
textToSpeech.say("Welcome to Coronaverse, please state your command") #says this as introduction prompt
textToSpeech.runAndWait()

def command(newCommand):
    if newCommand.lower() == "stats today" or newCommand.lower() == "daily stats" or newCommand.lower() == "today":
        dailyStats()
    if newCommand.lower() == "financial help canada":
        financialHelp()
    if newCommand.lower() == "news" or newCommand.lower() == "get news":
        news()
    if newCommand.lower() == "united states" or newCommand.lower() == "stats united states":
        statsUS()
    if newCommand.lower() == "canada" or newCommand.lower() == "stats canada":
        statsCanada()
    if newCommand.lower() == "reddit":
        reddit()
    if newCommand.lower() == "buy mask":
        buyMasks()
    if newCommand.lower() == "buy sanitizer" or newCommand.lower() == "buy hand sanitizer":
        buySanitizer()
    if newCommand.lower() == "clinic":
        clinic()
    if newCommand.lower() == "help":
        help()

r = sr.Recognizer()
newText = ""
commands = ["stats today", "daily stats", "today", "financial help canada", "news", "get news", "united states", "stats united states", "canada", "stats canada"
            ,"reddit", "buy mask", "buy sanitizer", "buy hand sanitizer", "clinic", "help"]

while newText != "quit program" and newText != "close program" and newText != "quit":
    with sr.Microphone() as source:
        try:
            print("Computer: Please state next command?")
            text = r.listen(source,phrase_time_limit=8)
            newText = r.recognize_google(text)
            print("You said: " + newText)
            if newText.lower() in commands:
                command(newText)
        except sr.UnknownValueError:
            print("Computer: Invalid Command, please try again.")

print("Coronaverse Exiting...")
textToSpeech.say("Coronaverse Exiting") #says this as exit prompt
textToSpeech.runAndWait()