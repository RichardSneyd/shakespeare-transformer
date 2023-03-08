# read in the file to inspect
with open('text.txt', 'r', encoding='utf-8') as f: 
    text = f.read()

# how many characters?
#print("length of dataset in chars: ", len(text))

# let's look at the first 1000 chars
#print(text[:1000])

# get all unique characters 
chars = sorted(list(set(text)))
vocab_size = len(chars)
#print(''.join(chars))
#print('vocab_size' + str(vocab_size))p

# create a mapping from characters (string) to integers, then integer to character (string)
stoi = {ch:i for i,ch in enumerate(chars)}
itos = { i:ch for i,ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s] # encoder: encode string to integer list
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: decode integer list to

import torch
data = torch.tensor(encode(text), dtype=torch.long)
