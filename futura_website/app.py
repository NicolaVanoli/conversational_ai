from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import uvicorn
import json
from os import listdir
from os.path import isfile, join
import torch
from torch import TensorType, nn
import os.path
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/transcriptions")
def get_transcriptions():
    onlyfiles = [f for f in listdir("C:/Users/nicol/Desktop/Personal/conversational_ai/transcriptions") if isfile(
        join("C:/Users/nicol/Desktop/Personal/conversational_ai/transcriptions", f)) and 'txt' in f and '_' in f]
    return Response(json.dumps(jsonable_encoder(onlyfiles)), status_code=status.HTTP_200_OK)


@app.put("/open_transcription/{id}")
def open_transcription(id: int):
    with open("C:/Users/nicol/Desktop/Personal/conversational_ai/transcriptions/tr_" + str(id) + ".txt", 'r') as f:
        lines = f.readlines()

    # text = f.read(f)
    # print(text)
    # return Response(json.dumps(jsonable_encoder(text)), status_code=status.HTTP_200_OK)
    return Response(json.dumps(jsonable_encoder(lines)), status_code=status.HTTP_200_OK)


@app.put("/predict_sentiment/{id}")
def predict_sentiment(id: int):
    tokenizer = AutoTokenizer.from_pretrained(
        "neuraly/bert-base-italian-cased-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained(
        "neuraly/bert-base-italian-cased-sentiment")

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
            'positive': round(float(positive), 3),
            'neutral': round(float(neutral), 3),
            'negative': round(float(negative), 3)
        }


    with open('C:/Users/nicol/Desktop/Personal/conversational_ai/transcriptions/tr_' + str(id) + '.txt') as f:
        lines = f.readlines()

    pos = []
    neu = []
    neg = []

    predictions = []

    for line in lines:
        line = re.sub("[\(\[].*?[\)\]]", "", line).lstrip()
        if line.startswith('User'):
            prediction = predict_sentence(line)
            pos.append(prediction['positive'])
            neu.append(prediction['neutral'])
            neg.append(prediction['negative'])
            predictions.append(f'\n{line}\n{prediction}\n\n')

    pos = sum(pos)/len(pos)
    neu = sum(neu)/len(neu)
    neg = sum(neg)/len(neg)

    return Response(json.dumps(jsonable_encoder(predictions)), status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    uvicorn.run(app, port=6655)

    # go to http://127.0.0.1:6655/docs
