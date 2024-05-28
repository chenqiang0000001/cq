import pymysql
import yaml
"""
1.PyMySQL 是一个第三方库，安装PyMySQL: 1.pip install pymysql; 2.通过pycharm 【Setting】-【Project】安装;
2.导入 import pymysql
3.创建数据库的链接 connect = pymysql.connect() 参数：host 数据库主机地址，port 数据库端口号(int类型)，user 登录账号，
password 登录密码，database 要连接的数据库名称，charset 数据库编码格式(utf8)
4.基于上述connect对象创建cursor游标，connect.cursor(),游标的理解：可以把作为数据数据操作的对外暴露的服务接口，承载了行为和数据；
5.基于游标执行sql, cursor.execute(sql);
6.执行完查询的sql后获取查询到的数据datas = cursor.fetchall() 默认返回的是元组数据类型；
7.所有操作执行完毕不需要在进行数据库的操作了要关闭游标cursor.close(),并关闭数据库连接connect.close()
8.由于查询操作返回的是数据类型默认是元组，对数据的获取并不方便，所以我们可以指定游标返回字典数据类型；
9.在创建游标时传入pymysql.cursors.DictCursor，即：connect.cursor(pymysql.cursors.DictCursor) 实现指定返回字典数据类型
10.对数据库进行增/删/改操作,需要进行事务的提交 connect.commit(), 查询操作无需此操作；
11. 封装成一个工具类实现在其他模块中调用，完成数据增删改查操作；

"""


class ConnectDB:
    """
    使用方法：
    1.创建db实例 db = ConnectDB();
    2.执行select操作 res = db("select", sql)
    3.执行insert, update, delete操作 db("update", sql)
    4.所有增删改查都执行完毕了，进行数据库链接的关闭 db(connect=False)
    5.注意：数据库关闭后，需要重新实例化才可继续进行增删改查；
    """
    config = {
        "host": "jumpserver.lecangs.com",
        "port": 33060,
        "user": "BM9SybzPuDFinumHhDdkj6q8OwDHDG4OBuX5",
        "password": "qMGTunAo4eYDEfjf",
        "database": "loctek_1108",
        "charset": "utf8"
    }

    def __init__(self):
        self.conn = pymysql.connect(**self.config)

    def select_datas(self, sql):  # select
        cur = self.conn.cursor(pymysql.cursors.DictCursor)  # 创建游标
        cur.execute(sql)  # 通过游标执行sql语句
        res = cur.fetchall()  # 通过游标获取执行结果
        cur.close()
        return res

    def modify_datas(self, sql):  # update, insert, delete
        cur = self.conn.cursor()  # 创建游标
        cur.execute(sql)  # 执行sql语句
        self.conn.commit()  # 提交事务
        cur.close()

    def connect_close(self):  # 关闭数据库
        self.conn.close()

    def __call__(self, act=None, sql=None, connect=True):
        if connect:  # 如果connect 为 True
            if act == 'select':
                datas = self.select_datas(sql)
                return datas
            elif act in ['update', 'insert', 'delete']:
                self.modify_datas(sql)

        else:  # 当connect 为 False 时关闭数据库的连接
            self.connect_close()


if __name__ == '__main__':
    c = ConnectDB()
    status = 'SELECT * FROM bms_hand_adjust WHERE id = 16'
    data1 = c.select_datas(status)
    print(data1)
    print(c)