vocabulary = None

def load_vocabulary(vocab: dict):
    if not vocab:
        print("Invalid Vocabulary data!")
        return
    
    global vocabulary
    vocabulary = vocab

def build_BoW(data: list) -> list:
    if not vocabulary:
        printf("Vocabulary is not initialized yet!")
        return None
    if not data:
        print("Invalid token data provided!")
        return None

    vector_list = list()
    for token_list in data:
        vector = list()
        seen = set()
        for token in token_list:
            if token in seen:
                continue
            seen.add(token)
            if token in vocabulary:
                vector.append(token_list.count(token))

        vector_list.append(vector)
    
    return vector_list