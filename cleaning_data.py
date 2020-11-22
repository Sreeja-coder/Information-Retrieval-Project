import pandas as pd
import pickle
import nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import krovetz
import numpy as np

from collections import defaultdict

#

print("started cleaning data")

def remove_stopwords():
    stop = stopwords.words('english')
    df['description_no_stopwords'] = df['description'].apply(
        lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    df['question_no_stopwords'] = df['question'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in (stop)]))
    del df['description']
    # del df['question']
#
def tokenize_description():
    tokenized_lists_D = []
    ##  tokenizing description  ###
    for des in df['description_no_stopwords']:
        #     word_tokens = word_tokenize(des)
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        new_words = tokenizer.tokenize(des)
        tokenized_lists_D.append(new_words)

    ## tokenize questions
    tokenized_lists_Q = []
    for des in df['question_no_stopwords']:
        #     word_tokens = word_tokenize(des)
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        new_words = tokenizer.tokenize(des)
        tokenized_lists_Q.append(new_words)
    return tokenized_lists_D,tokenized_lists_Q
#
def krovetz_stem(tokenized_list):
    ks = krovetz.PyKrovetzStemmer()
    stemmed_list = []
    for l in tokenized_list:
        new_list = []
        for word in l:
            #             print(word)
            #             print(ks.stem(word))
            new_list.append(ks.stem(word))
        stemmed_list.append(new_list)
    return stemmed_list



##calling functions to clean data:

#reading the csv file
df=pd.read_csv("pcikle_to_csv.csv")
print(df['description'][45])
remove_stopwords()
tokenized_lists_D,tokenized_lists_Q = tokenize_description()
#
tokenize_stemmed_stopword_list_D = krovetz_stem(tokenized_lists_D)
tokenize_stemmed_stopword_list_Q = krovetz_stem(tokenized_lists_Q)
# print(tokenize_stemmed_stopword_list_D)

df["q_tokenized_stemmed_no_stopwords"]=tokenize_stemmed_stopword_list_Q
df["d_tokenized_stemmed_no_stopwords"]=tokenize_stemmed_stopword_list_D
#
#
# print(df["q_tokenized_stemmed_no_stopwords"][45])


print("ending cleaning data")




