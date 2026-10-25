from pathlib import Path
import re

Dataset_file_path: str = None

data = list()

word_index = dict()

_word_idx = 1

raw_word_count = 0
clean_word_count = 0
total_line_count = 0

def load(filepath: str = None):
    if not Path(filepath).is_file():
        print("Error: Invalid file path specified or file does not exist!")
        return
    
    global Dataset_file_path
    Dataset_file_path = filepath
    print(f"Dataset {Dataset_file_path} Loaded successfully!")

def _sample_output():
    for i in range(100):
        print(data[i])
    print(word_index)

def _clean_word(word: str) -> str:
    word = re.sub(r'[^a-zA-Z0-9]', '', word)
    return word.lower()


def _index_words(sentence: list):
    global raw_word_count
    global clean_word_count
    global _word_idx
    for word in sentence:
        raw_word_count += 1
        word = _clean_word(word)
        if word not in word_index:
            clean_word_count += 1
            word_index[word] = _word_idx
            _word_idx += 1

def run(delim: str = " "):
    print(f"Initializing the tokenization process with {Dataset_file_path}")
    with open(Dataset_file_path, "r") as reviews:
        for review in reviews:
            splitted_list = review.rstrip("\n").split(delim)
            splitted_list[0] = splitted_list[0].split(" ")
            data.append(tuple(splitted_list))
    
    print("Vocabularizing words...")
    global total_line_count
    for sentence in data:
        total_line_count += 1
        _index_words(sentence[0])
    print("\n\nTokenization Complete!")
    print(f"Total line count {total_line_count}")
    print(f"Total Word count {raw_word_count}")
    print(f"Unique word count {clean_word_count}")
    _sample_output()

