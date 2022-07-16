from gtts import gTTS
from playsound import playsound
import os

text = 'dmd.'
tts = gTTS(text = text , lang='en')
tts.save("./tovoice.mp3")

fileName = "tovoice"
fileExtension = "mp3"

fullPath:str = fr"{os.getcwd()}/{fileName}.{fileExtension}".replace("\\", "/")
tts.save(fullPath)
playsound(fullPath)