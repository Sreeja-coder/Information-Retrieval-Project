import pandas as pd
import pickle
import nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import krovetz
import numpy as np
from nltk.corpus import wordnet
import re
from bs4 import BeautifulSoup
from html import unescape
from nltk.tokenize import word_tokenize

from collections import defaultdict

print("started cleaning data")


def remove_stopwords():
    stop = stopwords.words('english')
    pattern = r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))';
    ks = krovetz.PyKrovetzStemmer()
    new_word_final = []
    for i in range(len(df2)):
        line = df2['description'].iloc[i]
        line = line.strip('\[ \]')
        match = re.findall(pattern, line)
        for m in match:
            url = m[0]
            line = line.replace(url, '')
        soup = BeautifulSoup(unescape(line), 'lxml')
        line = soup.text
        line = ' '.join([word.strip('; : ! * - \\ · . ® \® //') for word in line.split() if word not in (stop)])
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        text = tokenizer.tokenize(line)
        check_pos = lambda pos: pos[:] in ['NN', 'NNP', 'CD', 'NNS', 'JJ', 'NNPS', 'VBD', 'POS']
        new_words = [x for (x, pos) in nltk.pos_tag(text) if check_pos(pos)]
        #         new_words = line.split()
        new_word_final.append(krovetz_stem_word(new_words))
        print(i)

    print('completed descriptions')

    df['question_no_stopwords'] = df['question'].apply(
        lambda x: ' '.join([word for word in x.split() if word.lower() not in (stop)]))
    # del df['description']
    # del df['question']
    new_word_questions = []
    for i in range(len(df)):
        line = df['question_no_stopwords'].iloc[i]
        line = line.strip('\[ \]')
        match = re.findall(pattern, line)
        for m in match:
            line = line.replace(m[0], '')
        soup = BeautifulSoup(unescape(line), 'lxml')
        line = soup.text
        line = ' '.join([word.strip('; : ! * - \\ · . ® \® //') for word in line.split() if word not in (stop)])
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        text = tokenizer.tokenize(line)
        check_pos = lambda pos: pos[:] in ['NN', 'NNP', 'CD', 'NNS', 'JJ', 'NNPS', 'VBD', 'POS']
        new_words = [x for (x, pos) in nltk.pos_tag(text) if check_pos(pos)]
        #         new_words = line.split()
        new_word_questions.append(krovetz_stem_word(new_words))
    print('completed questions')
    return new_word_final, new_word_questions


def krovetz_stem_word(word):
    ks = krovetz.PyKrovetzStemmer()
    stemmed_list = []
    for i in word:
        try:
            stemmed_list.append(ks.stem(i))
        except:
            print(i)
            stemmed_list.append(i)
    return stemmed_list


def query_tokenize(line):
    stop = stopwords.words('english')
    pattern = r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))';
    ks = krovetz.PyKrovetzStemmer()
    line = line.strip('\[ \]')
    match = re.findall(pattern, line)
    for m in match:
        url = m[0]
        line = line.replace(url, '')
    soup = BeautifulSoup(unescape(line), 'lxml')
    line = soup.text
    line = ' '.join([word.strip('; : ! * - \\ · . ® \® //') for word in line.split() if word not in (stop)])
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    text = tokenizer.tokenize(line)
    check_pos = lambda pos: pos[:] in ['NN', 'NNP', 'CD', 'NNS', 'JJ', 'NNPS', 'VBD', 'POS']
    new_words = [x for (x, pos) in nltk.pos_tag(text) if check_pos(pos)]
    #         new_words = line.split()
    return (krovetz_stem_word(new_words))


df=pd.read_csv('pcikle_to_csv.csv',encoding='utf-8')
df2 = df.copy()
df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]
df2 = df2.drop_duplicates(subset = ["asin"])
df2 = df2.reset_index(drop=True)
cleaned_words,cleaned_questions = remove_stopwords()
print("cleaning data ended")