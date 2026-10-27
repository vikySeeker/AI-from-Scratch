from tokenizer import tokenize as tz
from tokenizer import BoW as bw

# Specify the dataset file path 
Dataset_file_path = "./dataset/amazon_cells_labelled.txt"

(train_data, train_label), (test_data, test_label) = tz.load(Dataset_file_path)     # loading training and test data to process.

print(f"Total lines in data {len(train_data)}")

print("Tokenizing the training data...")

tokens, tok_count = tz.tokenize(train_data)     # tokenizing the data

print(f"Total tokens: {tok_count}")

print("Vocabularizing the tokens...")

vocabulary, vocab_size = tz.vocabularize(tokens)    # generating vocabulary with the given set of tokens

print(f"Total Vocabularies {vocab_size}")

print(f"Building Bag of Words vector...")

bw.load_vocabulary(vocabulary)                      # loading vocabulary to the bag of words model
vector = bw.build_BoW(tokens, padding=1)            # bag of words vector building

print(f"Vector built successfully!\n")