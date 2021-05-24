# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

res01 = score.delete_one({'name':'태연'})
print(res01.deleted_count)
# 제일먼저 만난 애 하나만 삭제

# midterm 이라는 field가 존재하는 document 들 삭제
res02 = score.delete_many({'midterm': {'$exists':True}})
print(res02)
print(res02.deleted_count)