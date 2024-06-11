# import gtts
# from playsound import playsound
# import googletrans

# print(googletrans.LANGUAGES)
# a = gtts.gTTS("rakesh tu pizza ni pejya ta main tera kaam ni krna",lang="hi")

# a.save("myfile.mp3")
# playsound("myfile.mp3")




import pyttsx3
import speech_recognition as sp


def speak(audio):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty("voice",voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r=sp.Recognizer()
    with sp.Microphone() as source:
        print("listening...")
        speak("listening")

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en')
        print(f"user said:{query}")
    except:
        print("say that again")
        speak("say that again")
        return "None"
    return query

while True:
    query=take_command().lower()
    if "hello" in query:
        speak("Hello dear! How can I help you")
    