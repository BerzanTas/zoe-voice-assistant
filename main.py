
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import wikipedia
import wolframalpha
import pywhatkit
import time
import workonwebsite


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

        if 'youtube' in website:
            while True:
                self.talk("What do you want me to play?")

                name = self.command().lower()
                time.sleep(1)
                
                if 'play' in name:
                    name = name.replace('play', '')
                    workonwebsite.youtube(name)
                    break
                elif 'nothing' in name:
                    break

                time.sleep(3)

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


    def list_or_dict(self, var):
        if isinstance(var, list):
            return var[0]['plaintext']
        else:
            return var['plaintext']
        

    
    def current_time(self):
        time = datetime.now().time()
        time = str(time).split(":")
        self.talk(f"{time[0]} hours and {time[1]} minutes")



    def wolfram_compute(self):
        query = self.query.replace("compute", "")
        self.talk('computing')

        response = wolfram_client.query(query)

        if response['@success'] == 'false':
            return 'Could not compute'

        else:
            result = ''

            pod0 = response['pod'][0]
            pod1 = response['pod'][1]

            if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):

                result = self.list_or_dict(pod1['subpod'])
                return result.split('(')[0]
            else:
                question = self.list_or_dict(pod0['subpod'])
                return question.split('(')[0]
                self.talk('Computation failed. Checking for information in wikipedia.')
                return self.search_wikipedia(question)

    #main loop
    def main(self):
        while True:
            while True:
                wake_up = self.command().lower()
                if 'zoe' in wake_up and 'wake up' in wake_up:
                    break

            
            self.talk('Hi owner! How can I help you?')

            while True:
            
                self.query = self.command().lower()
                
                if activationWord in self.query:
                    self.query = self.query.replace("zoe", "")

                    if len(self.query.split()) == 0:
                        self.talk('Yes owner? What can I do for you?')

                    if 'say hello' in self.query:
                        self.say_hello()
                    
                    #plays song on youtube
                    if 'play' in self.query:
                        self.play_youtube()

                    #opens the website
                    if 'go to' in self.query:
                        self.go_to_website()
                        time.sleep(1)


                    if 'are you there' in self.query:
                        self.talk("Yes, I am here and I am listening to your commands.")
                    
                    #searches for something in wikipedia
                    if 'search' in self.query and 'wikipedia' in self.query:
                        self.search_wikipedia()
                    
                    if 'compute' in self.query:
                        try:
                            result = self.wolfram_compute()
                            self.talk(result)
                        except:
                            self.talk('Im unable to compute, Im sorry')

                            
                    if 'what time' in self.query:
                        self.current_time()

                        
                    if 'sleep' in self.query and len(self.query.split()) == 1:
                        self.talk('I will take a nap')
                        break
                    if 'close' in self.query:
                        self.talk('Goodbye')
                        exit()
                    
if __name__ == "__main__":

    assistant = Zoe()
    assistant.main()

