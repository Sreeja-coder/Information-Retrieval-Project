import math
from collections import Counter

from cleaning_data import *
from tfidf import *
import numpy as np


print("started cosine  distance")

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

def gen_vector(tokens):
    Q = np.zeros((len(columns)))

    counter = Counter(tokens)
    words_count = len(tokens)

    query_weights = {}

    for token in np.unique(tokens):

        tf = counter[token] / words_count
        df = word_doc_freq(token)
        idf = np.log((len(cleaned_questions)) / (df + 1))

        try:
            ind = columns.index(token.lower())
            Q[ind] = tf * idf
            # print(ind)
        except:
            pass
    return Q

def cosine_sim(a, b):
    cos_sim = np.dot(a, b)/((np.linalg.norm(a)*np.linalg.norm(b))+1)
    return cos_sim


def cosine_similarity(k1, query):
    print("Cosine Similarity")
    #     preprocessed_query = preprocess(query)
    #     tokens = word_tokenize(str(preprocessed_query))

    print("\nQuery:", query)
    #     print("")
    #     print(tokens)

    d_cosines = []

    query_vector = gen_vector(query)
    # print(query_vector)

    print("len", len(query_vector))
    for d in D:
        d_cosines.append(cosine_sim(query_vector, d))

    out = dict()
    for i in range(len(d_cosines)):
        out[i] = d_cosines[i]

    out = dict(sorted(out.items(), key=lambda item: item[1]))

    #     print(d_cosines)
    #     out = np.array(d_cosines).argsort()
    #     out=list(out)
    #     out=out[-10:]

    print("")
    # print(out)
    final_set = set()
    for x in list(reversed(list(out)))[0:50]:
       final_set.add(df_main['question'][x])
    final_set = list(final_set)
    for j in range(k1):
        print(j,":",final_set[j])
    return final_set


# Query = cleaned_words[150]
asin = []
query = []
gen_questions = []
for i in range(len(eval_output)):
    asin.append(eval_output[i][0])
    Query = eval_output[i][1]
    query.append(Query)
    gen_questions.append(cosine_similarity(10, Query))
    # Query = query_tokenize("['Committed to present the best audio performance, DN-1000 is designed to be one of the finest earphones. By utilising the innovative Hybrid technology&quot; which drivers, it creates an amazing sound that is suitable for almost all music. Sound Signature: Natural rich bass with excellent treble extension and crystal clear clarity. Accessories: 10 sets of Eartips 1 pair of Earhook 3.5mm Female to 6.5mm Male Adapter 3.5mm Female to 2-pin Male Adapter Carry Box Soft leather Carry pouch Shirt Clip Technical Specification: Type: Dynamic Balanced Armature(10mm) Sound pressure level: 98+/-2dB Impedance: 10 Frequency Response: 16Hz-22KHz Noise Attenuation: 26dB Plug: 3.5mm Gold-Plated Cable Length: 1.20M']")
    # Query =  query_tokenize("The projector is equipped with an innovative cooling system with heat dispersion, as well as a noise suppression technology which cuts fan sound in half.Two Built-in speaker will bring you an amazing viewing experience.")
    # eval_output[i].append(gen_questions)
    # print(Query)

output_df = pd.DataFrame()
output_df['asin'] = asin
output_df['query'] = query
output_df['genQuestions'] = gen_questions
output_df.to_csv('input_for_eval.csv')

print("endng cosine")
