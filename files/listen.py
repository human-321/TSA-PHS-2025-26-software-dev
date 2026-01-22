import speech_recognition as sr
#https://realpython.com/python-speech-recognition/


r = sr.Recognizer()



def getMicData(): #get mic data save to a file return file address
    return 'assets\listen.wav'

def decodeAudio():
    dataPath = getMicData()
    harvard = sr.AudioFile(dataPath)
    with harvard as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        audio = r.record(source)

    r.recognize_tensorflow(audio)

