import pymysql
conn=None
err= None
class sql:
    def __init__(self):
        self.hostname="localhost"
        self.username="root"
        self.password=""
        self.database="lathonia"

            #lets add self conn here check back again

    # def function(self):
    #     try:
    #         self.conn = pymysql.connect(host='localhost',
    #                                     user='root',
    #                                     password='',
    #                                     database='lathonia',
    #                                     port=3306,
    #                                     cursorclass=pymysql.cursors.DictCursor)
    #         # print("I am Wokring Properly IDK why this guy taking everything from stack lets check " + str(self.conn))
    #         print("iiii")
    #     except pymysql.connect.Error as e:
    #         # print(type(self.conn))
    #         self.err = str(e)
    #         print(self.err)
    #         self.conn = -1
    #     print("this is self.conn "+ str(self.conn))
    #     return self.conn
    def function(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='lathonia',
                                    port=3306,
                                    cursorclass=pymysql.cursors.DictCursor)
        return self.conn
# import pymysql
# conn=None
# class sql:
#     def __init__(self):
#         self.db_name="trans_"
#         self.hostname="localhost"
#         self.password=""
#         self.username="root"
#         self.conn=pymysql.connect(host='localhost',
#                                  user='root',
#                                  password='',
#                                  database="test1",
#                                  #charset='utf8mb4',
#                                 port=3306,
#                                 cursorclass=pymysql.cursors.DictCursor)#<pymysql.connections.Connection object at 0x0358E1F0>
#
#         #self.conn = "shriram"
#     def func(self):
#         return self.conn
# #m=sql()
# #obj=m.func()
# #print(obj)
# #print(conn)
#
# """
# with obj.cursor() as cursor:
#         sql="SELECT * FROM `trans_`"
#
#         cursor.execute(sql)
#         result=cursor.fetchall()
#         l = len(result)
#         for i in range(l):
#             print(result[i])
#         #tp=type(result)
#         #print(tp)
#         #l=len(result)
#         #print(l)"""