vocabulary = None

# Loads the vocabulary for the bag of words model to utilize

def load_vocabulary(vocab: dict):
    if not vocab:
        print("Invalid Vocabulary data!")
        return
    
    global vocabulary
    vocabulary = vocab

# builds a bag of words vector from the given list of training dataset
# the training data passed is in the format of nested list tokens
# this will return a nested list of vectors where it frequency of each word is
# the vector is padded with 0 to match the length of the longest sentence list.  

def build_BoW(data: list, padding: str = None) -> list:
    if not vocabulary:
        printf("Vocabulary is not initialized yet!")
        return None
    if not data:
        print("Invalid token data provided!")
        return None

    vector_list = list()
    padding_length = 0
    if padding != None:
        longest_list = max(data, key=len)
        padding_length = len(longest_list)
        
    for token_list in data:
        vector = list()
        vector_len = 0
        seen = set()
        for token in token_list:
            if token in seen:
                continue
            seen.add(token)
            if token in vocabulary:
                vector.append(token_list.count(token))
        vector_len = len(vector)
        if padding == 1 and vector_len < padding_length:
            needed = padding_length - vector_len
            vector.extend([0] * needed)

        vector_list.append(vector)
    
    return vector_list