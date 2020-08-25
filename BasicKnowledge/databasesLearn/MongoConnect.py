from pymongo import MongoClient, cursor

client = MongoClient()

db = client.learn
collection = db.fortunater


def insertDoc():
    doc1 = {'name': 'MPQ', 'age': 21, 'gender': 'M'}
    # 插入数据
    collection.insert_one(doc1)
    doc2 = {'name': 'HQL', 'age': 21, 'gender': 'M'}
    collection.insert_one(doc2)


def deleteDoc():
    # 删除文档的方法：delete_one(), delete_many(), remove()
    # delete_one()是删除第一条查询到的符合条件的数据
    # delete_many()和remove()是删除所有符合条件的数据
    collection.delete_many({'name': "MPQ"})


def findDoc():
# 查询某一条文档
    res = collection.find({'name': 'XYF'})
    print("条件查询结果：")
    for item in res:
        print(item)


def findAllDocs():
    # 查询所有文档
    res = collection.find()
    print(res.collection)
    print("所有数据查询结果：")
    res_list = []
    for item in res:
        print(type(item))
        print(item)
        res_list.append(item)
    print(res_list)


def update():
    # 也分update_one()和update_many()
    collection.update_many({'name': 'HQL'}, {'name': 'HQL','age': 19})


def clear():
    collection.drop()

if __name__ == '__main__':
    insertDoc()
    # deleteDoc()
    # update()
    clear()
    findAllDocs()