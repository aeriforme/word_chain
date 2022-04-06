# start from a selected word
# create the set of anagrams
# create the set of words that differ by 1 letter
# create the set of semantically affine words
# randomly select 1 word from the 3 sets
# do the same for the new word until you have ~10 words 


import numpy as np 
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import re
import string
import nltk
from nltk.corpus import stopwords, wordnet
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
nltk.download('wordnet')
nltk.download('omw-1.4')

f = open('words_dictionary.json')
english_words = (json.load(f)).keys()

# '/usr/share/dict/american-english'


def get_anagrams(source, dictionary):
    d = defaultdict(list)
    sorted_source = "".join(sorted(source))
    for word in dictionary:
        key = "".join(sorted(word))
        if key == sorted_source:
            d[key].append(word)
    for key, anagrams in d.items():
        return list(anagrams)
    
def synonym_antonym_extractor(phrase):

     synonyms = []
     antonyms = []

     for syn in wordnet.synsets(phrase):
          for l in syn.lemmas():
               synonyms.append(l.name())
               if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())

     return list(synonyms), list(antonyms)    



seed = 'fabrication'
words = [seed, ]
chain_length = 10 

i = 0

while i < chain_length:
    
    options = []
    
    #_________________________________________________________________________
    # ANAGRAMS
    print('***********************')
    anagrams = get_anagrams(words[i], english_words)
    print(anagrams)
    if anagrams is not None : options.append(list(anagrams))
    #_________________________________________________________________________
    # 1 DIFFERENT LETTER      
    print('***********************')
    one_diff_letter = [w for w in english_words if (len(w)==len(words[i])) and (sum(a!=b for a,b in zip(words[i],w)) == 1)]
    print(one_diff_letter)
    if len(one_diff_letter)>0:  options.append(list(one_diff_letter))
    #_________________________________________________________________________
    # ONE ADDITIONAL IN FRONT OR AT THE END 
    print('***********************')     
    one_more_letter = [w for w in english_words if (((words[i] in w) or (w in words[i])) and (abs(len(w)-len(words[i])) == 1)) ]
    print(one_more_letter)
    if len(one_more_letter)>0: options.append(list(one_more_letter))
    # SYNONYMS & ANTONYMS
    print('syn & ant ***********************')     
    syn, ant = synonym_antonym_extractor(phrase=seed)
    print(syn)
    print(ant)
    if len(syn)>0: options.append(list(syn))
    if len(ant)>0: options.append(ant)    


    # SEMANTICS -> AI 

    flat_options = [item for sublist in options for item in sublist]    
    num_options = len(flat_options)
    index = np.random.randint(0, high=num_options, size=1, dtype=int)[0]
    next_word = flat_options[index]
    
    if next_word not in words:  
        words.append(next_word) 
        i = i + 1
    

print('final result')
print(words)

