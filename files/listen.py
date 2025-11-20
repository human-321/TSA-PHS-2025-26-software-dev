import speech_recognition as sr


listen_file = sr.AudioFile('assets\listen.wav')
r = sr.Recognizer()

r.recognize_ibm()

def startListening():
    with listen_file as source:
        audio = r.record(source)
