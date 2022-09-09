import pyodbc
import time
import threading
import queue

class MssqlController():
    def __init__(self):
        starttime = time.time()
        self.queue = queue.Queue()
        super().__init__()

    def ConnectMssql(self, sqlServerNum, localIp, database, user, password):
        # params : 数据库版本, IP, 要连接的数据库, 用户名, 密码
        driver = '{ODBC Driver 17 for SQL Server}'

        print(driver, localIp, database, user, password)
        # 开启子线程，自动更新数据库连接
        sql = threading.Thread(target=self.update_sql, args=(driver, localIp, database, user, password))
        # 守护线程
        sql.setDaemon(True)
        sql.start()
        self.conn = self.queue.get()


    # 动态更新数据库连接 一个小时更新一次
    def update_sql(self,driver,localip,database,user,password):
        while True:
            try:
                self.conn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(driver,localip,database,user,password))
            except Exception as EX:
                time.sleep(5)
                print(repr(EX))
            else:
                self.queue.put(self.conn)
                time.sleep(60*60)
                self.conn.close()

    def Execute(self, sqlCode):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(sqlCode)
        except pyodbc.IntegrityError as ITE:
            raise pyodbc.IntegrityError('数据写入库时 --->>> 主键出现重复 sql ==> "{}"'.format((sqlCode)))
        except pyodbc.ProgrammingError as PGE:
            raise pyodbc.ProgrammingError('语法错误 : sql == > "{}"'.format(sqlCode))
        else:
            self.conn.commit()

    def Select(self, sqlCode):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(sqlCode)
        except Exception as EX:
            print(repr(EX))
        else:
            return self.cursor.fetchall()

def DataToJson(data, tableName):
    jsonData = []
    if tableName == 'list':
        for row in data:
            result = {}
            result['QunNum'] = "\"" + str(row[0]) + "\""
            result['MastQQ'] = "\"" + str(row[1]) + "\""
            result['CreateDate'] = "\"" + str(row[2]) + "\""
            result['Title'] = "\"" + str(row[3]) + "\""
            result['Class'] = "\"" + str(row[4]) + "\""
            result['QunText'] = "\"" + str(row[5]) + "\""
            jsonData.append(result)
    else:
        for row in data:
            result = {}
            result['ID'] = "\"" + str(row[0]) + "\""
            result['QQNum'] = "\"" + str(row[1]) + "\""
            result['Nick'] = "\"" + str(row[2]) + "\""
            result['Age'] = "\"" + str(row[3]) + "\""
            result['Gender'] = "\"" + str(row[4]) + "\""
            result['Auth'] = "\"" + str(row[5]) + "\""
            result['QunNum'] = "\"" + str(row[6]) + "\""
            jsonData.append(result)
    return jsonData



if __name__ == '__main__':
    # controller = MssqlController()
    # # ip = input("ip:\n")
    # # database = input("database:\n")
    # # user = input("user:\n")
    # # password = input("password:\n")
    # controller.ConnectMssql(17, '127.0.0.1', 'GroupData1', 'SA', '3140224')
    # # "select top 10 * from list where Title like  '%兄弟%';"
    # sql = input("sql语句:")
    # datalist = controller.Select(sql)
    # print(datalist, '------')
    import json
    con = MssqlController()
    con.ConnectMssql(17, '127.0.0.1', 'GroupData1', 'SA', '3140224')
    #
    datalist = con.Select("select top 20 * from list;")
    jsondata = DataToJson(datalist, 'list')

