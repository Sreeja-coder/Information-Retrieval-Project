from data_extraction import *
from sklearn.feature_extraction.text import TfidfVectorizer

#we need to find words from the dict_title and take their count from questions

 #intersection of dict_title and dict_questions based on column "asin"
# combined={}

# set_of_words = set(title_words.values())

# print(set_of_words)


numOfWordsA = dict.fromkeys(title_words, 0)

for list_word in questions_words.values():
    for word in list_word:
        if title_words.__contains__(word.lower()):
            print(word)
            numOfWordsA[word.lower()] += 1

print(numOfWordsA)




































# from py4tfidf.vectorizer import Tfidf
#
# # print(dict_title)
# #
# #
# # print(dict_questions)
# key = dict_title.keys() & dict_questions.keys()
# combined={}
# for k in key:
#     # print((dict_questions[k]))
#     combined[k]=dict_questions[k]+dict_title[k]
# #
# # print(type(combined.values()))
# # print(list(combined.values()))
# final=[]
# for key,value in combined.items():
#     final.append(value)
#
# # print(final[7])
# vec = Tfidf()
# x_train = vec.vectorize_train(final)
# # x_test = vec.vectorize_test(x_test)
# print(vec)