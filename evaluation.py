import pandas as pd
import nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
from nltk.corpus import wordnet
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn



## *******" gen and og"******** ##

def eval_gen_og(gen,og):
    score = 0
    for i in gen:
        best = 0
        w1 = wn.synsets(i)
        if (len(w1) > 0):
            for j in og:
                w2 = wn.synsets(j)
                if len(w2) < 1:
                    continue
                temp = w1[0].path_similarity(w2[0])
                if temp != None and temp > best:
                    best = temp
        else:
            if i in og:
                best = 1
        #     print(best)
        score = score + best

    return score / len(gen)



## ************"og and query "**************** ##
def eval_og_query(og,query):
    score = 0
    for i in og:
        best = 0
        w1 = wn.synsets(i)
        if(len(w1)>0):
            for j in query:
                w2 = wn.synsets(j)
                if len(w2)<1:
                    continue
                temp = w1[0].path_similarity(w2[0])
                if temp!= None and temp > best:
                    best = temp
        else:
            if i in query:
                best = 1
    #     print(best)
        score = score + best
    return score/len(og)

### ****** "gen and query " ***** ####
def eval_gen_query(gen,query):
    score = 0
    for i in gen:
        best = 0
        w1 = wn.synsets(i)
        if (len(w1) > 0):
            for j in query:
                w2 = wn.synsets(j)
                if len(w2) < 1:
                    continue
                temp = w1[0].path_similarity(w2[0])
                if temp != None and temp > best:
                    best = temp
        else:
            if i in query:
                best = 1
        #     print(best)
        score = score + best

    return score / len(gen)

if __name__ == "__main__":
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    stop = stopwords.words('english')
    df = pd.read_csv('input_for_eval.csv')
    print(df.head())
    df3_main = pd.read_csv('electronics1.csv', encoding='utf-8')
    ultimate_score  = []
    df3_main = df3_main[-200:]
    for i in df.index:
        asin = df.asin[i]
        # print("asin",asin)
        query = df['query'][i]
        # print("query",query)
        gen_questions = df.genQuestions[i]
        x = df3_main.loc[df3_main['asin'] == str(asin)]
        og_questions = x['question'].tolist()

        og = []
        gen = []
        for i in og_questions:
            text = tokenizer.tokenize(i)
            og.extend(text)
        for i in gen_questions:
            text = tokenizer.tokenize(i)
            gen.extend(text)
        og = [x.lower() for x in og]
        gen = [x.lower() for x in gen]
        og = list(set(og))
        gen = list(set(gen))
        og = [word.strip('; : ! * - \\ · . ® \® //') for word in og if word not in (stop)]
        gen = [word.strip('; : ! * - \\ · . ® \® //') for word in gen if word not in (stop)]
        ultimate_score.append([eval_gen_og(gen,og),eval_gen_query(gen,query),eval_og_query(og,query)])

    output_eval = pd.DataFrame(ultimate_score, columns=['comparison', 'model', 'original'])
    output_eval.to_csv('eval_output.csv')
