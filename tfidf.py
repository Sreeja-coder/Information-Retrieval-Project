from cleaning_data import *

DF = {}

print("started tfidf data")

### creating columns of the tf-idf matrix ###

def creating_columns():
    columns_tfidf = set()
    for row in tokenize_stemmed_stopword_list_D:
        for word in row:
            columns_tfidf.add(word)
    return columns_tfidf

#calculate document frequency
def cal_doc_freq(columns_tfidf):
    # DF = {}
    for word in columns_tfidf:
        for i in range(len(tokenize_stemmed_stopword_list_Q)):
            if (word in tokenize_stemmed_stopword_list_Q[i]):
                try:
                    DF[word].add(i)
                except:
                    DF[word] = {i}
    for i in DF:
        DF[i] = len(DF[i])
    return DF

def word_doc_freq(word):
    c = 0
    try:
        c = DF[word]
    except:
        pass
    return c

#calculate document frequency for each word
def cal_inv_doc_freq(columns_tfidf):
    cal_doc_freq(columns_tfidf)
    iDF = {}
    for i in DF:
        iDF[i] = np.log(len(tokenize_stemmed_stopword_list_Q) + 1 / (DF[i] + 1))
    return iDF

def term_freq():
    term_freq_dict = dict()

    for index in range(len(tokenize_stemmed_stopword_list_Q)):
        for word in columns_tfidf:
            if word in tokenize_stemmed_stopword_list_Q[index]:
                term_freq_dict.setdefault(index, []).append((word, tokenize_stemmed_stopword_list_Q[index].count(word)))
    return term_freq_dict


def cal_tf_idf():
    tf_idf = dict()
    for key, value in term_freq_dict.items():
        for val in value:
            tf_idf.setdefault(key, []).append((val[0], iDF[val[0]] * val[1]))
    return tf_idf


####calling the functions

columns_tfidf = creating_columns()
# print(len(columns_tfidf))
# print(len(tokenize_stemmed_stopword_list_Q))
iDF = cal_inv_doc_freq(columns_tfidf)
term_freq_dict = term_freq()
tf_idf = cal_tf_idf()
print(len(tf_idf))


print("ending tfidf data")

