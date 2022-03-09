import gtts
from playsound import playsound
import json
import os

data = ['en']


def start(data):
    choices = ['language', 'message', 'history']

    initialMessage = print('''welcome to this simple tts made with python! \n \n These are your initial choices:
    \n 1.   Choose language (default = en)
    \n 2.   What message do you want to be read out? select this option to write a new message!
    \n 3.   Your saved previous tts messages saved in folder.''')

    choice = input('\n What do you want to do?: ')

    if choice == '1':
        language(data)

    elif choice == "2":
        speech(data)

    elif choice == '3':
        files()

    else:
        start(data)


def language(data):
    lang = input(
        'What language do you want your tts to be in? (type 2 for list of avaliable languages)')

    if lang == "2":
        dictArr = []
        dictArr.append(gtts.lang.tts_langs())

        print(json.dumps(dictArr, sort_keys=False, indent=4))

        languageChoice = input('Please type in the language code you want:   ')
        data[0] = languageChoice

        speech(data)
        start(data)


def speech(data):

    message = input("Your message:  ")
    tts = gtts.gTTS(message, lang=data[0])

    ttsName = message[0:10] + ".mp3"
    tts.save(ttsName)

    playsound(ttsName)


def files():
    prevFiles = []
    for file in os.listdir('./'):
        if file.endswith(".mp3"):
            os.path.join('    ', file)


start(data)
