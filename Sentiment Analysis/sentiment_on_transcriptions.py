import torch
from torch import TensorType, nn  
import os.path
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("neuraly/bert-base-italian-cased-sentiment")

# Load the model, use .cuda() to load it on the GPU
model = AutoModelForSequenceClassification.from_pretrained("neuraly/bert-base-italian-cased-sentiment")


def predict_sentence(sentence: str) -> dict:
    input_ids = tokenizer.encode(sentence, add_special_tokens=False)

    # Create tensor, use .cuda() to transfer the tensor to GPU
    tensor = torch.tensor(input_ids).long()
    # Fake batch dimension
    tensor = tensor.unsqueeze(0)

    # Call the model and get the logits
    # logits, = model(tensor)
    logits = model(tensor).logits

    # Remove the fake batch dimension
    logits = logits.squeeze(0)

    # The model was trained with a Log Likelyhood + Softmax combined loss, hence to extract probabilities we need a softmax on top of the logits tensor
    proba = nn.functional.softmax(logits, dim=0)

    # Unpack the tensor to obtain negative, neutral and positive probabilities
    negative, neutral, positive = proba
    # print(sentence)
    # print(f'Positive: {round(float(positive),3)}\nNeutral: {round(float(neutral),3)} \nNegative: {round(float(negative),3)}')
    return {
        'positive':round(float(positive),3),
        'neutral': round(float(neutral),3),
        'negative': round(float(negative),3)
    }


with open(os.path.dirname(__file__) +'/../transcriptions/tr_22.txt') as f:
    lines = f.readlines()

pos = []
neu = []
neg = []

for line in lines:
    line = re.sub("[\(\[].*?[\)\]]", "", line).lstrip()
    if line.startswith('User'):
        prediction = predict_sentence(line)
        pos.append(prediction['positive'])
        neu.append(prediction['neutral'])
        neg.append(prediction['negative'])
        print(f'\n{line}\n{prediction}\n\n')

pos = sum(pos)/len(pos)
neu = sum(neu)/len(neu)
neg = sum(neg)/len(neg)

print(f'FINAL\npositiv{pos}\nneutral{neu}\nnegative{neg}')