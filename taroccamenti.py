import json
from googletrans import Translator
from tqdm import tqdm
n = 436
# Open the JSON file for reading
# with open('banking77_prepared_valid_it.jsonl', 'r') as existing_it:
#     # Parse the JSON data into a Python dictionary
#     existing_data = [json.loads(line) for line in existing_it]

translator= Translator()
with open("transcriptions/tr_79.txt", "r") as f:
    with open("en_transcription.txt", "w") as new_f:
       
        with tqdm(desc='Building Test Set', total=222) as progress:
            for index,line in enumerate(f):
                try:
                    if index >= 0: 
                        print(line.split(':')[1])
                        
                        translation = translator.translate(line.split(':')[1], dest='en')
                        print(translation.text)
                        new_f.write(f"{line.split(':')[0]}: {translation.text}\n")
                        progress.update(1)
                        print('\n')
                except:
                    print(f'Could not translate line: {line}')
                    continue

