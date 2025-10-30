


# # python3 -m piper.download_voices en_US-lessac-medium
import os
import winsound
import wave

from piper import PiperVoice


baseWavName = "wahwahstopreadingthisSpAmSpAm_b.wav"
voice = PiperVoice.load("assets\\en_US-lessac-medium.onnx" , "assets\\en_US-lessac-medium.onnx.json")

def speak(words):
    wavName = baseWavName

    with wave.open(wavName, "wb") as wav_file:
        voice.synthesize_wav(words, wav_file)
    
    winsound.PlaySound(wavName,winsound.SND_FILENAME)

    if os.path.exists(wavName):
        os.remove(wavName)
    


