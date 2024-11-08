import markovify  # Import the Markovify library for text generation

# Load text for TTPD album
text = open("ttpd-songs.txt").read() 

# Create a Markov model using the text, setting state_size to 2 for optimized coherence
generator = markovify.Text(text, state_size=2, well_formed=False) # well_formed = False allows for more diverse sentence structures

# Generate a paragraph with 10 sentences for the TTPD album
paragraph = ""  # Empty string to store generated paragraph
for i in range(10):  # Loop 10 times to generate 10 sentences
    paragraph += str(generator.make_short_sentence(390))  # Generate a short sentence with max length of 390 characters and add to paragraph
    paragraph += " "  # Add a space after each sentence

# Print the generated paragraph
print("\n\n\n")  # Print new lines 
print(paragraph)  # Print the generated paragraph for TTPD album
print("\n\n\n")  # Print new lines 

#Same thing for Debut album
text = open("debut-songs.txt").read() 

generator = markovify.Text(text, state_size=2, well_formed=False)

paragraph = ""  
for i in range(10): 
    paragraph += str(generator.make_short_sentence(300))  
    paragraph += " "

print("\n\n\n") 
print(paragraph)  
print("\n\n\n")  
