###Text Mining###
sentences = "we are Learning TextMining from Sanjivani AI"
##if we want to know position of learning
sentences.index("Learning")
##it will show Learning is 7th position
##this will show character position from  0 to n

###########################################

##if we are want to know position  textmining words
sentences.split().index("TextMining")
##it will be split words in list and count the position 
##if you want to see the list select from sentences.split()   
##it will show 3

############################################
sentences.split()[2][::-1]
##[start:end end:-1(start)] will start from -1,-2,-3 till 

############################################
##suppose we want to print first to last word of the sentence

words = sentences.split()
first_word = words[0]
first_word
last_word = words[-1]
last_word

###now we want to contact the first and last word

contact_word = first_word + " " + last_word
contact_word


##################################################
##we want to print even words from sentence
##words having odd lenght will not be printed

[words[i] for i in range(len(words)) if i%2 == 0]

#########################################
##if we want to print certain/particular word/words

sentences[-2:]
 ##this will print only AI
 
##########################################
##if we want to print entire sentence in reverse ordered:
  
sentences[::-1]  

###############################################
###suppose we want to select each word and print in reversed

words
print(" ".join(word[::-1] for word in words))

#######################################################



#####TOKENATIOZATION####

import nltk 
nltk.download('punkt')
from nltk import word_tokenize
words = word_tokenize("I am reading NLP fundamentals ")
print(words)

###############################

###parts of speech(PoS) tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
##it is goining to mention og speech

##################################################
from nltk.corpus import stopwords
stop_words = stopwords.words("English")
print(stop_words)



#####################################
##suppose we want to replace word in string

sentences2 = "I visited MY IND 14-02-19"
normalized_sentence = sentences2.replace("My","Malaysia").replace("IND","India")
normalized_sentence = normalized_sentence.replace("-19", "-2020")
print(normalized_sentence)

####################################################
##suppose we want to auto correction in sentence 

from autocorrect import Speller
#declare the function Speller define for English

spell = Speller(lang = 'en')
spell('Englilish')

###############################################
##suppose we want to coorect whole sentence

import nltk 
nltk.download('punkt')
from nltk import word_tokenize
sentence3 = "Natural Lanaguage procress detaied within the aart of extraction"
##first tokenize this sentence
sentence3 = word_tokenize(sentence3)
correct_sentence =" ".join([spell(word) for word in sentence3])
print(correct_sentence)

###############################################
#####stemming

stemmer = nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("jumpimng")
stemmer.stem("Jumped")

#################################################
####Lematizer
##lematizer looks into dictionary words

nltk.download("wordnet")

from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("programmed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")

########################################################

##chuking (Shallow Parsing) Identifying named entities

nltk.download("maxent_ne_chunker")
nltk.download("words")
sentences4 = "We are Learning NLP in python by Sanjivani "

##first we will tokenize

nltk.download("averaged_percepron_tagger")
words = word_tokenize(sentences4)
words = nltk.pos_tag(words)
i = nltk.ne_chunk(words,binary=True)
[a for a in i if len(a) == 1]

###############################
##sentences tokenization

from nltk.tokenize import sent_tokenize
sent = sent_tokenize("we are Learning NLP in python. delivered by sanjivani ")
sent

##########################################

from nltk.wsd import lesk
sentence1 = "keeep your savings in bank"
print(lesk(word_tokenize(sentence1),'bank'))

##

sentence2 = "It is so risky to drive over the bank og river"
print(lesk(word_tokenize(sentence2),'bank'))

#####################################
##













