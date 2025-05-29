import pymysql

# 配置数据库参数
DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '180623alex'
DBNAME = 'pydb'

def connect_db():
    try:
        # 连接到 MySQL 数据库
        db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
        print('Connected to the pydb database successfully!')
    except pymysql.MySQLError as e:
        print(f'Error connecting to the database: {e}')
    return db

def close_db(db):
    # 关闭数据库连接
    if db:
        db.close()
        print('Database connection closed.')

def create_table(db):
    # 创建 Student 表
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student'
        '(Name VARCHAR(20), ' \
        'Age INT, ' \
        'City VARCHAR(20))'
        )
    print('Table Student created succesfully!')
def drop_table(db):
    # 删除表
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS Student')
    print('Table Student dropped successfully!')

def insert_data(db):
    # 插入数据
    cursor = db.cursor()
    cursor.execute("INSERT INTO Student (Name, Age, City) VALUES ('Alex', 20, 'Beijing')")
    cursor.execute("INSERT INTO Student (Name, Age, City) VALUES ('Bob', 21, 'Shanghai')")
    cursor.execute("INSERT INTO Student (Name, Age, City) VALUES ('Cathy', 22, 'Guangzhou')")
    # 提交数据到数据库
    db.commit()
    print('Data inserted successfully!')

def get_data(db):
    # 查询数据
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Student')
    ressults = cursor.fetchall()
    # 打印查询结果
    for row in ressults:
        print(f'Name: {row[0]}, Age: {row[1]}, City: {row[2]}')

def update_data(db):
    # 更新数据
    cursor = db.cursor()
    cursor.execute('UPDATE Student SET Name = %s WHERE Name = %s', ('Pussy', 'Alex'))
    db.commit()
    print('Data updated successfully!')

def delete_data(db):
    # 删除数据
    cursor = db.cursor()
    cursor.execute('DELETE FROM Student WHERE Name = %s', ('Bob'))
    db.commit()
    print('Data deleted successfully!')

def main():
    db = connect_db()
    create_table(db)
    # insert_data(db)
    get_data(db)
    # update_data(db)
    # get_data(db)
    # delete_data(db)
    # get_data(db)
    close_db(db)

main()