import soundcard as sc
import soundfile as speech
import speech_recognition 

OUTPUT_FILE_NAME = "assemblyai-and-python-in-5-minutes/customer.wav"    # file name.
SAMPLE_RATE = 48000              # [Hz]. sampling rate.
RECORD_SEC = 10        # [sec]. duration recording audio.


    

print(sc.get_microphone(id='Microfono (USB Audio Device)', include_loopback=True))
with sc.get_microphone(id='Microfono (USB Audio Device)', include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
    # record audio with loopback from default speaker.
    data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
    
    # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    speech.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
    r = speech_recognition.Recognizer()
    with speech_recognition.WavFile("assemblyai-and-python-in-5-minutes/customer.wav") as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file
        # print(r.recognize_google(audio,language="it-IT"))   # recognize speech using Google Speech Recognition
