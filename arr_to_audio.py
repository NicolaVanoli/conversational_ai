import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("out.wav") as source:
    audio_text = r.listen(source)
    print(audio_text)
    text = r.recognize_google(audio_text, language = "it-IT")

print(text)