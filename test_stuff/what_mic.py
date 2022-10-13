import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
for i, el in enumerate(sr.Microphone.list_microphone_names()):
    # if 'Altopar' in el:
    print(i, el)

# recognizer = sr.Recognizer()
# print('qusdadf')

# with sr.Microphone(device_index=1) as mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=0.05)
#             audio = recognizer.listen(mic)
#             # print(type(audio))
#             print(type(audio))
#             message = recognizer.recognize_google(audio, language="it-IT")
#             print(message)