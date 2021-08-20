import pymysql
import time
from lathonia.library_ import sql,Exceptor
db_= sql.sql()
class queries:
    def __init__(self,ip = "default"):
        self.ip = str(ip.strip())

    def updater (self,username,mail_id,mail_token):
        self.mail_token = mail_token
        self.mail_id = mail_id
        self.username = username

        try:
            # with self.conn.cursor() as cursor:
            self.conn = db_.function()
            cursor = self.conn.cursor()
            query = "UPDATE `users` SET `mail_token` = %s WHERE `username` = %s AND `mail_id`=%s"
            parameter = (self.mail_token,self.username, self.mail_id)
            cursor.execute(query, parameter)
            self.conn.commit()
            result = 1

        except pymysql.Error as e: #GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
            f = open('logs/error.log.txt', 'a')
            f.write("[Error Handler : {Updater Error Line 25:" +str(e)+"}\nDate Time : {"+str(time.ctime(time.time()))+"}\nIP_ADDR :"+self.ip+"\nUsername : "+self.username+"]\n\n")
            f.close()
            result = -1
        except:
            f = open('logs/error.log.txt', 'a')
            f.write("[{Unexpected Unknown error occured in Updater }"+"\nDate Time :  {"+str(time.ctime(time.time()))+"}\nIP_ADDR :"+self.ip+"\nUsername : "+self.username+"]\n\n")
            f.close()
            result = -1
        return result
    def activater(self,username,mail_id):
        self.mail_id = mail_id
        self.username = username
        # self.conn = connection
        try:
            self.conn =db_.function()
            cursor = self.conn.cursor()
            query = "UPDATE `users` SET `active` = '1' WHERE `username` = %s AND `mail_id`=%s"
            parameter = (self.username, self.mail_id)
            cursor.execute(query,parameter)
            self.conn.commit()
            result = 1
        except pymysql.Error as e: #GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
            f = open('logs/error.log.txt', 'a')
            f.write("[Error Handler : {Activater Error Line 43:" +str(e)+"}\nDate Time : {"+str(time.ctime(time.time()))+"}\nIP_ADDR :"+self.ip+"\nUsername : "+self.username+"]\n\n")
            f.close()
            result = -1
        except:
            f = open('logs/error.log.txt', 'a')
            f.write("[{Unexpected Unknown error occured in Activater  }"+"\nDate Time :  {"+str(time.ctime(time.time()))+"}\nIP_ADDR :"+self.ip+"\nUsername : "+self.username+"]\n\n")
            f.close()
            result = -1

        return result
    def verfication(self,username = None,mail_id=None): #DONT RAISE ANY EXCEPTION THROUGH VERIFCATION .IT IS LIB FUNCTION SO DONT!
        self.mail_id = mail_id
        self.username = username
        # self.conn = connection
        print("Trying ...122")
        if self.username != None and self.mail_id != None:
            try:
                # with self.conn.cursor() as cursor:
                self.conn =db_.function()
                cursor = self.conn.cursor()
                query = "SELECT `active` FROM `users` WHERE `username` = %s AND `mail_id`=%s"
                # print("The First Verification")
                parameter = (self.username,self.mail_id)
                cursor.execute(query, parameter)
                res = cursor.fetchall()
                if len(res) > 0 :
                    if type(res) == list:
                        activater = res[0]['active']
                        if activater == 1:
                            result = 1
                            # print("The Verfication Result => " + str(res) + str(result))
                        elif activater == 0:
                            result = 0
                            string_value = res[0]['active']
                            # print("The Verfication Result :else  => " + str(string_value))
                        else:
                            result = -1
                    else:
                        result = -2
                else:
                    result = -3
            except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
                f = open('logs/error.log.txt', 'a')
                f.write("[Error Handler : {verification Error line 79:" + str(e) + "}\nDate Time : {" + str(time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
                f.close()
                result = -4
            except:
                f = open('logs/error.log.txt', 'a')
                f.write("[{Unexpected Unknown error occured in verification Error line 79 }" + "\nDate Time :  {" + str(
                    time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
                f.close()
                result = -4
        elif self.username != None and self.mail_id == None:
            try:
                self.conn = db_.function()
                cursor = self.conn.cursor()
                query = "SELECT `active` FROM `users` WHERE `username` = %s "
                print("The Second Verification")
                parameter = (self.username)
                cursor.execute(query, parameter)
                res = cursor.fetchall()
                if len(res) > 0 :
                    if type(res) == list:
                        activater = res[0]['active']
                        if activater == 1:
                            result = 1
                            # print("The Verfication Result => " + str(res) + str(result))
                        elif activater == 0:
                            result = 0
                            print("Here")
                            string_value = res[0]['active']
                            # print("The Verfication Result else  => " + str(string_value))
                        else:
                            result = -1
                    else:
                        result = -2
                else:
                    result = -3
            except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
                f = open('logs/error.log.txt', 'a')
                f.write("[Error Handler : {Verfication Error 109 :" + str(e) + "}\nDate Time : {" + str(time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
                f.close()
                result = -4
            except:
                f = open('logs/error.log.txt', 'a')
                f.write("[{Unexpected Unknown error occured in Verfication Error 109  }" + "\nDate Time :  {" + str(
                    time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
                f.close()
                result = -4
        elif self.username == None and self.mail_id != None:
            print("Trying ...12")
            try:
                self.conn = db_.function()
                cursor = self.conn.cursor()
                query = "SELECT `active` FROM `users` WHERE `mail_id`=%s"
                print("The Third Verfication")
                parameter = (self.mail_id)
                cursor.execute(query, parameter)
                res = cursor.fetchall()
                if len(res) > 0 :
                    if type(res) == list:
                        activater = res[0]['active']
                        if activater == 1:
                            result = 1
                            # print("The Verfication Result => " + str(res) + str(result))
                        elif activater == 0:
                            result = 0
                            string_value = res[0]['active']
                            # print("The Verfication Result :else  => " + str(string_value))
                        else:
                            result = -1
                    else:
                        result = -2
                else:
                    result = -3
            except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
                f = open('logs/error.log.txt', 'a')
                f.write("[Error Handler : {Verfication Error 139 :" + str(e) + "}\nDate Time : {" + str(time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.mail_id+ "]\n\n")
                f.close()
                result = -4
            except:
                f = open('logs/error.log.txt', 'a')
                f.write("[{Unexpected Unknown error occured in Verfication Error 139 }" + "\nDate Time :  {" + str(time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.mail_id+ "]\n\n")
                f.close()
                result = -4
        else:
            # print("The else condition")
            result = -5
        print("Result"+str(result))
        return  result
    def dup_checker(self,username,mail_id):
        self.username = username
        self.mail_id = mail_id
        try:
            db = db_.function()
            cursor = db.cursor()
            query = "SELECT `username` FROM `users` WHERE `username` = %s OR `mail_id`= %s"
            parameter = (self.username,self.mail_id)
            cursor.execute(query,parameter)
            res = cursor.fetchall()
            print("The dup checker REsult " + str ( res))
            if(len(res) > 0 ):
                if type(res) == list:
                    # Logs should be here
                    result = -1
                    print(result)
                else:
                    result = 1
            else:
                result = 2
        except pymysql.Error as e: #GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
            print("I am Happed")
            f = open('logs/error.log.txt', 'a')
            f.write("[Error Handler : {Duplicate Error line 171 :" +str(e)+"}\nDate Time : {"+str(time.ctime(time.time()))+"}\nIP_ADDR :"+self.ip+"\nUsername : "+self.username+"]\n\n")
            f.close()
            result = -2
        except:
            f = open('logs/error.log.txt', 'a')
            f.write("[{Unexpected Unknown error occured in Dup checker }"+"\nDate Time :  {"+str(time.ctime(time.time()))+"}\nIP_ADDR :"+self.ip+"\nUsername : "+self.username+"]\n\n")
            f.close()
            result = -3
        return result
    def login_mail_id(self,conn,password,mail_id):
        self.password = password.strip()
        try:
            # with conn.cursor() as cursor:
            cursor = conn.cursor()
            query = "SELECT `password` FROM `users` WHERE `mail_id` = %s"
            parameters = (mail_id)
            cursor.execute(query, parameters)
            res = cursor.fetchall()
            if len(res) > 0:
                if type(res) == list:
                    res__ = res[0]['password']
                    res_ = str(res__).strip()
                    if self.password == res_:
                        result = 1
                    else:
                        result = -1 #PASSWORD INCORRECT
                else:
                    result = -2
            else:
                result = -3

        except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
            f = open('logs/error.log.txt', 'a')
            f.write("[Error Handler : {Login mail_id Error 228:" + str(e) + "}\nDate Time : {" + str(
                time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
            f.close()
            result = -4
        except:
            f = open('logs/error.log.txt', 'a')
            f.write("[{Unexpected Unknown error occured in Login mail_id Error 228 }" + "\nDate Time :  {" + str(
                time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
            f.close()
            result = -4
        return result
    def login_username(self,conn,password,username):
        self.password =password.strip()
        try:
            cursor = conn.cursor()
            query = "SELECT `password` FROM `users` WHERE `username` = %s"
            parameters =(username)
            cursor.execute(query,parameters)
            res = cursor.fetchall()
            if len(res) > 0:
                if type(res) == list:
                    res__= res[0]['password']
                    res_ = str(res__).strip()
                    if self.password == res_:
                        result =1
                    else:
                        result = -1  #PASSWORD INCORRECT
                else:
                    result = -2
            else:
                result = -3
        except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
            f = open('logs/error.log.txt', 'a')
            f.write("[Error Handler : {Login username Error 254 :" + str(e) + "}\nDate Time : {" + str(
                time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
            f.close()
            result = -4
        except:
            f = open('logs/error.log.txt', 'a')
            f.write("[{Unexpected Unknown error occured in Login username Error 254 }" + "\nDate Time :  {" + str(
                time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
            f.close()
            result = -4
        return result

    #
    def mail_updater(self,username,mail_id,sent_message,status):
        self.username = username
        self.mail_id = mail_id
        self.message = sent_message
        self.status= status
        try:
            db= db_.function()
            cursor = db.cursor()
            query = "INSERT INTO `mail_manager`(`username`, `mail_id`,`status`, `sent_message`) VALUES (%s,%s,%s,%s)"
            parameters = (self.username,self.mail_id,status,sent_message)
            cursor.execute(query,parameters)
            db.commit()
            result = 1
        except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
            f = open('logs/error.log.txt', 'a')
            f.write("[Error Handler : {mail_updater Error 379:" + str(e) + "}\nDate Time : {" + str(
                time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
            f.close()
            result = -1
            pass
        except:
            f = open('logs/error.log.txt', 'a')
            f.write("[{Unexpected Unknown error occured in mail_updater Error 385}" + "\nDate Time :  {" + str(
                time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
            f.close()
            result = -1
            pass
        return result
    def session_manager_1(self,access_token,refresh_token,username="default",mail_id="default",mobile="default"):
        try:
            db= db_.function()
            cursor = db.cursor()
            query= "INSERT INTO `sessions`(`username`, `mail_id`, `mobile`, `access_token`, `refresh_token`,`active`,`type`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            parameters =(username,mail_id,mobile,access_token,refresh_token,1,"API")
            cursor.execute(query,parameters)
            db.commit()
            result = 1
        except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
            f = open('logs/Authentication_Err.txt', 'a')
            f.write("[Error Handler : {session_manager- Authentication_Err 319:" + str(e) + "}\nDate Time : {" + str(
                time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + username + "]\n\n")
            f.close()
            result = -1
            pass
        except:
            f = open('logs/Authentication_Err.txt', 'a')
            f.write("[{Unexpected Unknown error occured in session manager 1 326}" + "\nDate Time :  {" + str(
                time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + username + "]\n\n")
            f.close()
            result = -1
            pass
        return result

    def session_getter(self,access_token,username=None,mail_id=None):
        content = None
        if username != None  and mail_id == None:
            try:
                db = db_.function()
                cursor = db.cursor()
                query = "SELECT * FROM `sessions` WHERE `access_token` = %s AND `username` = %s AND `active`=%s"
                paramters=(access_token,username,1)
                cursor.execute(query,paramters)
                content = cursor.fetchall()
                result = 1

            except:
                result = -1
        elif username == None and mail_id !=None:
            try:
                db = db_.function()
                cursor = db.cursor()
                query = "SELECT * FROM `sessions` WHERE `access_token` = %s AND `mail_id` = %s AND `active`=%s"
                paramters = (access_token, mail_id, 1)
                cursor.execute(query, paramters)
                content = cursor.fetchall()
                result = 1

            except:
                result = -1
        else:
            raise Exceptor.ISE()

        return result,content
    def session_changer_1(self,refresh_token,username=None,mail_id=None):
        content = None
        if username != None and mail_id == None:
            try:
                db = db_.function()
                cursor = db.cursor()
                query = "SELECT * FROM `sessions` WHERE `refresh_token` = %s AND `username` = %s"
                paramters = (refresh_token, username)
                cursor.execute(query, paramters)
                content = cursor.fetchall()
                result = 1

            except:
                result = -1
        elif username == None and mail_id != None:
            try:
                db = db_.function()
                cursor = db.cursor()
                query = "SELECT * FROM `sessions` WHERE `refresh_token` = %s AND `mail_id` = %s "
                paramters = (refresh_token,mail_id)
                cursor.execute(query, paramters)
                content = cursor.fetchall()

                result = 1

            except:
                result = -1
        else:
            raise Exceptor.ISE()
        # print(str(result))
        return result, content
    def deactivate_session(self,refresh_token,username=None,mail_id=None):

        if username != None and mail_id == None:
            try:
                db = db_.function()
                query = "UPDATE `sessions` SET `active` = '0' WHERE `username` = %s AND `refresh_token` = %s AND `active` = %s"
                cursor = db.cursor()
                parameters=(username,refresh_token,1)
                c= cursor.execute(query,parameters)
                print(c)
                db.commit()
                print(db.commit())
                result = 1
            except:
                result = -1
        elif username == None and mail_id !=None:
            try:
                db = db_.function()
                query = "UPDATE `sessions` SET `active` = '0' WHERE `mail_id` = %s AND `refresh_token` = %s AND `active` = %s "
                cursor = db.cursor()
                parameters = (mail_id, refresh_token,1)
                cursor.execute(query, parameters)
                db.commit()
                result = 1
            except:
                result = -1
        else:
            raise Exceptor.ISE()
        return result
# with db.cursor() as cursor:
# with db.cursor() as cursor:
#     query = "ALTER IGNORE TABLE users ADD UNIQUE INDEX idx_name (mail_id)"
#     cursor.execute(query)
#     db.commit()
# self.instagram = instagram
# self.twitter =twitter
# def dup_check(self,username,connection):
#     self.username = username
#     self.conn =connection
#     with self.conn.cursor() as cursor:
#         query = "SELECT `username` FROM `users` WHERE `username` = %s"
#         parameter = (self.username)
#         cursor.execute(query, parameter)
#         res = cursor.fetchall()
#         print("The Dup Check Result " + str(res))
# from lathonia.library_ import  mail
# import  pymysql
# import random
# def login(self,password,username = None,mail_id=None):
#     #     self.username = username
#     #     self.mail_id =mail_id
#     #     self.password = password
#     #     # db = db_.function()
#     #     # if db != -1:
#     #     if username != None and mail_id == None:
#     #         var = self.verfication(username=self.username)
#     #         if var == 1:
#     #             try:
#     #                 db = db_.function()
#     #                 if self.login_username(db,password,username) ==1:
#     #                     result = 1
#     #                 else:
#     #                     result = -1
#     #
#     #             except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
#     #                 f = open('logs/error.log.txt', 'a')
#     #                 f.write("[Error Handler : {Login Error 287 :" + str(e) + "}\nDate Time : {" + str(
#     #                     time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
#     #                 f.close()
#     #                 result = -4
#     #             except:
#     #                 f = open('logs/error.log.txt', 'a')
#     #                 f.write("[{Unexpected Unknown error occured in Login Error 287}" + "\nDate Time :  {" + str(
#     #                     time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
#     #                 f.close()
#     #                 result = -4
#     #         elif var == -1:
#     #             raise Exceptor.ActivationErr()
#     #         elif var == -2 or var == -3:
#     #             raise Exceptor.LoginUserException()
#     #         else:
#     #             raise Exceptor.ISE()
#     #     elif username == None and mail_id != None:
#     #         var2 =self.verfication(mail_id=self.mail_id)
#     #         if var2 == 1:
#     #             try:
#     #                 db = db_.function()
#     #                 if self.login_mail_id(db,password,mail_id) == 1:
#     #                     result = 1
#     #                 else:
#     #                     result =-1
#     #             except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
#     #                 f = open('logs/error.log.txt', 'a')
#     #                 f.write("[Error Handler : {Login Error 287 :" + str(e) + "}\nDate Time : {" + str(
#     #                     time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
#     #                 f.close()
#     #                 result = -4
#     #             except:
#     #                 f = open('logs/error.log.txt', 'a')
#     #                 f.write("[{Unexpected Unknown error occured in Login Error 287}" + "\nDate Time :  {" + str(
#     #                     time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
#     #                 f.close()
#     #                 result = -4
#     #         elif var2 == -1:
#     #             raise Exceptor.ActivationErr()
#     #         elif var2 == -2 or var2 == -3:
#     #             raise Exceptor.LoginUserException()
#     #         else:
#     #             raise Exceptor.ISE()
#     #     else:
#     #         raise Exceptor.InfoError()
#     #
#     #
#     #     print("the " + str(result))
#     #     return result