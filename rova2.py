import pyaudio

import soundcard as sc
import soundfile as sf

OUTPUT_FILE_NAME = "test.wav"    # file name.
SAMPLE_RATE = 48000              # [Hz]. sampling rate.
RECORD_SEC = 3        # [sec]. duration recording audio.


import numpy
import speech_recognition as sr

def pyaudio_play(data, rate=44100):
    ''' Send audio array to pyaudio for playback
    '''
    import pyaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=rate, output=1)
    stream.write(data.astype(numpy.float32).tobytes())
    stream.close()
    p.terminate()
    print(type(stream))
  
    r = sr.Recognizer()
            # use "test.wav" as the audio source
    audio = r.record(stream)                        # extract audio data from the file
    try:
        print("Transcription: " + r.recognize_google(audio,language="it-IT"))   # recognize speech using Google Speech Recognition
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
    # record audio with loopback from default speaker.
    data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
    print(data[:, 0])

    pyaudio_play(data)
    sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
    
    


def generate_sample(self, ob, preview):
    print("* Generating sample...")
    tone_out = array(ob, dtype=int16)

    if preview:
        print("* Previewing audio file...")

        bytestream = tone_out.tobytes()
        pya = pyaudio.PyAudio()
        stream = pya.open(format=pya.get_format_from_width(width=2), channels=1, rate=OUTPUT_SAMPLE_RATE, output=True)
        stream.write(bytestream)
        stream.stop_stream()
        stream.close()

        pya.terminate()
        print("* Preview completed!")
    else:
        write('sound.wav', SAMPLE_RATE, tone_out)
        print("* Wrote audio file!")