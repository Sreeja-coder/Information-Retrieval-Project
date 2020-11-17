# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:49:34 2020

@author: shahp
"""
import json as simplejson
import string

import pandas as pd
from collections  import  defaultdict
import re

dict_title = {}   #beauty dict with asin as key and title split as values

df = pd.read_pickle('beauty_df.pkl')
print(df.columns)

print(df.iloc[1])

print(df['title'][1])

# =============================================================================
# df1 = pd.read_pickle('beauty_qa_df.pkl')
# =============================================================================

# =============================================================================
# for index, row in df.iterrows():
#     # print(row)
#     line=str(row['description'])[1:-1]
#     line = re.sub('<[^<]+>', "", line)
#     line = re.sub('<', "", line)
#     line = re.sub('>', "", line)
#     line=line.replace("\\n","")
#     line = line.replace("\\t", "")
# 
#     for char in string.punctuation:
#         line= line.replace(char, ' ')
#     dict_title[row['asin']] = line.split(" ")
# 
# 
# dict_questions = defaultdict(list)
# for index, row in df1.iterrows():
#     # print(row['question'])
#     
#     val = row['question']
#     # print(type(val['questionText']))
#     # print(val['questionText'])
#     # l = row['questions'].split(" ")
#     x = val.split(" ")
#     # y=','.join(x)
#     for i in x:
#         dict_questions[row['asin']].append(i)
# 
# # key = dict_title.keys() & dict_questions.keys()
# #
# # print(key)
# questions_words={}
# title_words= []
# for key,value in dict_title.items():
#     for v in value:
#         title_words.append(v.lower())
# 
# title_words = set(title_words)
# print(title_words)
#     # dict_title[k]
# print(title_words)
# #print(df['asin'].intersection(df1['asin']))
# print(df1['asin'])
# common = dict_title.keys() & dict_questions.keys()
# print(len(common))
# 
# 
# print(df)
# =============================================================================
