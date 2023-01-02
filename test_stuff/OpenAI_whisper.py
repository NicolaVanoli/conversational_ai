import whisper
import soundcard as sc
import soundfile as speech
import speech_recognition 


OUTPUT_FILE_NAME = "customer.wav"    # file name.
SAMPLE_RATE = 48000              # [Hz]. sampling rate.
RECORD_SEC = 10        # [sec]. duration recording audio.

model1 = whisper.load_model("small") # can choose "medium" or "large"
    

print(sc.get_microphone(id='Microfono (USB Audio Device)', include_loopback=True))
with sc.get_microphone(id='Microfono (USB Audio Device)', include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
    # record audio with loopback from default speaker.
    data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
    speech.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
    r = speech_recognition.Recognizer()
    with speech_recognition.WavFile(OUTPUT_FILE_NAME) as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file
        print(r.recognize_google(audio,language="it-IT"))   # recognize speech using Google Speech Recognitio
    out = model1.transcribe(OUTPUT_FILE_NAME,language="it")
    print('*'*50)
    print(out['text'])




