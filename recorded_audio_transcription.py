import pydub
import whisper
import os, sys
from pyannote.audio import Pipeline
from pydub.playback import play
import numpy as np

import os
# os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
wav_file = 'event_10_01.wav'
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token="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")


# apply the pipeline to an audio file
diarization = pipeline(wav_file, num_speakers=2)

# dump the diarization output to disk using RTTM format
with open("tmp_audio.rttm", "w") as rttm:
    diarization.write_rttm(rttm)


model = whisper.load_model("medium")

def apply_function_to_rttm_segments(rttm_file, wav_file, func):
    # Load the .wav file
    audio = pydub.AudioSegment.from_wav(wav_file)

    # Parse the RTTM file
    results = []
    with open(rttm_file, 'r') as f:
        for line in f:
            
            # return
            # Extract the relevant information from the RTTM file line
            fields = line.strip().split()
            type_ = fields[0]
            if type_ != "SPEAKER":
                continue  # Skip non-speech segments
            speaker_id = fields[7]
            start_time = float(fields[3])
            end_time = start_time + float(fields[4])
            

            # Extract the audio data for this segment from the .wav file
            start_time_ms = int(start_time * 1000)
            end_time_ms = int(end_time * 1000)
            segment_audio = audio[start_time_ms:end_time_ms]

           
            # Store the segment information and audio data
            # play(segment_audio)

            segment_audio.export('tmp_segment_audio.wav', format='wav')
            # play(segment_audio)
            result = func()
            results.append({
                'speaker': speaker_id.replace('SPEAKER_0','UTENTE_'),
                'transcript': result,
                'start': round(start_time,2),
                'end': round(end_time,2),

            })

    
    os.remove('tmp_segment_audio.wav')
    os.remove('tmp_audio.rttm')
    return results


def my_function():
    # print(audio)
    # return
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio('tmp_segment_audio.wav')
    
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    # Only consider the probability of the Italian language

    # print(probs)
    print(f"Detected language: {max(probs, key=probs.get)}")
    if max(probs, key=probs.get) == 'it':


        # decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)
        
        # Do something with the audio data
    

        return result.text
    else: return 'NOT ITALIAN'







results = apply_function_to_rttm_segments(
    'tmp_audio.rttm', wav_file, my_function)
# print(results)

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + "_" + str(counter)  + extension
        counter += 1
    print(path)
    return path

# open a (new) file to write
call_to_text = open(uniquify("transcriptions/tr.txt"), "w")



for el in results: 
    call_to_text.write(f"{el['start']}->{el['end']}, {el['speaker']}: {el['transcript']}\n")
    print(f"{el['start']}->{el['end']}, {el['speaker']}: {el['transcript']} \n")

call_to_text.close()