# Import Module
import os
import sys 
import re 
import nltk

# Folder Path
path = "C:/Users/nicol/Desktop/Personal/conversational_ai/transcriptions"

# Change the directory
os.chdir(path)

# Read text File

data = []

def read_text_file(file_path):
	with open(file_path, 'r') as f:
		return  [re.sub("[\(\[].*?[\)\]]", "", line.rstrip().replace('User:','')).lstrip() for line in f if 'Bot:' not in line]
		# print(f.read())
# iterate through all file

for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{path}\{file}"

		# call read text file function
		data.append(read_text_file(file_path))

data = [item for sublist in data for item in sublist]
data = ' '.join(data)

allWords = nltk.tokenize.word_tokenize(data)
stopwords = nltk.corpus.stopwords.words('italian')

cleanWorlds  = []
for el in allWords:
	if el not in stopwords:
		cleanWorlds.append(el)

allWordDist = nltk.FreqDist(w.lower() for w in cleanWorlds)
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in cleanWorlds)  



mostCommon= allWordDist.most_common(10)
print(mostCommon)
