import json
import csv


with open('intents_gtts.json', encoding='utf-8') as fh:
    data = json.load(fh)


print(len(data['intents']))

with open('testtessdft.csv', 'w', encoding='UTF8') as f:
    
    writer = csv.writer(f, lineterminator = '\n')
    writer.writerow(['text','intent'])
    for el in data['intents']:
        for pattern in el['patterns']:
            writer.writerow([pattern,el['tag']])

