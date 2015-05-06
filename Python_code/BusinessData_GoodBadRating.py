# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import sys
import tokenize
good_rating=['2.5','3.0','3.5','4','4.5','5.0']
bad_rating=['1.0','1.5','2.0']
def csvReadWrite():

    i=0
    j=0
    categories=[]
    good_csv = csv.writer(open("Good_Rating.csv", "w"))
    bad_csv = csv.writer(open("Bad_Rating.csv", "w"))
    
   
    
    #with open('/home/sravan/Desktop/data_mining/course_project/SampleData.csv', 'r') as csvfile:
    
    
    with open('/home/sravan/Desktop/data_mining/course_project/dataset-examples-master/yelp_academic_dataset_business.csv', 'r') as csvfile:
        
        row = csv.reader(csvfile, delimiter=',')
        
        for data in row: 
            
            if i==0:
               i=i+1
               continue
            categories=[]
            j=0
            business_id=data[16]
            stars=data[65]
            temp=data[9]
           
            split=temp.split("\'")
            if len(split) > 1:
                while j < len(split):
                   
                    categories.append(split[j].lower())
                    j=j+1
            
                
           
            
           
            if "restaurants" in categories:
               
               
               
              
                if stars in good_rating:
           # if i<10:
                                       
                    good_csv.writerow([business_id,stars])
                elif stars in bad_rating:
                     
                    bad_csv.writerow([business_id,stars])
                
                #print("hi",data)
            
                #print(data[9])
         
           

                
csvReadWrite()         
