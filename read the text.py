import speech_recognition as sr
import pyperclip               # we have imported spch,pyperclip,pyttsx3
import pyttsx3
import win32com.client
Wshell = win32com.client.Dispatch("WScript.Shell")
Wshell.Sendkeys("",0)
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[5].id)
r=sr.Recognizer()
rdds='ok'
flag='0'
b='1'
while 1:
        with sr.Microphone() as source:
             try:
                audio=r.listen(source ,timeout=10.0)
                message=r.recognize_google(audio)
                if rdds in message:                                                           #what happens when rdds keyword is recognized
                   Wshell.AppActivate('Chrome')
                   Wshell.Sendkeys("^c",0)
                   print(message)
                   flag='1';
                if flag == b:
                   print('')
                   engine.say(pyperclip.paste())
                   engine.runAndWait()
                   flag='0'
             except sr.UnknownValueError:
                       engine.say('I didnt get you, what you said ?') 
                       engine.runAndWait()
             except sr.RequestError as e:
                       engine.say("SOME TECHINCAL ERROR; {0}".format(e))
                       engine.runAndWait()
               
