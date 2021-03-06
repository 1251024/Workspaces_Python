# -*- coding:utf-8 -*-

from pymongo import MongoClient, cursor
import pprint

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

cursor = score.find()
# print(cursor)
# cursor 객체로 나옴
# find()는 cursor 객체를 리턴한다

for doc in cursor:
    pprint.pprint(doc)
# pretty라는 함수가 있어서 pprint 하면 예쁘게 나옴

print('-----------')

# 조건 걸어서 가져오기
lee = score.find({'name': '이순신'})
print(lee) # cursor 값이 나옴

for doc in lee:
    print(doc)

leess = score.find_one({'name':'이순신'})
print(leess)


print('-----------')

print('document의 총 갯수: ', score.count_documents({}))


print('-----------')
# 국어점수가 70점보다 더 큰 도큐먼트들을 출력하자.
kors = score.find({'kor':{'$gt':70}},{'_id':0})
for doc in kors:
    print(doc)

