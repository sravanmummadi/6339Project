# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:27:07 2015

@author: sravan
"""
import nltk, re, pprint,sys
import csv
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer # tokenizer 
from nltk.stem.porter import PorterStemmer
stopwordslist = set(stopwords.words('english')) # storing stop words into list
stemmer = PorterStemmer() # getting stemmer object
stemmed_tokens_global={}
"""
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document) [1]
    sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
    sentences = [nltk.pos_tag(sent) for sent in sentences] [3]
"""  

def tagText(Text):
    text=nltk.word_tokenize(Text)
    #text=nltk.word_tokenize("We are going out.Just you and me.")
    print(nltk.pos_tag(text))
    
    
def csvReadWrite():

    i=0
    j=0
    categories=[]
    
    
    
    #with open('/home/sravan/Desktop/data_mining/course_project/SampleData.csv', 'r') as csvfile:
    with open('Bad_Rating.csv', 'r') as bad_restaurants_csvfile:
        with open('/home/sravan/Desktop/data_mining/course_project/dataset-examples-master/yelp_academic_dataset_business.csv', 'r') as business_csvfile:
            business_row = csv.reader(business_csvfile, delimiter=',')
            restaurant_row = csv.reader(bad_restaurants_csvfile, delimiter=',')
            
        
            #for restaurant_data in restaurant_row: 
            
                
            #business_id=restaurant_data[0]
                
            for business_data in business_row:                        
                if business_data[16] == "PK6aSizckHFWk8i0oxt5DA":
                    print(business_data[9])
                    quit()
                            
        
         
           

csvReadWrite()


