import sys 
sys.argv

word_list = sys.argv
word_list.pop(0)

input_words = sys.argv[1:] 

# Filter the input to ensure the words exist in the dataset
valid_words = [word for word in input_words if word in word_list]

# Check if any valid words exist
if len(valid_words) == 0:
    print("None of the input words exist in the dataset.")
else:
    sorted_words = sorted(valid_words)
    print("Sorted words:", sorted_words)

