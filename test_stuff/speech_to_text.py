# 1. visit hf.co/pyannote/segmentation and accept user conditions
# 2. visit hf.co/settings/tokens to create an access token
# 3. instantiate pretrained speaker segmentation pipeline
import ctypes, sys
import time

from pyannote.audio import Pipeline
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# if is_admin():
#     pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
#                                     use_auth_token="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")
#     # pipeline = Pipeline.from_pretrained("pyannote/speaker-segmentation")
#     output = pipeline("customer.wav",num_speakers=2)

#     for turn, _, speaker in output.itertracks(yield_label=True):
#         # speaker speaks between turn.start and turn.end
#         print(turn,_,speaker)
#     time.sleep(20)
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# 1. visit hf.co/pyannote/speaker-diarization and hf.co/pyannote/segmentation and accept user conditions (only if requested)
# 2. visit hf.co/settings/tokens to create an access token (only if you had to go through 1.)
# 3. instantiate pretrained speaker diarization pipeline





from pyannote.audio import Pipeline
if is_admin():

    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",use_auth_token="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")

    # 4. apply pretrained pipeline
    diarization = pipeline("C:/Users/nicol/Desktop/Personal/conversational_ai/test_event.wav", num_speakers=2)
    # with open("./conversational_ai/audio.rttm", "w") as rttm:
    #     diarization.write_rttm(rttm)
    # 5. print the result
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
    # start=0.2s stop=1.5s speaker_0
    # start=1.8s stop=3.9s speaker_1
    # start=4.2s stop=5.7s speaker_0
    # ...
    time.sleep(100)

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
