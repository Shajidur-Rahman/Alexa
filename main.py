import speech_recognition as sr
import pyttsx3
import datetime

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
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        # print(f"The current time is :{time}")
        talk(f"The current time is :{time}")

run_alexa()
