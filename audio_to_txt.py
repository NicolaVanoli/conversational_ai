import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file
    print(r.recognize_google(audio,language="it-IT"))   # recognize speech using Google Speech Recognition
