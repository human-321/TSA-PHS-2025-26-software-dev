

# # python3 -m piper.download_voices en_US-lessac-medium
import os
import winsound
import wave

from piper import PiperVoice


baseWavName = "wahwahstopreadingthisSpAmSpAm_b.wav"
voice = PiperVoice.load("assets\\en_US-lessac-medium.onnx" , "assets\\en_US-lessac-medium.onnx.json")

def speak(words):
    print("speaking the following words: fuck you")
    wavName = baseWavName

    with wave.open(wavName, "wb") as wav_file:
        voice.synthesize_wav(words, wav_file)
    
    winsound.PlaySound(wavName,winsound.SND_FILENAME)
    
    if os.path.exists(wavName):
        os.remove(wavName)
    
def help():
    speak("""
          hello this is the audio-visual disablity helper; the top button (the one you clicked) is the help button
          the 1st button on the second row is the mic transcriptor, it turns on your mic and transcripts it to the textbox to its side
          the 2nd button on the 2nd row is the file transcriptor, it still transcripts but you select the file instead of your mic
          the button on the last row is the speaker button, it will speak any words typed in the typebox to its side
          """)
