import playsound
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='hr')
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)


speak('Svijetlo je upaljeno')
