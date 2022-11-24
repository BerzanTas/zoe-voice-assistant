
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import wikipedia
import wolframalpha
import pywhatkit


#speech engine initalisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

activationWord = 'zoe'

app_id = 'R62449-JA4TLJKQHA'
wolfram_client = wolframalpha.Client(app_id)


#Chrome path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

class Zoe():
    def __init__(self):
        pass

    def talk(self,text, rate = 120):
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()

    def command(self):
        listener = sr.Recognizer()
        print('Zoe is listening...')

        with sr.Microphone() as source:
            listener.pause_threshold = 2
            input_speech = listener.listen(source)

        try:
            print('Recognizing speech...')
            query = listener.recognize_google(input_speech, language='en')
        
        except:
            pass

            return 'None'

        return query

    def play_youtube(self):
        song = self.query.replace("play", "")
        self.talk('playing' + song)
        pywhatkit.playonyt(song)

    def say_hello(self):
        self.talk('Hi everyone, Im Zoe')


    def go_to_website(self):
        website = self.query.replace("go to", "")
        self.talk("Opening" + website)
        webbrowser.get('chrome').open_new(website)

    def search_wikipedia(self):
        sentence = self.query.replace("search","").replace("on wikipedia", "")
        
        self.talk("Searching for" + sentence)

        search_results = wikipedia.search(sentence)

        if not search_results:
            print('No wikipedia result')
            return 'No results received'
        
        try:
            wiki_page = wikipedia.page(search_results[0])
        
        except wikipedia.DisambiguationError as error:
            wiki_page = wikipedia.page(error.options[0])
        print(wiki_page.title)
        wiki_summary = str(wikipedia.summary(wiki_page, sentences = 2))
        
        self.talk(wiki_summary)
    
    def wolfram_compute(self):
        self.talk('computing')


    def main(self):
        
        self.talk('Yo! How can I help you?')

        while True:
        
            self.query = self.command().lower()
            
            if activationWord in self.query:
                self.query = self.query.replace("zoe", "")

                if 'say hello' in self.query:
                    self.say_hello()
                
                #plays song on youtube
                if 'play' in self.query:
                    self.play_youtube()

                #opens the website
                if 'go to' in self.query:
                    self.go_to_website()

                if 'are you there' in self.query:
                    self.talk("Yes, I am here and I am listening to your commands.")
                
                #searches for something in wikipedia
                if 'search' in self.query and 'wikipedia' in self.query:
                    self.search_wikipedia()
                
                if 'compute' in self.query:
                    self.wolfram_compute()
#main loop
if __name__ == "__main__":

    assistant = Zoe()
    assistant.main()


    













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