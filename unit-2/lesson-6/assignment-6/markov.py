import markovify

text = open("kamala.txt").read()

generator = markovify.Text(text)

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(140))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")

# Unit 2 Project Comments

# For my Unit 2 Project, I was thinking of scraping Taylor Swift song lyrics from different albums and use Markov chains to generate a "bonus song" for each album. I'd be interested to see what themes dominate her earlier albums in comparison to her most recent work and see if a Markov chain would be able to generate a song for each. 