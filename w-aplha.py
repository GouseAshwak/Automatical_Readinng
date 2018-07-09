import wolframalpha
import wikipedia
import win32com.client as wincl
import speech_recognition as sr
x=1
speak = wincl.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
print('hello I am your AI assisatnt  you can call me:InFii.')
print('How can i help you ?')
speak.Speak("hello I'm your AI assistant you can call me:Infii")
speak.Speak('   ')
speak.Speak('How can i help you ?')
speak.Speak('   ')
while(x==1):
     with sr.Microphone() as source:
         print('YOUR FRIEND INFI IS READY TO HELP ')
         print('DO YOU WANT ANY THING TO KNOW ?')
         speak.Speak('YOUR FRIEND Infii IS READY TO HELP')
         speak.Speak('')
         speak.Speak('DO YOU WANT ANY THING TO KNOW ? ')
         audio = r.listen(source)
         try:
             inpu = r.recognize_google(audio)
             print(inpu)
             speak.Speak(inpu)
             
             try:
                 #wolframalpha
                  client=wolframalpha.Client("3X3HLW-Y2QV7J2VTH")
                  res=client.query(inpu)
                  answer=next(res.results).text
                  print(answer)
                  speak.Speak(answer)
                  speak.Speak("            ")
               
             except:
                    #wikipedia
                    print(wikipedia.summary(inpu,sentences=3))
                    speak.Speak(wikipedia.summary(inpu,sentences=3))
                    
         except sr.UnknownValueError:
                 print("Infii could not understand audio")
                 speak.Speak("Infii could not understand audio") 
                 
         except sr.RequestError as e:
                   speak.Speak("Could not request results from Google ; {0}".format(e))
                   
                   print("Could not request results from Google ; {0}".format(e))



                       
