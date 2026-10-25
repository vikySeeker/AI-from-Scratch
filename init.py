from tokenizer import tokenize as tz

# Specify the dataset file path 
Dataset_file_path = "./dataset/amazon_cells_labelled.txt"

tz.load(Dataset_file_path)

tz.run("\t")