import pyttsx3 #pyttsx3 is a text-to-speech conversion library in Python.
import speech_recognition as sr
import webbrowser
import wikipedia
import os



engine = pyttsx3.init("sapi5") #Microsoft Speech API (sapi5) inbuilt voice jate nite pari

voices = engine.getProperty("voices")#Gets the current value of an engine property. #voice thake
# print(voices)
engine.setProperty('voice',voices[0].id)#for set voice proparty( propery set krte cai)
# print(voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()##Without this command, speech will not be audible to us.


def take_command():
       r = sr.Recognizer()
       with sr.Microphone() as source:
             r.adjust_for_ambient_noise(source, duration=1)
             print("Listening...")
             r.pause_threshold =1
             voice= r.listen(source)
             try:
                print("Recognizing..")
                command  = r.recognize_google(voice,language='en-bn') #Using google for voice recognition.
                command = command.lower()
                print(f"You Said : {command}\n")
             except:
                # print(e)
    
                print("say that again Please ")  #Say that again will be printed in case of improper voice
                return  None
    
             return  command

while True:
      command = take_command()
      
      if 'wikipedia' in command:
           speak("searching Wikipedia..")
           command = command.replace("wikipedia","") #blank remove wiki kre dibo
           results = wikipedia.summary(command,sentences = 4) #return 2 =sentence
           speak("According to wikipedia")
           print(results)
           speak(results)
    
      elif 'bored' in command:
                webbrowser.open("www.youtube.com/watch?v=6t1k2W_sxtU&list=RDemslA6Z69EQ&index=2")
    
      elif "lecture" in command:
                path ="G:\\term 3-2\\RSP"
                os.startfile(path)
      elif "thank you" in command:
          speak("You are Most Welcome")