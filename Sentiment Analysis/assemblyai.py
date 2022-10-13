from email.mime import application
import json
from urllib import response
import requests
import time

import os,sys 
print(os.getcwd())



upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

def upload_file(audio_file, header):
    upload_response = requests.post(
        upload_endpoint,
        headers=header, data=_read_file(audio_file)
    )
    return upload_response.json()

def _read_file(filename, chunk_size=5242880):
    with open(filename, "rb") as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def request_transcript(upload_url, header):
    transcript_request = {
        'audio_url': upload_url
    }
    transcript_response = requests.post(
        transcript_endpoint,
        json=transcript_request,
        headers=header
    )
    return transcript_response.json()


def make_polling_endpoint(transcript_response):
    polling_endpoint = "https://api.assemblyai.com/v2/transcript/"
    polling_endpoint += transcript_response['id']
    return polling_endpoint

def wait_for_completion(polling_endpoint, header):
    while True:
        polling_response = requests.get(polling_endpoint, headers=header)
        polling_response = polling_response.json()

        if polling_response['status'] == 'completed':
            break

        time.sleep(5)

def get_paragraphs(polling_endpoint, header):
    paragraphs_response = requests.get(polling_endpoint + "/paragraphs", headers=header)
    paragraphs_response = paragraphs_response.json()

    paragraphs = []
    for para in paragraphs_response['paragraphs']:
        paragraphs.append(para)

    return paragraphs

api_key = 'd5873d5d3d694e9d879d0b6bc7351244'

header = {
	'authorization': api_key,
	'content-type': 'application/json'
}

upload_file('Sentiment Analysis/customer.wav', header)
transcript_response = request_transcript('customer.wav', header)
polling_endpoint = make_polling_endpoint(transcript_response)
wait_for_completion(polling_endpoint, header)
paragraphs = get_paragraphs(polling_endpoint, header)


with open('transcript.txt', 'w') as f:
	for para in paragraphs:
		print(para['text'] + '\n')
		f.write(para['text'] + '\n')