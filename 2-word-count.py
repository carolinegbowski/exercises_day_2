
doc = "Hi my name is Caroline. Is Caroline. Caroline is my name. What is your name?"
import collections
from collections import Counter

def word_stats(doc, n):
    doc = doc.lower()
    doc = "".join((char if char.isalpha() or char in ("'", "-", "’") else " ") for char in doc)
    word_list = doc.split()
    counted_word_list = Counter(word_list)
    most_common_words = counted_word_list.most_common(n)
    for word, occurrence in most_common_words:
        print(word + ", " + str(occurrence))
    return


# word_stats(doc, 4)

with open("article.txt", "r") as f:
    words = f.read()
    word_stats(words, 10)

# getting s as an output -- from contractions perhaps?
# need to fix code here
# so that contractions stay, spaces and punctuation don't go to the list
