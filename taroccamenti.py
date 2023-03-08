import json
from googletrans import Translator
from tqdm import tqdm
n = 436
# Open the JSON file for reading
# with open('banking77_prepared_valid_it.jsonl', 'r') as existing_it:
#     # Parse the JSON data into a Python dictionary
#     existing_data = [json.loads(line) for line in existing_it]

translator= Translator()
with open("banking77_prepared_valid.jsonl", "r") as f:
    with open("banking77_prepared_valid_it.jsonl", "w") as new_f:
        # for old_data in existing_data:


        #     json.dump(old_data, new_f,  ensure_ascii=False)
        #     new_f.write("\n")
        # del existing_data
        with tqdm(desc='Building Test Set', total=9003-n) as progress:
            for index,line in enumerate(f):
                try:
                    if index > 56:
                        line = json.loads(line)
                        data = line['prompt'].replace('\n\n###\n\n','')
                        print(data)
                        translation = translator.translate(data, dest='it')
                        line['prompt'] = str(translation.text) + "\n\n###\n"
                        json.dump(line, new_f, ensure_ascii=False)
                        new_f.write("\n")
                        print(line)
                        progress.update(1)
                        print('\n')
                except:
                    print(f'Could not translate line: {line}')
                    continue

