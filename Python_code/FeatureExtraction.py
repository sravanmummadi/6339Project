# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:27:07 2015

@author: sravan
"""
import nltk, re, pprint,sys
import csv
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer # tokenizer 
from nltk.stem.porter import PorterStemmer
stopwordslist = set(stopwords.words('english')) # storing stop words into list
stemmer = PorterStemmer() # getting stemmer object
stemmed_tokens_global={}
negative_words_corpus=['not good','bad','very small','tough','expensive','raw','mediocre','dirty','horrible','filthy','awful','gross','unpleasant','dead','greasy','average','nasty','so-so','dry','meh','hard','high','ridiculous','too much','poor','sub-par','crappy','wrong','undrinkable','yucky','sketchy','enormous','rubbery','not impressive','far','not edible','not close','offensive','loud','unreasonable','slow','tough','wierd','heavy','overly','messy','incorrect','non-existent','inappropriate','unprofessional','opposite','terrible','wasn\'t fresh','not fresh','rude','huge','tiny','lousy','uncomfirtable','inconvenient','busy','sad']
attribute_review_corpus={}
business_id=''
review=''
negative_features={}
"""
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document) [1]
    sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
    sentences = [nltk.pos_tag(sent) for sent in sentences] [3]
"""  

def negative_attribute():
    for ids in attribute_review_corpus.keys():
        if ids not in negative_features.keys():
            negative_features[ids] = []
        for feature in attribute_review_corpus[ids]:
            
            tokenize_feature=nltk.word_tokenize(feature)
            for word in tokenize_feature:
                if word in negative_words_corpus:
                    negative_features[ids].append(feature)
                    break
        print(ids,negative_features[ids])
        

def traverse(result):
    feature=""
    try:
        result.label() 
    except AttributeError:
        return 
    else:
        if result.label() == 'attribute_review':
            #print(result)
            #print("businessid",business_id)
            for leaf in result:
                
                feature+=" "+leaf[0]
                
            attribute_review_corpus[business_id].append(feature)  # or do something else
            #print("features",attribute_review_corpus)
            
        else:
            for child in result:
                traverse(child)

def attribute_review_Extraction(tag_list):
    #tag_list=nltk.pos_tag(tag_list)
    #pattern = "attribute_review: {<NN><VBD><JJ>,<NN><VBZ><JJ>,<VBD><DT>*<VBZ>,<NN><VBD><RB>*<JJ>,<RB>*<JJ><NN>}"
    patterns = """attribute_review: {<NN><VBD><JJ>}
                                    {<NN><VBZ><JJ>}
                                    {<VBD><DT><VBZ>}
                                    {<NN><VBD><RB>*<JJ>}
                                    {<RB><JJ><NN>}"""
    NPChunker =  nltk.RegexpParser(patterns) # create a chunk parser 
    result = NPChunker.parse(tag_list) #parse the example sentence
    traverse(result)
    
            
            
    
def tagText(Text):
    
    text=nltk.word_tokenize(Text.lower())
    #text=nltk.word_tokenize("We are going out.Just you and me.")
    tag_list=nltk.pos_tag(text)
    attribute_review_Extraction(tag_list)
    return
    
    
def csvReadWrite():
    global attribute_review_corpus
    global business_id
    global review
    i=0
    j=0
    k=0
    categories=[]
    feature_csv = csv.writer(open("features.csv", "w"))
    
    
    #with open('/home/sravan/Desktop/data_mining/course_project/SampleData.csv', 'r') as csvfile:
    with open('Bad_Rating.csv', 'r') as bad_restaurants_csvfile:
        with open('/home/sravan/Desktop/data_mining/course_project/dataset-examples-master/yelp_academic_dataset_review.csv', 'r') as review_csvfile:
           
            restaurant_row = csv.reader(bad_restaurants_csvfile, delimiter=',')
            review_row = csv.reader(review_csvfile, delimiter=',')
        
            for restaurant_data in restaurant_row: 
            
                
                business_id=restaurant_data[0]
                if business_id not in attribute_review_corpus.keys():
                        attribute_review_corpus[business_id]=[]
                #print(attribute_review_corpus)
                
               
                    
                for review_data in review_row:                       
                        
                        if review_data[4] == business_id:
                            #print("test",review_data[2])
                            
                            review=review_data[2]
                            #print("review",review)
                            tagText(review)
                #print("features",attribute_review_corpus)
                review_csvfile.seek(0,0)
                
                
                negative_attribute()                   
                
                            
                #review_csvfile.seek(0,0) 
    
                
                     
                           
                            
        
         
           

csvReadWrite()


