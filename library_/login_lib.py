"""------------------------------------------------------------------------------------------
    * This Library is to Handle Login queries here and checking password validation after then it will
provide new login session
------------------------------------------------------------------------------------------"""
from lathonia.library_ import sql,queries,Exceptor,oauth_lib
import pymysql,time

db_ = sql.sql()

class login:
    def __init__(self):
        self.DEFAULT = "DEFAULT"

    def login(self,password,username = None,mail_id=None,ip="Default"):
        """------------------------------------------------------------------------------------------
            * putting Exception Handler function in try Exception will sort out the "INT OBJECT IS NOT SUBSCRIPTABLE " this is raising while
we are deprecating our own Exceptor Handler . while using this exceptor handler ,putting two results is not mandatory
if u putting like that is not problem.

            * :param password:not to be none

            * :param username:not to be none

            * :param mail_id:not to be none

            * :param ip:up to your choice y

            * :return: will be 4 variable access,refresh,result and identity of user
        ------------------------------------------------------------------------------------------"""
        self.username = username
        self.mail_id =mail_id
        self.password = password
        self.ip=ip
        # db = db_.function()
        # if db != -1:
        qu = queries.queries(ip)

        if username != None and mail_id == None:
            print("Base")
            var = qu.verfication(username=self.username)

            if var == 1:
                try:
                    db = db_.function()
                    log_auth=qu.login_username(db,password,username)
                    if  log_auth ==1:
                        OAuth=oauth_lib.main()
                        try:
                            gen = OAuth.main(username=username)
                            if gen[0] == 1:
                                access_token=gen[1]
                                refresh_token = gen[2]
                                Identity=gen[3]
                                result = 1
                            else:
                                raise Exceptor.UnknownErr()
                        except Exception as e:
                            raise Exceptor.Handler(str(e))
                    elif log_auth == -1:
                        # print("ssssss")
                        raise Exceptor.PasswordIncorrect()
                    elif log_auth == -2 or log_auth == -3:
                        raise Exceptor.LoginUserException()
                    else:
                        raise Exceptor.ISE()
                except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
                    f = open('logs/error.log.txt', 'a')
                    f.write("[Error Handler : {Login Error 287 :" + str(e) + "}\nDate Time : {" + str(
                        time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
                    f.close()
                    result = -4


                except Exception as e:
                    print("happedn")
                    raise Exceptor.Handler(str(e))
                except:
                    f = open('logs/error.log.txt', 'a')
                    f.write("[{Unexpected Unknown error occured in Login Error 287}" + "\nDate Time :  {" + str(
                        time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
                    f.close()
                    result = -4
            elif var == 0:
                raise Exceptor.ActivationErr()
            elif var ==-1 or var == -2 or var == -3:
                raise Exceptor.LoginUserException()
            else:
                print("somthiong cuasing wrr")
                raise Exceptor.ISE()
        elif username == None and mail_id != None:
            var2 =qu.verfication(mail_id=self.mail_id)
            if var2 == 1:
                print("Trying...")
                try:
                    db = db_.function()
                    log_auth=qu.login_mail_id(db,password,mail_id)
                    if log_auth== 1:
                        OAuth = oauth_lib.main()
                        try:
                            gen = OAuth.main(mail_id=mail_id)
                            if gen[0] == 1:
                                access_token = gen[1]
                                refresh_token = gen[2]
                                Identity = gen[3]
                                result = 1
                            else:
                                raise Exceptor.UnknownErr()
                        except Exception as e:
                            print("Printer")
                            raise Exceptor.Handler(str(e))
                    elif log_auth == -1:
                            raise Exceptor.PasswordIncorrect()
                    elif log_auth == -2 or log_auth == -3:
                        raise Exceptor.LoginUserException()
                    else:
                        print("Excepting...")
                        raise Exceptor.ISE()
                except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY

                    f = open('logs/error.log.txt', 'a')
                    f.write("[Error Handler : {Login Error 287 :" + str(e) + "}\nDate Time : {" + str(
                        time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.mail_id+ "]\n\n")
                    f.close()
                    print("Tried")
                    result = -4

                except Exception as e:
                    print("Tyi")
                    raise Exceptor.Handler(str(e))
                except:
                    print("Excepting...1")
                    f = open('logs/error.log.txt', 'a')
                    f.write("[{Unexpected Unknown error occured in Login Error 287}" + "\nDate Time :  {" + str(
                        time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.mail_id+ "]\n\n")
                    f.close()
                    result = -4
            elif var2 == 0:
                raise Exceptor.ActivationErr()
            elif var2 ==-1 or var2 == -2 or var2 == -3:
                raise Exceptor.LoginUserException()
            else:
                print("Trying...1")
                raise Exceptor.ISE()
        else:
            print("Trying...21")
            raise Exceptor.InfoError()
        print("the " + str(result))
        if result == 1:
            return result, access_token, refresh_token, Identity
        else:
            return result,self.DEFAULT


    # def main(self,password,username=None,mail_id=None):
    #     self.password = str(password).strip()
    #     query = queries.queries()
    #     self.username = str(username).strip()
    #     self.mail_id = str(mail_id).strip()
    #     if username != None and mail_id == None:
    #
    #         flag = 1
    #         # print("Verfied By username")
    #     elif username == None and mail_id != None:
    #         query.login(self.password,mail_id=self.mail_id)
    #         flag =1
    #     else:
    #         raise ValueError("User or Email Invalid")
    #     return flag