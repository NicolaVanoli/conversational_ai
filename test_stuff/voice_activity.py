# 1. visit hf.co/pyannote/segmentation and accept user conditions
# 2. visit hf.co/settings/tokens to create an access token
# 3. instantiate pretrained model
from pyannote.audio import Model
import sys
model = Model.from_pretrained("pyannote/segmentation", 
                              use_auth_token="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")


print(model.specifications)
sys.exit(0)
from pyannote.audio.pipelines import Resegmentation
HYPER_PARAMETERS = {
  # onset/offset activation thresholds
  "onset": 0.5, "offset": 0.5,
  # remove speech regions shorter than that many seconds.
  "min_duration_on": 0.0,
  # fill non-speech regions shorter than that many seconds.
  "min_duration_off": 0.0
}
pipeline = Resegmentation(segmentation=model)
pipeline.instantiate(HYPER_PARAMETERS)
vad = pipeline("C:/Users/nicol/Desktop/Personal/conversational_ai/customer1.wav")
print(vad)
# `vad` is a pyannote.core.Annotation instance containing speech regions
