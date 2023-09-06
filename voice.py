import pyttsx4
from comtypes.client import CreateObject
from comtypes.gen import SpeechLib


def say(text: str):
    engine = pyttsx4.init()
    engine.say(text)
    engine.runAndWait()

def read_file():
    voice = CreateObject('SAPI.SpVoice')
    stream = CreateObject('SAPI.SpFileStream')
    outFile = 'voice.wav'
    stream.open(outFile, SpeechLib.SSFMCreateForWrite)
    voice.AudioOutputStream = stream
    inFile = 'voice.txt'
    with open(inFile, 'r', encoding='utf-8') as f:
        text = f.read()
    voice.speak(text)
        

if __name__ == '__main__': 
    say('你好！今天天气真好...')
    # read_file()
