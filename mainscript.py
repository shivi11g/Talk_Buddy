import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random 
import time #for sleep function
import pywhatkit
import pyautogui
import requests
import math
import openai

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

purple = "#8a2be2"


engine = pyttsx3.init('sapi5') #microsoft speech api
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

commandtext = ""
outputtext = ""

global_i = 0
i=0

def modifyCommandText(newtxt):
    currtext = scrollableLeftContent.cget("text")
    # print(text)
    # newtxt = "Modify karaya baabe da"
    global commandtext
    commandtext =  currtext +  "\n" + newtxt 
    # commandtext.append(currtext)
    
    scrollableLeftContent.configure(text = commandtext)
    
def modifyOutputText(newtxt):
    currtext = scrollableRightContent.cget("text")
    # print(text)
    # newtxt = "Modify karaya baabe da"
    global outputtext
    outputtext =  currtext +  "\n" + newtxt 
    # commandtext.append(currtext)
    
    scrollableRightContent.configure(text = outputtext)




def speak(audio):
    '''Converts text to speech'''
    engine.say(audio)
    engine.runAndWait()



def wishMe():
        '''Wishes user according to time'''
        # currtext = scrollableLeftContent.cget("text")
        
        
        # # print(text)
        # newtxt = "Modify karaya baabe da"
        # global commandtext
        # commandtext = newtxt + commandtext + "\n" + currtext 
        # # commandtext.append(currtext)
        
        # scrollableLeftContent.configure(text = commandtext)
        
        # txt = "modify karaya"
        # modifyCommandText(txt)
        
        hour = int(datetime.datetime.now().hour)
        if(hour>=6 and hour<12):
            speak("Good Morning !")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        
        else:
            speak("Good evening")
    
        speak("This is your talk buddy. How can i assist you today?")
        modifyOutputText("This is your talk buddy. How can i assist you today?")

def takeCommand():
    '''Convert user speech to text'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        print("Executed threshold")
        r.energy_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("Executed energy")
        audio = r.listen(source)
        print("Gone to end")
        
    try:  
        print("Recognising...")
        query = r.recognize_google(audio, language='En-In')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def openai_output(inp):
        openai.api_key = ''
        messages = [ {"role": "system", "content": "You are an intelligent assistant."} ]

        message = inp
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )

        reply = chat.choices[0].message.content
        print(f"OpenAI: {reply}")
        messages.append({"role": "assistant", "content": reply})
        return reply
        
        
def send_whatsapp_message(to, content):
    try:
        in_file = False
        f = open("whatsapp_contacts.txt", "r")
        lines = f.read().split('\n')
        for line in lines:
            phn = line.split(":")[0]
            name = line.split(":")[1]
            if(name==to):
                string_ph = phn
                in_file = True
                break
    
        pywhatkit.sendwhatmsg_instantly(
            phone_no = string_ph, 
            message = content
        )
        print("Message sent!")
    except Exception as e:
        print(str(e))
    
    
def send_schedule_whatsapp_message(to, content, time_h, time_m):
    try: 
            in_file = False
            f = open("whatsapp_contacts.txt", "r")
            lines = f.read().split('\n')
            for line in lines:
                phn = line.split(":")[0]
                name = line.split(":")[1]
                if(name==to):
                    string_ph = phn
                    in_file = True
                    break           
            pywhatkit.sendwhatmsg(
                phone_no= string_ph, 
                message = content,
                time_hour = int(time_h),
                time_min = int(time_m)
            )
            print("Message sent!")
    except Exception as e:
        print(str(e))


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

def button_callback():
    print("button clicked")
    
def take_query():
    query = takeCommand().lower()
    
    modifyCommandText(query)
     
    #Logic for executing tasks based on query

    
    # -------------About Assistant-----------------
    if 'about yourself' in query or 'who are you' in query or 'introduce yourself' in query:
        text = "Hello! I am your virtual talk buddy, a virtual assistant,Feel free to ask me anything, and I'll do my best to assist you!"
        modifyOutputText(text)
        speak(text)
 
        
    #-------------Wikipedia search-----------
    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia',"")
        results = wikipedia.summary(query, sentences = 2)
        
        modifyOutputText("According to Wikipedia")
        speak("According to Wikipedia")
        
        modifyOutputText(results)
        print(results)
        speak(results)

    
    #------------------Open IDE-------------------
    elif 'open code' in query or 'open vs code' in query:
        codePath = r"C:\Users\Shivi Gupta\OneDrive\Desktop\Visual Studio Code.lnk"
        os.startfile(codePath)

        
    #-------------------Open Spotify--------------
    # elif ('open spotify') in query:
    #     appPath = r"C:\Users\Dell\OneDrive\Desktop\Spotify.lnk"
    #     txt = "Opening Spotify"
    #     modifyOutputText(txt)
    #     speak(txt)
        
    #     os.startfile((appPath))

        
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
            webdomain = website.split(".")[0]
            
            txt = f"Opening {webdomain}.com"
            speak(txt)
            modifyOutputText(txt)
            
            webbrowser.open(f"{webdomain}.com")
            
            
    #-----------------Play Music------------------
    elif 'play music' in query or 'play song' in query:
        music_dir = 'c:\\Users\\Shivi Gupta\\Music'
        songs = os.listdir(music_dir)
        
        outputtext = "Playing music"
        modifyOutputText(outputtext)
        speak(outputtext)
        
        # print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

        
    
    #------------------Tell Time-------------------
    elif 'the time' in query or 'time now' in query or 'tell time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        
        modifyOutputText(f"The time now is {strTime}")
        speak(f"The time now is {strTime}")
    
    
    
    
    
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
        except Exception as e:
            print(e)
            speak("Sorry, I am unable to send the emaiL. Please try again")

    # -----------Send Whatsapp Message-------
    elif 'whatsapp' in query:
        try:
            speak("Whom you want to send whatsapp message to") 
            receiver = takeCommand().lower()
            print(receiver)
            
            speak("What should i say through the mail?")
            content = takeCommand()
            speak("Do you want to schedule this message")
            flag = takeCommand().lower()
            if flag == "yes":
                speak("Give the time hour")
                time_hour = takeCommand()
                speak("Give the time minute")
                time_minute = takeCommand()
                send_schedule_whatsapp_message(receiver, content, time_hour, time_minute)
            else:
                send_whatsapp_message(receiver, content)
        except Exception as e:
            print(e)
            speak("Sorry, I am unable to send the whatsapp message. Please try again")
            
            
    #--------------Tell A joke------------
    elif 'joke' in query or 'laugh' in query:
        speak("Arzz kiyaa hai")
        joke = tellJoke()
            
        question = joke.split("?")[0]
        ans = joke.split("?")[1]
            
            
        print(question)
        modifyOutputText(question)
        speak(question)
        
        time.sleep(1.5) #pause
        
        print(ans)
        modifyOutputText(ans)
        speak(ans)
        speak("Ha ha ha ha!")
        
    #--------------ToDo list------------
    elif ('add to do' in query) or ('add work' in query) or ('add task' in query) or ('add to do' in query) or ('add list' in query) or ('new task' in query) or ('record task' in query) or ('a task' in query) or ('add to list' in query):
        
        
#strings = ['play music', 'play song', 'start playlist']
#query = 'play some music please'

#if any(s in query for s in strings):
    # Do something
    
        speak("V")
        speak("inside this list")
        speak("What task you want to add to your todo list?")
        task = takeCommand()
        txtoutput = f"Adding the task - {task} to list."
        modifyOutputText(txtoutput)
        print(task)
        addToDoList(task)
        speak("Do you want to add anymore tasks to the list?")
        if(takeCommand() == "yes"):
            speak("What task you want to add to your todo list?")
            task = takeCommand()
            txtoutput = f"Adding the task - {task} to list."
            modifyOutputText(txtoutput)
            print(task)
            addToDoList(task)
        else:
            speak("Ok")
        
        # while(True):
            #further tasks add?
            # speak("Do you want to add any more tasks to your todo list?")
            # response = takeCommand().lower()
            # if('yes' or 'more' or 'one' or '1' or 'sure') in response:
            #     continue
            # else:
            #     break

    
    #-----------Setting alarms and timers.------
    
    #---------Responding to simple greetings like "hello" or "hi".--------
    elif('hi'  in query or 'hello' in query):
        speak("Hello there, it's great to hear from you! How can I assist you today?")
        take_query()
    
    #--------Providing weather updates based on location.-----------
    elif 'weather' in query:
        lst= query.split(" ")
        idx= lst.index("of")
        idx1= idx+1
        city_name= lst[idx1]
        api_key= ""
        temp=""
        humidity=""


        def get_weather(api_key, city_name, temp, humidity):
            url= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
            response= requests.get(url).json()
            print(response)
            temp= response['main']['temp']
            # print(temp)
            temp= math.floor((temp)- 273.15)
            feels_like= response['main']['feels_like']
            feels_like= math.floor((feels_like)- 273.15)
            humidity= response['main']['humidity']
            # humidity= math.floor((temp)- 273.15)
            return { 
            'temp': temp,
            'feels_like': feels_like,
            'humidity' : humidity
            }

        weather= get_weather(api_key, city_name, temp, humidity)
        # get_weather(api_key, city_name)
        print(weather['temp'])
        print(weather['feels_like'])
        print(weather['humidity']) 
        temp= weather['temp']
        humidity= weather['humidity']  
        speak(f"{city_name} has a temperature of {temp} degree celsius and {humidity} humidity gram per metre cube")
        modifyOutputText(f"{city_name} has a temperature of {temp} degree celsius and {humidity} humidity gram per metre cube")
 
            
    elif('stop') in query:
        # continue;      
        pass    
    
    elif ('quit') in query:
        exit()
   
   
   #uncomment later
    
    else:
        outputgpt = openai_output(query)
        speak(outputgpt)
        print(outputgpt)
        modifyOutputText(outputgpt)
        
    
    
def assist():
    global global_i
    if(global_i==0):
        wishMe()
        global_i+=1
    else:
        speak("How can I assist you?")
    take_query()
    
    # while True:
        
        
            
#----------------------------------------------
#GUI IMPLEMENTATION --->
#----------------------------------------------


#---root---
app = customtkinter.CTk()

app.title("Virtual assistant")
app.geometry("1400x700")
# app.config(background='#a7c5f9')



# Load the microphone image
logo_image = Image.open("assets/logo4.png")
logo_icon = ImageTk.PhotoImage(logo_image)

# Load the image file
# logo_image = customtkinter.PhotoImage(file="assets/logo.png")

# Create a label widget to display the image
logo_label = customtkinter.CTkLabel(app, text = "", image=logo_icon , pady = 20)
logo_label.pack()


#--------label---------
# label = customtkinter.CTkLabel(app, text="Virtual Assistant", fg_color="transparent",  width=150 , height= 50, font=("Arial", 30))
# label.pack(padx=20, pady = 20)
#-------------


#main frame
main_frame = customtkinter.CTkFrame(master=app ,bg_color='transparent')
main_frame.pack(pady=20, padx=60, fill='both',expand=True)


# main_frame.master.configure(background='black')



# left frame
left_frame = customtkinter.CTkFrame(main_frame)
left_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of frame
labelleft = customtkinter.CTkLabel(left_frame, text="Command Window", fg_color="transparent",  width=70 , height= 30, font=("Arial", 15))
labelleft.pack(padx=10, pady = 10)

#childScrollabeFrame
leftchild_frame = customtkinter.CTkScrollableFrame(left_frame)
leftchild_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of scrollableFrame
scrollableLeftContent = customtkinter.CTkLabel(leftchild_frame, text = "hello world",fg_color="transparent",  width=50 , height= 20, font=("Arial", 15), wraplength=300)
print("checking error")
scrollableLeftContent.pack(padx=10, pady = 10)



# middle frame
middle_frame = customtkinter.CTkFrame(main_frame)
middle_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

# Load the assistant_face
assistant_face_image = Image.open("assets/char_bot.jpg")
assistant_face_image = assistant_face_image.resize((500, 450))  # Resize the image as needed
assistant_face_icon = ImageTk.PhotoImage(assistant_face_image)


#label of middleframe
labelleft = customtkinter.CTkLabel(middle_frame, image = assistant_face_icon,text="", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15))
labelleft.pack(padx=10, pady = 10)






# right frame
right_frame = customtkinter.CTkFrame(main_frame)
right_frame.pack(side="right", padx=20, pady=20)

#label of right frame
labelright = customtkinter.CTkLabel(right_frame, text="Output Window", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15))
labelright.pack(padx=10, pady = 10)

#childScrollabeFrame
rightchild_frame = customtkinter.CTkScrollableFrame(right_frame)
rightchild_frame.pack(side="right", padx=20, pady=20)

#label of scrollableFrame
scrollableRightContent = customtkinter.CTkLabel(rightchild_frame, text = "hello world", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15), wraplength=300)
print("checking error")
scrollableRightContent.pack(padx=10, pady = 10)





# Load the microphone image
mic_image = Image.open("assets/microphone2.png")
mic_image = mic_image.resize((40, 40))  # Resize the image as needed
mic_icon = ImageTk.PhotoImage(mic_image)

# Create the circular button
mic_button = customtkinter.CTkButton(app, image=mic_icon, text = "give command", command=assist)
mic_button.pack(padx=20, pady=20)

#--------button-----
# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.pack(padx=20, pady=20)
#------------------



app.mainloop()
