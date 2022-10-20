# Behnam Baharmand
# A1: Simple Text Manipulation with Python
# Version 0.1.1

import string

inputFile = open("./A1/text.txt")
text = inputFile.read()


# 👩🏻‍🍳 Splits the text into sentences (returns an int.)
def sentence_chef(data):
    sentences = data.split(".")
    sentences.remove("")
    return len(sentences)


# 👨🏻‍🍳 Counts the words (returns an int.)
def word_chef(data):
    words = data.split()
    return len(words)


# Some adornments to prettify the output
print("\n► Simple Text Manipulation with Python:")
print("  ======================================")

# 1. Count how many sentences the text above contains and print out this information on the screen as an output (e.g., “This text contains X sentences”).
print(f"   This text contains {sentence_chef(text)} sentences.")


# 2. Count how many words the text above contains and print out this information on the screen as an output (e.g., “This text contains X words”).
print(f"   This text contains {word_chef(text)} words.\n")

# 3. Order all the sentences of the text according to their length (number of words per sentence) and print out this information on the screen as an output. It should be presented in the following order: the longest sentence first, the second longest thereafter and so on (e.g., ‘The longest sentence in this text contains “X” words”; The second longest sentence in this text contains “Y” words, …., and the shortest sentence in this text contains “Z” words’).

print("►► Sentences sorted by length:")

words_count = []
for sentence in text.split(". "):
    current_sentence = len(sentence.split())
    words_count.append(current_sentence)

words_count.sort(reverse=True)

for i in range(len(words_count)):
    if i == 0:
        print(f"   The first sentence contains {words_count[i]} words.")
    elif i == 1:
        print(f"   The second sentence contains {words_count[i]} words.")
    elif i == 2:
        print(f"   The third sentence contains {words_count[i]} words.")
    elif i == sentence_chef(text) - 1:
        print(f"   The last/shortest sentence contains {words_count[i]} words.")
    else:
        print(f"   The sentence #{i + 1} contains {words_count[i]} words.")

# 4. Extract five longest words in the entire text, create a List with those items and order them alphabetically. Print out these results on the screen (e.g., ‘Five longest words in this text ordered alphabetically are: “word1”,“word2”, “word3”, “word4”, “word5”’).
print("\n")
text = text.translate(str.maketrans("", "", string.punctuation))
all_words = text.split()
print("►►► The five longest words in this text ordered alphabetically are:")

if len(all_words) < 5:
    print("   There are fewer than 5 words in the text.")
else:
    all_words = list(dict.fromkeys(all_words))  # If repetitive words are not desirable
    all_words = sorted(all_words, key=len, reverse=True)
    fiveWords = sorted(all_words[:5:])

    for i in range(len(fiveWords)):
        if i < 5:
            print(f"   {fiveWords[i].capitalize()}")
