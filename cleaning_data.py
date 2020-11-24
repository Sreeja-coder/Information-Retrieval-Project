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

#

print("started cleaning data")



def remove_stopwords():
    stop = stopwords.words('english')
    pattern=r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))';
    ks = krovetz.PyKrovetzStemmer()
    new_word_final = []
    for i in range(3005,3007):
        line = df2['description'].iloc[i]
        print(line)
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
        check_pos = lambda pos: pos[:] in ['NN','NNP','CD','NNS', 'JJ','NNPS', 'VBD','POS']
        new_words = [x for (x, pos) in nltk.pos_tag(word_tokenize(line)) if check_pos(pos)]
#         new_words = line.split()
        new_word_final.append(krovetz_stem_word(new_words))
        print(i)
        

    print('completed descriptions')

    df['question_no_stopwords'] = df['question'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in (stop)]))
    #del df['description']
    # del df['question']
    new_word_questions = []
    for i in range(len(df)):
        line = df['question'].iloc[i]
        line = line.strip('\[ \]')
        match = re.findall(pattern, line)
        for m in match:
            line = line.replace(m[0], '')
        soup = BeautifulSoup(unescape(line), 'lxml')
        line = soup.text
        line = ' '.join([word.strip('; : ! * - \\ · . ® \® //') for word in line.split() if word not in (stop)])
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        text = tokenizer.tokenize(line)
        check_pos = lambda pos: pos[:] in ['NN','NNP','CD','NNS', 'JJ','NNPS', 'VBD','POS']
        new_words = [x for (x, pos) in nltk.pos_tag(word_tokenize(line)) if check_pos(pos)]
#         new_words = line.split()
        new_word_questions.append(krovetz_stem_word(new_words))
    print('completed questions')
    return new_word_final,new_word_questions
#
def tokenize_description():
# =============================================================================
#     tokenized_lists_D = []
#     ##  tokenizing description  ###
#     for des in df['description_no_stopwords']:
#         #     word_tokens = word_tokenize(des)
#         tokenizer = nltk.RegexpTokenizer(r"\w+")
#         new_words = tokenizer.tokenize(des)
#         tokenized_lists_D.append(new_words)
# =============================================================================

    ## tokenize questions
    tokenized_lists_Q = []
    for des in df['question_no_stopwords']:
        #     word_tokens = word_tokenize(des)
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        new_words = tokenizer.tokenize(des)
        tokenized_lists_Q.append(new_words)
    return tokenized_lists_Q
#
def krovetz_stem(tokenized_list):
    ks = krovetz.PyKrovetzStemmer()
    stemmed_list = []
    for l in tokenized_list:
        new_list = []
        for word in l:
            newword = ""
            try:
                newword =  ks.stem(word)
            except:
                newword = word
            new_list.append(newword)
        stemmed_list.append(new_list)
    return stemmed_list

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
        


##calling functions to clean data:

#reading the csv file
df=pd.read_csv('electronics.csv',encoding='utf-8')
df2 = df.copy()
df2 = df2.drop_duplicates(subset = ["asin"])
df2 = df2.reset_index(drop=True)
print(len(df2))
df = df.drop(['description'], axis=1)
print(df2['description'][45])
cleaned_words,cleaned_questions = remove_stopwords()

# tokenized_lists_Q = tokenize_description()
# print(len(tokenized_lists_Q),"000")
#
# =============================================================================
# tokenize_stemmed_stopword_list_D = krovetz_stem(tokenized_lists_D)
# =============================================================================
# tokenize_stemmed_stopword_list_Q = krovetz_stem(tokenized_lists_Q)
# print(len(tokenize_stemmed_stopword_list_Q),"123")
# print(tokenize_stemmed_stopword_list_D)

# df["q_tokenized_stemmed_no_stopwords"]=tokenize_stemmed_stopword_list_Q
# =============================================================================
# df["d_tokenized_stemmed_no_stopwords"]=tokenize_stemmed_stopword_list_D
# =============================================================================
#
#
# print(df["q_tokenized_stemmed_no_stopwords"][45])


print("ending cleaning data")
print(len(df))




