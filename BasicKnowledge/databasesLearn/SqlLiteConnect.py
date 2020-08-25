import sqlite3


def create_Database():
    # 创建表
    c.execute("CREATE TABLE student (id integer, name text, age integer, gender text)")


def insert_Many_data(data):
    # 插入多条数据
    c.executemany("INSERT INTO student VALUES (?, ?, ?, ?)", data)


def insert_One_data(data):
    # 插入一条数据
    c.executemany("INSERT INTO student VALUES (?, ?, ?, ?)", data)


def delete_data_byId(id):
    # 根据id删除数据
    c.execute("DELETE FROM student WHERE id=?", [id])


def delete_data_byName(name):
    # 根据name删除数据
    c.execute("DELETE FROM student WHERE name=?", (name,))


def querry_Data():
    # 查询数据
    for row in c.execute("SELECT * FROM student"):
        print(row)


if __name__ == '__main__':
    connection = sqlite3.connect('fortunater.db')
    c = connection.cursor()

    data = [
        (1000, 'XYF', 20, 'Man'),
        (1001, 'WH', 20, 'Man'),
        (1002, 'LWT', 20, 'Woman'),
    ]
    delete_data_byId(1001)
    insert_Many_data(data)
    querry_Data()

    # 提交改变
    connection.commit()
    # 关闭连接
    connection.close()
