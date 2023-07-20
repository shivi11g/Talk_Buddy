import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random 
import time #for sleep function

engine = pyttsx3.init('sapi5') #microsoft speech api
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    '''Converts text to speech'''
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    '''Wishes user according to time'''
    hour = int(datetime.datetime.now().hour)
    if(hour>=6 and hour<12):
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening")
   
    speak("This is ModiJi. How can i assist you today?")


def takeCommand():
    '''Convert user speech to text'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:  
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMPT('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
    
def tellJoke():
    '''Tells joke'''
    with open ("assets/jokes.txt", "r") as f:
        jokes_list = f.readlines()
        rand_num = random.randint(0, 39)
        joke = jokes_list[rand_num]
        return joke

def addToDoList(task):
    '''Add task in ToDoList'''
    with open ("assets/toDoList.txt", "a") as f:
        f.write(task)
        f.write("\n")
        
        
        
    

if __name__=="__main__":
    # speak("Aashish is a Good boy")
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        #Logic for executing tasks based on query
        
        #-------------Wikepedia search-----------
        if'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        #----------Open a website in browser-----------
        # elif 'open stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")
        # elif 'open youtube' in query:
        #     webbrowser.open("youtube.com")
        # elif 'open google' in query:
        #     webbrowser.open("google.com")
        
        #-----------------Coded self------------------
        elif 'open' in query:
            lst = query.split(" ")
            ind1 = lst.index("open")
            
           
            if(ind1+1<len(lst)):
                website = lst[ind1+1]
                print(website)
                webbrowser.open(f"{website}.com")
                
        #-----------------Play Music------------------
        elif 'play music' in query or 'play song' in query:
            music_dir = 'c:\Users\Shivi Gupta\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        
        #------------------Tell Time-------------------
        elif 'the time' in query or 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time now is {strTime}")
        
        
        #------------------Open IDE-------------------
        elif 'open code' in query or 'open vs code' in query:
            codePath = r"C:\Users\Shivi Gupta\OneDrive\Desktop\Visual Studio Code.lnk"
            os.startfile(codePath)
            
            
        #-------------------Open Spotify--------------
        # elif ('open spotify') in query:
        #     appPath = r"C:\Users\Dell\OneDrive\Desktop\Spotify.lnk"
        #     os.startfile((appPath))
        
        
        #------------------Send an Email----------------
        #-----------inactive for now(Require permission)---------------
        elif 'email to' in query or 'send an email' in query or 'send email' in query:
            try: 
                speak("Whom you want to send email to")
                receiver = takeCommand()
                mailTo = "xyz@gmail.com"  #dummy if mail not found
                
                #find the mailaddress of the receiver
                with open ("emails.txt", "r") as f:
                    email_entires = f.read().splitlines()
                    for email_entry in email_entires:
                        name = email_entry.split(" ")[0]
                        email_address = email_entry.split(" ")[1]
                        if(name==receiver):
                            mailTo = email_address
                
                speak("What should i say through the mail?")
                content = takeCommand()
                sendEmail(mailTo, content)
                speak("Email sent!")
            except exception as e:
                print(e)
                speak("Sorry, I am unable to send the emaiL. Please try again")
                
                
                
        #--------------Tell A joke------------
        elif'joke' in query or'laugh' in query:
            speak("Arzz kiyaa hai")
            joke = tellJoke()
               
            question = joke.split("?")[0]
            ans = joke.split("?")[1]
               
                
            print(question)
            speak(question)
            
            time.sleep(1.5) #pause
            
            print(ans)
            speak(ans)
            speak("Ha ha ha ha!")
            
        #--------------ToDo list------------
        elif ('add to do' in query) or ('add work' in query) or ('add task' in query) or ('add todo' in query) or ('add list' in query) or ('new task' in query) or ('record task' in query) or ('a task' in query) or ('add to list' in query):
            
            
    #strings = ['play music', 'play song', 'start playlist']
    #query = 'play some music please'

    #if any(s in query for s in strings):
        # Do something
        
        
            speak("inside this list")
            while(True):
                speak("What task you want to add to your todo list?")
                task = takeCommand()
                print(task)
                addToDoList(task)
                
                #further tasks add?
                speak("Do you want to add any more tasks to your todo list?")
                response = takeCommand().lower()
                if('yes' or 'more' or 'one' or '1' or 'sure') in response:
                    continue
                else:
                    break

        
        #-----------Setting alarms and timers.------
        
        #---------Responding to simple greetings like "hello" or "hi".--------
        elif('hi'  in query or 'hello' in query):
            speak("Hello there, it's great to hear from you! How can I assist you today?")
            
        #--------Providing weather updates based on location.-----------
        
                
        elif('stop') in query:
            continue;          
        elif ('quit') in query:
            exit()
        
            
        

