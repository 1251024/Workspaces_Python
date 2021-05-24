# -*- coding:utf-8 -*-

from pymongo import MongoClient, collection

# 1. 클라이언트 가져오기 2가지
client = MongoClient('127.0.0.1', 27017)
# client = MongoClient('mongodb://127.0.0.1/27017')

# 2. 클라이언트 접속 2가지
db = client.test
# db = client['test']

# 3. 컬렉션 가져오기 2가지
collection = db.score
# collection = db['score']


# 4. document 가져오기
result = collection.find()

for res in result:
    print(res)