# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test']
score = db['score']


# 김태리의 final의 math를 100으로 변경하자
res01 = score.update_one(
    {'name':'김태리'},
    {'$set':{'final.math':100}}
)

print(res01.matched_count)
print(res01.modified_count)

#먼저 find된 document 하나만 수정 됨

print('----------')

res02 = score.update_many(
    {'midterm.kor':{'$gt':60}},
    {'$set': {'midterm.kor':100}}
)

print(res02)
print(res02.matched_count)
print(res02.modified_count)