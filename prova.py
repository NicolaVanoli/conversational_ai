import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
for i, el in enumerate(sr.Microphone.list_microphone_names()):
    # if 'Altopar' in el:
    print(i, el)

recognizer = sr.Recognizer()
print('qusdadf')

with sr.Microphone(device_index=33) as mic:
            print('quadf')
            recognizer.adjust_for_ambient_noise(mic, duration=0.05)
            print('qua')
            audio = recognizer.listen(mic)
            # print(type(audio))
            print(type(audio))
            message = recognizer.recognize_google(audio, language="it-IT")
            print(message)