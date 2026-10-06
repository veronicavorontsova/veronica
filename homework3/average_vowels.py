# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

def counting_vowels_and_consonants(string):
	vowels = "aeiouAEIOU"
	number_of_vowels = 0
	number_of_consonants = 0
	for i in string:
		if i.isalpha():
			if i in vowels:
				number_of_vowels +=1
			else: 
				number_of_consonants +=1
	return (number_of_vowels, number_of_consonants) 

def average_vowels_and_consonants(string):
	sentences = []
	i = 0
	for i in range(len(paragraph)):
		if paragraph[i] == ".":
			sentences.append(paragraph[:i+1])
			i+=1
	num_of_sentences = len(sentences)
	total_number_of_vowels = 0
	total_number_of_consonants = 0
	for i in sentences: 
		number_of_vowels, number_of_consonants = counting_vowels_and_consonants(i)
		total_number_of_vowels += number_of_vowels
		total_number_of_consonants += number_of_consonants 
	average_number_of_vowels = total_number_of_vowels/num_of_sentences
	average_number_of_consonants = total_number_of_consonants/num_of_sentences 
	return(num_of_sentences, average_number_of_vowels, average_number_of_consonants)

print(f"The paragraph has {counting_vowels_and_consonants(paragraph)[0]} vowels and {counting_vowels_and_consonants(paragraph)[1]} consonants.")
print(f"The paragraph has {average_vowels_and_consonants(paragraph)[0]} sentences. On average, each sentence has {average_vowels_and_consonants(paragraph)[1]} vowels and {average_vowels_and_consonants(paragraph)[2]} consonants.")