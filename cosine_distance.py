import math
from collections import Counter

from cleaning_data import *
from tfidf import *
import numpy as np


print("started cosine  distance")
## cal the tf-idf matrix :

sorted(columns_tfidf)
print(len(columns_tfidf))
columns = list(columns_tfidf)


D = np.zeros((len(cleaned_questions), len(columns_tfidf)))
for key,values in tf_idf.items():
    # print(key)
    # print(values)
    # print("i",i)
    for v in values:
        # print(v)
        try:
            # print("inside try")
            ind = columns.index(v[0])
            # print(v[0])
            # print(ind)
            D[key][ind] = v[1]
            # print(D[key][ind])
        except:
            # print("in except")
            pass


# print(columns.index("try"))

def gen_vector(tokens):
    Q = np.zeros((len(columns)))

    counter = Counter(tokens)
    words_count = len(tokens)

    query_weights = {}

    for token in np.unique(tokens):

        tf = counter[token] / words_count
        df = word_doc_freq(token)
        idf = math.log((len(cleaned_questions) + 1) / (df + 1))

        try:
            ind = columns.index(token)
            Q[ind] = tf * idf
        except:
            pass
    return Q



def cosine_sim(a, b):
    cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cos_sim
#
def cosine_similarity(k, query):
    print("Cosine Similarity")
#     preprocessed_query = preprocess(query)
#     tokens = word_tokenize(str(preprocessed_query))

    print("\nQuery:", query)
#     print("")
#     print(tokens)

    d_cosines = []

    query_vector = gen_vector(query)
    
    print("len",len(query_vector))
    for d in D:
        d_cosines.append(cosine_sim(query_vector, d))

#     print(d_cosines)
    out = np.array(d_cosines).argsort()[:k][::-1]

    print("")

    print(out)
    for o in out:
        print(df['question'][o])
#
Query = cleaned_words[0]
cosine_similarity(10,Query)
print(Query)