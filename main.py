import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import rotatescreen
import time
import pytz
import sys
import os
screen = rotatescreen.get_primary_display()
todo = list
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

contacts = dict

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
            else:
                sys.exit()
    except:
        talk("i could not understand at a moment. please try again")
        sys.exit()
    return command

def run_alexa():
    global time5
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time_india = pytz.timezone('Asia/Calcutta')
        time = datetime.datetime.now(time_india).strftime('%H:%M %p')
        talk('Current time is ' + time)
    elif 'what is' in command:
        information = command.replace("what is",'')
        info = wikipedia.summary(information,5)
        print(info)
        talk(info)
    elif 'tell me about' in command:
        information2 = command.replace("tell me about",'')
        info2 = wikipedia.summary(information2,10)
        print(info2)
        talk(info2)
    elif 'who is' in command:
        information3 = command.replace("who is",'')
        info3 = wikipedia.summary(information3,10)
        print(info3)
        talk(info3)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'jokes' in command:
        talk(pyjokes.get_jokes())
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info4 = wikipedia.summary(person, 1)
        print(info4)
        talk(info4)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relation ship with wifi')
    elif 'you are stupid' in command:
        talk('did you said me stupid , now see what i will do , i will screw up your pc')
        screen.rotate_to(270)
        screen.rotate_to(90)
        screen.rotate_to(180)
        talk('wanna say sorry')
        command = take_command()
        if 'sorry' in command:
            screen.rotate_to(0)
    elif 'who made you' in command:
        talk('i was developed by a greate man Avik , thanks to him for developing me')
    elif 'who do you like' in command:
        talk('of couse you but have to maintain a relationship with wifi')
    elif 'Do you love me' in command:
        talk('yes,of course i love you')
    elif 'boy or girl' and 'you' in command:
        talk('i am a girl')
    elif 'why your name is' in command:
        talk('my name is seven because my developers birthday comes and add up to seven and i was made on a date of seven. ')
    elif 'make a list' in command:
        talk('list sucessfully created. your list name is todo list')
        talk('tell what do want to add in this list,please one task at a time')
        command = take_command()
        task = command
        todo.append(task)
        todo
    elif 'message' in command:
        talk('tell person name')
        command = take_command()
        name = command.replace(' ','')
        print(name)
        if name not in contacts:
            save_number(name)
        final_name=contacts[name]
        talk('pls tell what message you want to send')
        command = take_command()
        message = command
        message = str(message)
        print(message)
        talk('pls tell time if want to send now tell now')
        command = take_command()
        time_tell = command
        print(command)
        if 'now' in time_tell:
            time1 = pytz.timezone('Europe/London')
            time2 = datetime.datetime.now().strftime('%H:%M')
            print(time2)
            time3 = time2
            time3 = time3.replace(':','')
            time4 = list(time3)
            print(time4)
            time5 = str(time4.pop(0))
            time5 = time5 + str(time4.pop(-3))
            time6 = str(time4.pop(-2))
            time6 = time6 + str(time4.pop(-1))
            print(time5)
            print(time6)
            time5 = int(time5)
            time6 = int(time6)
            time6 = 2+time6
        pywhatkit.sendwhatmsg(final_name,message,time5,time6)
        talk('pls log in to whatsapp web on your default browser and make sure you brouser is open')
    elif'add'and'list' in command:
        talk('want do you want to add')
        command = take_command()
        task = command
        todo.append(task)
        todo
    elif 'search' in command:
        talk('getting results from google')
        search = pywhatkit.search(command)
        talk(search)
    elif 'how' in command:
        talk('getting results from google')
        search = pywhatkit.search(command)
        talk(search)
    else:
        talk('Please say the command again.')

def save_number(name_of_person:object) -> None :
    talk("sorry i can't remember the conatct of the person can you tell me his contact number")
    command = take_command()
    command = command.replace(' ','')
    new_contact = command
    print(new_contact)
    digits = len(new_contact)
    print(digits)
    if digits > 10 or digits< 10 :
        talk('sorry the contact number is invald.please start again')
        sys.exit()
    str(new_contact)
    new_contact = '+91'+ new_contact
    contacts[name_of_person] = new_contact

run_alexa()

