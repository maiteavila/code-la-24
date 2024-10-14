# Dictionary
word_frequencies = {}
word_frequencies["total"] = 0

# Words to skip
skip_words = {"the", "and", "of", "to", "in", "a", "that", "is", "it", "for", "on", "as", "with", "by"}

# Open the file
with open("hamlet.txt", "r") as file:
    for line in file:
        lowercase_line = line.lower() #Makes everything lowercase
        words = lowercase_line.split() #Split each line into words

        for word in words:

            # Skip words
            if word not in skip_words and word != '':
                # Update word frequency
                if word in word_frequencies:
                    word_frequencies[word] += 1
                else:
                    word_frequencies[word] = 1

# Update total word count
                word_frequencies["total"] += 1

# Sort the dictionary 
word_list = word_frequencies.items()
print('word_list')
print(word_list)

sorted_word_frequencies = sorted(word_list, key=lambda item: item[1], reverse=True) #Had my boyfriend help me with this. Essentially: key=lambda tells the loop to sort using the following commands.

# Print the top 10 most frequent words
print("Top 10 most frequent words:")
for i in range(1, 11):  # Skip the "total" key
    print(f"{sorted_word_frequencies[i][0]}: {sorted_word_frequencies[i][1]}")

# Display total word count
print(f"\nTotal word count: {word_frequencies['total']}")

#I was trying to remove the punctuation marks from the text. Not sure if tha affects results somehow, but I couldn't figure it out. 
#I'm also curious how to do this without the whole lambda key, because I really couldn't figure it out. :) 