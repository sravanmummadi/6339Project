# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:45:35 2015

@author: sravan
"""

import nltk,re


sentence="food is tasteful and delicious"
#text1.similar("good")
string=nltk.word_tokenize(sentence.lower())
tag_list=nltk.pos_tag(string)
pattern = "attribute_review: {<NN><VBZ><JJ>}"
NPChunker =  nltk.RegexpParser(pattern) # create a chunk parser 
result = NPChunker.parse(tag_list) #parse the example sentence
for child in result:
    print(child)
