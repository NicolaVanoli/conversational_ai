import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
for i, el in enumerate(sr.Microphone.list_microphone_names()):
    # if 'Altopar' in el:
    print(i, el)