from cleaning_data import *

DF = {}

print("started tfidf data")

def creating_columns():
    columns_tfidf = set()
    for row in cleaned_words:
        for word in row:
            columns_tfidf.add(word.lower())
    print('----------------------------------------')
    print(len(cleaned_words))
    print(len(columns_tfidf))
    print('=========================================')
    return columns_tfidf

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

def cal_inv_doc_freq(columns_tfidf):
    cal_doc_freq(columns_tfidf)
    iDF = {}
    for i in DF:
        iDF[i] = np.log(len(cleaned_questions)/ (DF[i] + 1)) #removed +1 from the numerator
    return iDF



def term_freq():
    term_freq_dict = dict()
    print("inside term_freq",len(cleaned_questions))
    for index in range(len(cleaned_questions)):
        for word in columns_tfidf:
            if word in cleaned_questions[index]:
                term_freq_dict.setdefault(index, []).append((word, cleaned_questions[index].count(word)/len(cleaned_questions[index])))
    print("inside term_freq",len(term_freq_dict))
    return term_freq_dict


def cal_tf_idf():
    tf_idf = dict()
    for key, value in term_freq_dict.items():
        for val in value:
            tf_idf.setdefault(key, []).append((val[0], iDF[val[0]] * val[1]))
    return tf_idf

columns_tfidf = creating_columns()
iDF = cal_inv_doc_freq(columns_tfidf)
term_freq_dict = term_freq()
tf_idf = cal_tf_idf()





print("ending tfidf data")

