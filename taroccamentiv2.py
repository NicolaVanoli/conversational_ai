import json,re

with open("banking77_prepared_valid_it.jsonl", "r") as f:
    with open("banking77_prepared_valid_it1.jsonl", "w") as new_f:
        for line in f:

            new_line = line.replace(f'"completion": " ', f'"completion": "')

            new_f.write(new_line)
            