import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

import os
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"


# Set up the GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')


# Set the device to use for input tensors
# device = torch.device("cuda")
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer
# Define the prompt for GPT-2
prompt = "What are the main topics discussed in the following text? \n"

# Define the text from which you want to extract main topics
text = "In this dialogue, the two speakers are discussing the opening hours of a bank and the process for blocking a credit card. Speaker 00 asks about the bank's opening hours and then asks for information about how to block their credit card, which has been stolen. Speaker 01 provides the bank's opening hours and instructs Speaker 00 on how to block their credit card by following certain instructions and identifying themselves. Speaker 00 thanks Speaker 01 and provides their name before ending the conversation."

# Tokenize the text and prompt
input_ids = tokenizer.encode(prompt + text, max_length=128, return_tensors='pt', truncation=True)

# Create an attention mask tensor
attention_mask = input_ids.ne(0).float()

# Set the pad_token_id and eos_token_id variables
pad_token_id = 128
eos_token_id = 128
print(pad_token_id)

# Move the input tensors to the GPU
# input_ids = input_ids.to(device)
# attention_mask = attention_mask.to(device)

# Move the model to the GPU
# model.cuda()

# Generate a summary of the main topics in the text using the GPT-2 model
summary, _ = model.generate(input_ids,attention_mask=attention_mask, max_length=2048, num_beams=5, temperature=1.0, pad_token_id=pad_token_id, eos_token_id=eos_token_id)

# Print the summary
print(tokenizer.decode(summary[0], skip_special_tokens=True))