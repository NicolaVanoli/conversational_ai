import torch
from torch import TensorType, nn  
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("neuraly/bert-base-italian-cased-sentiment")

# Load the model, use .cuda() to load it on the GPU
model = AutoModelForSequenceClassification.from_pretrained("neuraly/bert-base-italian-cased-sentiment")

sentence = "a che ora apre la banca"
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

print(f'Positive: {round(float(positive),3)}\nNeutral: {round(float(neutral),3)} \nNegative: {round(float(negative),3)}')