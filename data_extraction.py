import gzip
import json as simplejson
import string

import pandas as pd
from collections  import  defaultdict
import re


def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield simplejson.loads(l)

def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')


#### for questions #####
def parse1(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF1(path):
  i = 0
  df = {}
  for d in parse1(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')







print("point1")

df = getDF('data/meta_Electronics.json.gz')
# print(df.head())
# =============================================================================
# df.to_pickle('meta_electronics.pkl')
# =============================================================================
print("point2")
dict_title = {}   #beauty dict with asin as key and title split as values

for index, row in df.iterrows():
    # print(row)
    line=str(row['description'])[1:-1]
    line = re.sub('<[^<]+>', "", line)
    line = re.sub('<', "", line)
    line = re.sub('>', "", line)
    line=line.replace("\\n","")
    line = line.replace("\\t", "")

    for char in string.punctuation:
        line= line.replace(char, ' ')
    dict_title[row['asin']] = line.split(" ")


df1 = getDF1('data/qa_Electronics.json.gz')
# =============================================================================
# df1.to_pickle('beauty_qa_df.pkl')
# =============================================================================
dict_questions = defaultdict(list)
print(df1)
for index, row in df1.iterrows():
    # print(row['question'])
    
    val = row['question']
    # print(type(val['questionText']))
    # print(val['questionText'])
    # l = row['questions'].split(" ")
    x = val.split(" ")
    # y=','.join(x)
    for i in x:
        dict_questions[row['asin']].append(i)

# key = dict_title.keys() & dict_questions.keys()
#
# print(key)
questions_words={}
title_words= []
for key,value in dict_title.items():
    for v in value:


        title_words.append(v.lower())

title_words = set(title_words)
print(title_words)
    # dict_title[k]
print(title_words)
#print(df['asin'].intersection(df1['asin']))
print(df1['asin'])
common = dict_title.keys() & dict_questions.keys()
print(len(common))