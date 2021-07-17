import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
# voices = alexa.getProperty('voices')
# alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        # print(f"The current time is :{time}")
        talk(f"The current time is :{time}")
    elif 'play' in command:
        song = command.replace('play', '')
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        information = command.replace('tell me about', '')
        info = wikipedia.summary(information,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'exit' in command:
        exit()
    else:
        talk(f"I dont know about {command}. so I am searching google     ")
        pywhatkit.search(command)



while True:
    try:
        run_alexa()
    except:
        print("Please say again")
