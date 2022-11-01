# Behnam Baharmand
# A2: Text Manipulation and Processing with Python
# Version 0.1.0

# Import libraries
import re
import string
from collections import Counter
import goodies

### 1. Acquire the content
file_name = "./A2/Sapir1921_chapter1.txt"  # Sapir1921_chapter1.txt
theBookContent = open(file_name).read()
# theBookContent = theBook.read()

theStopWords = open("./A2/stopwordlist.txt")
sw_list = theStopWords.read()

# Function Defenitions @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Turns a str into a list
def sentence_chef(data):
    sentences = data.split(".")
    return sentences


# Returns the longest word from a list
def get_longest_word(all_words):
    all_words = list(dict.fromkeys(all_words))  # Repetitive words are NOT desirable
    all_words = sorted(all_words, key=len, reverse=True)
    longestWord = sorted(all_words[:1:])
    return longestWord[0]


# Returns a list containing all the words w/o punctuations
def get_all_words():
    text = theBookContent.translate(str.maketrans("", "", string.punctuation))
    return text.split()


# Removes stop words from a list
def rem_stop_words(list):
    list = [x.lower() for x in list]
    split_text_no_sw = [word for word in list if word not in sw_list]
    return split_text_no_sw


# Just for aesthetic purposes @-}
goodies.echo_badge()

### 2. Extract the longest sentence. =====================================

sentence_list = sentence_chef(theBookContent)
length_of_sentence = [len(i) for i in sentence_list]
longest_sentence = sentence_list[
    length_of_sentence.index(max(length_of_sentence))
].replace("\n", "")

print(f"\n▐░░ The longest sentence in {file_name} is:\n\n {longest_sentence}.")

### 3. Find the longest word. ============================================
# Please refer to the Project Report for more info on this methodology.
# TL;DR: The aim was to replicate a behaviour similar to online tools like:
# https://tools.randomcodez.com/find-longest-word
goodies.insert_new_segment()

all_words = theBookContent.split()

print(f'▐░░ Here is the longest word: "{get_longest_word(all_words)}"')

### 4. Extract the top 10 most frequent words. ===========================
goodies.insert_new_segment()
split_text = get_all_words()

counters = Counter(rem_stop_words(split_text))
most_freq = counters.most_common(10)
print(f"▐░░ The top 10 most frequent words are:\n\n{most_freq}")

### 5. Extract the named entities. =======================================
goodies.insert_new_segment()

target_capitalised_words = [
    x.strip() for x in re.findall(r"\b[A-Z][a-zA-Z]*\b", theBookContent)
]

named_entities = rem_stop_words(target_capitalised_words)
named_entities = [ne.capitalize() for ne in named_entities]

list_a = []
list_b = []

for i in named_entities:
    L = list_a if i[0].lower() < "m" else list_b
    L.append(i)

print("▐░░ Selected named entities are:\n")
print(f"From A-L ⬇️\n\n{sorted(list_a)}\n")
print(f"From M-Z ⬇️\n\n{sorted(list_b)}")
