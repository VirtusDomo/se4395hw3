#   Created by: James Anyabine
#   Homework 2: Word Guessing Game
#   Class: CS 4395 HLT
#   Professor: Dr. Karen Mazidi
#

import sys
import os
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


#Part 1
def reader(filepath):
    #print("\nUsing method 1")

    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        #text_in = f.read()
        lines = [line for line in f.readlines()]
    return lines

#Part 2
def process(text):
    lower = []
    #part a
    for i in range(len(text)):
        lower.append(text[i].lower())
    #part b and c and d
    nums = r'[0-9]'
    p = re.compile("[" + re.escape(string.punctuation) + "]")
    for i in range(len(lower)):
        lower[i] = lower[i].replace('--', ' ')
        lower[i] = re.sub(nums, '', lower[i])
        lower[i] = p.sub(' ', lower[i])
    return lower

#Part 3 and 4
def tokens(text):
    tokens = []
    unique = set()
    count, uni = 0, 0
    for i in range(len(text)):
        tokens.append(nltk.word_tokenize(text[i]))

    for i in range(len(tokens)):
        for j in range(len(tokens[i])):
            unique.add(tokens[i][j])
            count += 1
    for i in range(len(unique)):
        uni += 1

    print('Number of Unique Tokens:', uni)
    return tokens, count, unique

#Part 5 & 6
def importantDict(unique):
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in unique if not w in stop_words]
    print('Number of Important Words:', len(filtered))

    def importantTuple(word):
        ps = PorterStemmer()
        return (word, ps.stem(word))
    tup = []
    for w in unique:
        tup.append(importantTuple(w))
    print(tup)

    return tup

def dictWork(tups):
    return 0


def main():
    if len(sys.argv) > 1:
        rp = sys.argv[1]
        listed = reader(rp)
        l = process(listed)

        #Step 3, toke saved for step 11
        toke, tokecnt, unitoke = tokens(l)
        tups = importantDict(unitoke)


        #print(tokecnt)
        #print(listed[0].lower())
    else:
        print('Error, insufficient path please retry.')


if __name__ == '__main__':
    main()

