# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:22:57 2015

@author: sravan
"""

import csv

def readCSV(corpus_root):
    with open(corpus_root, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            print (', '.join(row))
readCSV("sample.csv")