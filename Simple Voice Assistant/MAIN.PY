#LIBRARIES
from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import glob
from playsound import playsound
import winsound
# import pygame
import smtplib
# import pyowm
import pywhatkit
import AppOpener
from AppOpener import run
# import wmi
# import sounddevice as sd
# import soundfile as sf
# import imagepip


dict_email={
    'rohan' : '0rohankamble1@gmail.com',
    'omkar' : 'omraje5990@gmail.com',
    'om'    : 'rageomraje90@gmail.com',
    'shreyas' : 'shreyas7557@gmail.com'

    }
engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice", voices[0].id)
# WELCOME STATEMENT
def speek(audio):
    engine.setProperty("rate",150)
    engine.say(audio)
    engine.runAndWait()



def time():
    Time= ("The current time is ",datetime.datetime.now().strftime("%H:%M:%S"))
    speek(Time)
    


def date():
    date=datetime.datetime.now().strftime("%m-%d-%Y")
    new_date=date.replace('-',' ')

    print(date)

    Date=("Today's date is",new_date)
    speek(Date)



def wish():
    
    # winsound.PlaySound("C:\\Users\\Kaustubh\\Downloads\\logo of M2M like irona man jarvis effect and iron man interface (online-audio-converter.com).wav",winsound.SND_FILENAME)


    hour=datetime.datetime.now().hour
    if   (hour >= 6 and hour < 12):
        speek("Hello!  Good morning sir!")
    elif (hour >= 12 and hour<=16):
        speek("Hello!  Good afternoon sir!")
    elif (hour >=16 and hour <=24):
        speek("Hello!  Good evening sir")
    else:
        speek("")
    
        


def reciver():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTINING......")
        r.pause_thrshold = 0.6
        r.energy_threshold= 4000
        # r.dynamic_energy_adjustment_damping= 2.0
        audio= r.listen(source)
    
    try:
        print("RECOGANISING...")
        cmd=r.recognize_google(audio, language='en-in')
        print(cmd)

    except Exception as e:
        # print(e)
        # speek("I am not able to understand you")
        return "None"
    return cmd



def send_email(to,content):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("kaustubh6220@gmail.com","6072@@Th")
        server.sendmail("kaustubh6220@gmail.com",to,content)
        server.close()



def wikipedia_search(cmd1):
    speek("searching wikipedia")
    cmd1= cmd1.replace("wekipedia","")
    result=wikipedia.summary(cmd1, sentences =2)
    print(result)
    speek(result)



def open_drive(cmd3):

    cmd3=cmd.replace("drive"," ")

    if "C" in cmd3 or "c" in cmd3:
        os.startfile("C:")
        
    elif "D" in cmd3 or "d" in cmd3:
        os.startfile("D:")

    elif "E" in cmd3 or "e" in cmd3:
        os.startfile("E:")

    else:
        print("Wrong Input")



if __name__ == '__main__':
    wish()
    while True:
        cmd = reciver().lower()


        if "good morning" in cmd:
            speek("Good Morning Boss")
            # speek("What can i do fo you")

        elif "time" in cmd:
            time()


        elif "date" in cmd:
            date()


        elif "wikipedia" in cmd:
            wikipedia_search(cmd)


        elif ("open google" in cmd) or ("google" in cmd):
            run("Google Chrome")


        elif ("open youtube" in cmd) or ("youtube" in cmd):
            speek("opening youtube")
            webbrowser.open("youtube.com")


        elif ("open facebook" in cmd) or ("facebook" in cmd):
            speek("opening facebook")
            webbrowser.open("facebook.com")


        elif ("open instagram" in cmd) or ("instagram" in cmd):
            speek("opening instagram")
            webbrowser.open("instagram.com")


        elif "how are you" in cmd:
            list1=["I am fine boss I hope you are fine too ","i am doing good","ekdam mast"]
            a=(random.shuffle(list1))
            speek(list1[0])

    
        elif ("play music" in cmd) or ("play song" in cmd) :
            speek("Playing music from device")
            music_dir= "C:\\Users\\kaust\\Desktop\\pendrive\\MS"
            songs = os.listdir(music_dir)
            # list_song=[songs]
            random.shuffle(songs)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

            
        # elif ("change music") or "next" in cmd:
        #     speek("Changing Music")
        #     music_dir= "C:\\Users\\kaust\\Desktop\\pendrive\\MS"
        #     songs = os.listdir(music_dir)
        #     # list_song=[songs]
        #     random.shuffle(songs)
        #     # print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))
        

        elif "send email" in cmd:
            try:
                speek("whom do you want to send email")
                cmd1=reciver().lower()
                ans=cmd1
                email=dict_email.get(ans)
                # speek("whom should i send Email")
                to = email
                speek("what is the content")
                content= reciver()
                send_email(to,content)
                speek("Email has been sent successfully")
            except Exception as e:
                print(e)
                speek("sorry i am not able to send email, Please check your internet connection")
        

        elif "play" in cmd:
            cmd= cmd.replace("play"," ")
            pywhatkit.playonyt(cmd)
            print("Playing", cmd)


        elif "drive" in cmd:
            open_drive(cmd)


        elif "folder" in cmd:
            os.getcwd("TRIAL")


        elif "what is my memory status" in cmd :
            speek()
            
            
            # elif "get information" or "get info" in cmd:
        #     try:
        #         cmd3= cmd.replace("get information about"," ")
        #         result1=(pywhatkit.info(cmd3, lines=5))
        #         print(result1)
        #         speek(result1)
        #     except exception as e:
        #         print("I could not find any related info")
        
        elif ("open vs code" in cmd) or ("visual studio code" in cmd):
            run("visual Studio Code")

        




        
