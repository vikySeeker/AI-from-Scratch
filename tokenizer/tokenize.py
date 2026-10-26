from pathlib import Path
import re

Dataset_file_path: str = None

def load(filepath: str = None, train_data_count: int = 800) -> tuple:
    if not Path(filepath).is_file():
        print("Error: Invalid file path specified or file does not exist!")
        return
    
    global Dataset_file_path
    Dataset_file_path = filepath

    review = list()
    label = list()
    train_data = tuple()
    train_label = tuple()
    test_data = tuple()
    test_label = tuple()

    with open(Dataset_file_path, "r") as dataset:
        for data in dataset:
            lst = data.rstrip("\n").split("\t")
            if len(lst) == 2:
                review.append(lst[0])
                label.append(lst[1])
        
        train_data = review[0:train_data_count]
        test_data = review[train_data_count:]
        
        train_label = label[0:train_data_count]
        test_label = label[train_data_count:]

    return (train_data, train_label), (test_data, test_label)


    print(f"Dataset {Dataset_file_path} Loaded successfully!")

def _sample_output():
    for i in range(100):
        print(data[i])
    print(word_index)

def _clean_words(words: list) -> list:
    for i in range(len(words)):
        words[i] = re.sub(r'[^a-zA-Z0-9]', '', words[i]).lower()
    return words

def tokenize(data: tuple) -> tuple | int:
    if not data:
        print("Invalid Data provided!")
    
    tokenized_data = list()
    token_count = 0
    for line in data:
        line = line.lower()
        line = line.split(" ")
        line = _clean_words(line)            
        token_count += len(line)
        tokenized_data.append(line)

    return tuple(tokenized_data), token_count

def vocabularize(data: tuple) -> dict | int:
    if not data:
        print("Invalid token list provided!")
    word_index = dict()
    _word_idx = 1

    for token_list in data:
        for token in token_list:
            if token not in word_index:
                word_index[token] = _word_idx
                _word_idx += 1
    
    return word_index, len(word_index)

