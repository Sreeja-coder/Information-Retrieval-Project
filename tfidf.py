from cleaning_data import *

DF = {}

print("started tfidf data")

### creating columns of the tf-idf matrix ###

def creating_columns():
    columns_tfidf = set()
    for row in cleaned_words:
        for word in row:
            columns_tfidf.add(word)
    print('----------------------------------------')
    print(len(cleaned_words))
    print(len(columns_tfidf))
    print('=========================================')
    return columns_tfidf

#calculate document frequency
def cal_doc_freq(columns_tfidf):
    # DF = {}
    for word in columns_tfidf:
        for i in range(len(cleaned_questions)):
            if (word in cleaned_questions[i]):
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
        iDF[i] = np.log(len(cleaned_questions) + 1 / (DF[i] + 1))
    return iDF

def term_freq():
    term_freq_dict = dict()
    print("inside term_freq",len(cleaned_questions))
    for index in range(len(cleaned_questions)):
        for word in columns_tfidf:
            if word in cleaned_questions[index]:
                term_freq_dict.setdefault(index, []).append((word, cleaned_questions[index].count(word)))
    print("inside term_freq",len(term_freq_dict))
    return term_freq_dict


def cal_tf_idf():
    tf_idf = dict()
    for key, value in term_freq_dict.items():
        for val in value:
            tf_idf.setdefault(key, []).append((val[0], iDF[val[0]] * val[1]))
    return tf_idf

# =============================================================================
# def definition(word_list):
#     temp = set()
#     for i in word_list:
#         syns = wordnet.synsets(i)
#         if(len(syns) == 0):
#             continue
#         text = syns[0].definition()
# # =============================================================================
# #         print(nltk.pos_tag(text))
# # =============================================================================
#         check_pos = lambda pos: pos[:2] in ['NN','NNP','CD','NNS', 'JJ','NNPS']
#         nouns = [x for (x, pos) in nltk.pos_tag(text) if check_pos(pos)]
#         temp.update(nouns)
#     temp.update(word_list)
#     return temp
# =============================================================================


####calling the functions

columns_tfidf = creating_columns()
# =============================================================================
# columns_tfidf = definition(columns_tfidf)
# =============================================================================
# print(len(columns_tfidf))
# print(len(tokenize_stemmed_stopword_list_Q))
iDF = cal_inv_doc_freq(columns_tfidf)
term_freq_dict = term_freq()
tf_idf = cal_tf_idf()
print(len(tf_idf))


print("ending tfidf data")

