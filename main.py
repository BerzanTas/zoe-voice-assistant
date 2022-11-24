
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import wikipedia
import wolframalpha

#speech engine initalisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

activationWord = 'zoe'

def talk(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def command():
    listener = sr.Recognizer()
    print('Zoe is listening...')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en')
    
    except Exception as exception:
        print('I dont understand, please repeat')
        talk('I dont understand, please repeat')

        print(exception)
        return 'None'

    return query
    
#main loop
if __name__ == "__main__":
   
   talk('Yo! How can I help you?')

   while True:
       
       query = command().lower().split()
       
       if query[0] == activationWord:
           query.pop(0)

           if query[0] == 'say':
               if 'hello' in query:
                   talk('Hi everyone, Im Zoe')
               else:
                   query.pop(0)
                   speech = ' '.join(query)
                   talk(speech)


    













"""

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def intro_talk():
    engine.say("Hey! What you want?")
    engine.runAndWait()
        



def talk(text):
    engine.say(text)
    engine.runAndWait()

def main():
    try:
        with sr.Microphone() as source:
            print("Zoe is listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "zoe" in command:
                talk(command)
    except:
        pass
"""