'''
NOT PERFORMING VERY WELL

'''




import torch
from torch import TensorType, nn  
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("MilaNLProc/feel-it-italian-sentiment")

# Load the model, use .cuda() to load it on the GPU
model = AutoModelForSequenceClassification.from_pretrained("MilaNLProc/feel-it-italian-sentiment")

sentence = "non sono soddisfatto"
input_ids = tokenizer.encode(sentence)

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
positive, negative = proba
print(sentence)
print(f'Positive: {round(float(positive),3)} \nNegative: {round(float(negative),3)}')