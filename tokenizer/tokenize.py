from pathlib import Path

Dataset_file_path: str = None

data = list()

def load(filepath: str = None):
    if not Path(filepath).is_file():
        print("Error: Invalid file path specified or file does not exist!")
        return
    
    global Dataset_file_path
    Dataset_file_path = filepath
    print(f"Dataset {Dataset_file_path} Loaded successfully!")

def run(delim: str = " "):
    print(f"Initializing the tokenization process with {Dataset_file_path}")
    with open(Dataset_file_path, "r") as reviews:
        for review in reviews:
            data.append(tuple(review.split(delim)))
    
    _sample_output()

def _sample_output():
    for i in range(100):
        print(data[i])


