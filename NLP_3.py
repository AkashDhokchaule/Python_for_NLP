# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:33:24 2024

@author: Admin
"""

import re
sentence = "sharat twitted , Whittessing 68th republic day India from Rajpath , \new Dehli,Mesmorizing performance by Indian Army !"
re.sub('r^([\s\w]|_)+', ' ', sentence).split()


'''

'''

def n_gram_extractor(input_str, n):
    tokens = re.sub(r'([^\s\w]|_)+', ' ', input_str).split()
    for i in range(len(tokens)-n-1):
        print(tokens[i:i+n])
        
n_gram_extractor("The cute little boy is playong with kitten",2)
n_gram_extractor("The cute little boy is playong with kitten",3)

################################################

from nltk import ngrams
##extracting n-grams with nltk
list(ngrams("The cute little boy is playong with kitten".split(),2))
list(ngrams("The cute little boy is playong with kitten".split(),3))

#######################

from textblob import TextBlob 
blob = TextBlob("The Cute Little boy is playing with kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)

###################################

###Tokenization using Keras

sentence5 = "sharat twitted , Whittessing 68th republic day India from Rajpath , \new Dehli,Mesmorizing performance by Indian Army ! "

from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)

#####################
from nltk.tokenize import MWETokenizer

sentence5

mwe_tokenizer = MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('!', ' ').split())

#####################################



































