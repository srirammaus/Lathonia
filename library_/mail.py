"""------------------------------------------------------------------------------------------
    Functions or pupose:-
        * It is responding for mail related work not for notification pusher
        * It will send mail synchronously by send through 'synch_mail' located in lathonia folder

    construction:-
        * As usual default args or params or vars
        * empty initialization
        function expalantion:-
        mailer:-
            * radom gen is used to create a random numbers from 111111 to  999999 :return OTP
            * mailer - respected args should be initialized
                * queries has been initialized
                * verfication
                *  ,respected flags will be :return
        for corresponding condition   .if 0 synch_send will happen
        synch_send:-
            *socket connection will happen after then it will send data to respected server .


    confusions:-
        * synch_send sokcets

------------------------------------------------------------------------------------------"""

import smtplib
import pymysql
import  json
import socket
import random
from lathonia.library_ import sql,queries,lib,Exceptor
db_ =sql.sql()
login_username = "srirammaus1@gmail.com"
login_password = "------"
user_id = login_username.strip()
pwd = login_password.strip()
host='127.0.0.1'
port=4444
class mail:
    def __init__(self,*args):
        pass
    def Random_generator(self):
        self.rd =random.randrange(111111,999999)
        return self.rd
    def mailer(self,username,mail_id):
        self.username =username.strip()
        self.mail_id = mail_id.strip()
        # self.flag
        query = queries.queries(self.username)
        # db = db_.function()
        # if db != -1 :
        verify =query.verfication(self.username, self.mail_id)
        if verify == 1:
            flag = 2  #1 or 2 is the proper Return value which should be used in if condition
            print("The Re-Attempt From This Ip : " )
        elif verify == 0:
            rd = self.Random_generator()
            print("This is Present Random Generated number =>" + str(rd))
            print("This is the Mail id i got From Request =>" +str(mail_id))
            mailid = str(mail_id.strip())
            print("The Stringedd Mail_id => " +mailid)
            if query.updater(self.username,self.mail_id,str(rd)) == 1:
                # flag = 1
                # mailing = lib.mailing(user_id,pwd,self.mail_id,rd)
                if self.sync_send(self.username,self.mail_id,otp= str(rd)) == 1:
                    flag =1
                else:
                    flag =1
            else:
                flag = -2
        elif verify == -1 or verify== -2 or verify == -3:
            raise Exceptor.LoginUserException()
        else:
            raise Exceptor.ISE()
        # else:
        #     flag = -4

        return flag

    def mail_activater(self,username,mail_id,otp):
        self.username = str(username).strip()
        self.mail_id = str(mail_id).strip()
        # self.conn = db_.function()
        self.otp = str(otp).strip()
        try:
            # with self.conn.cursor() as cursor:
            self.conn = db_.function()
            cursor = self.conn.cursor()
            print("I tried")
            query = "SELECT `mail_token` FROM `users` WHERE `mail_token`=%s AND `username` = %s AND `mail_id`=%s"
            print("i am here")
            paramters=(self.otp,self.username,self.mail_id)
            cursor.execute(query,paramters)
            res= cursor.fetchall()
            print(res)
            if len(res) > 0:
                if type(res) == list:
                    otp_ = res[0]['mail_token']
                    print("This is OTP => " + str(otp_))
                    if otp_ == self.otp:
                        flag = 1
                    else:
                        flag = -1
                else:
                    flag =-2
            else:
                raise Exceptor.OTP()

        except pymysql.Error as e:
            f = open('logs/mail_err_log.txt','a')
            Err = [{"Error At Mail Activater in Line 87 :  "+ str(e)+"\n\n"}]
            f.write(str(Err))
            f.close()
            raise Exceptor.ISE()
        except Exception as e:
            print("Tyi")
            raise Exceptor.Handler(str(e))
        except:
            f = open('logs/mail_err_log.txt', 'a')
            Err = [{"Unknown Error At Mail Activater in Line 87 :  "  + "\n\n"}]
            f.write(str(Err))
            f.close()
            raise Exceptor.ISE()
        return  flag,self.username,self.mail_id
    def sync_send(self,username,mail_id,otp):
        flag = 0
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            sock.connect((host,port))
            json_={
                "username": username,
                "mail_id":mail_id,
                "otp":otp
            }
            flag =1
        except socket.error as e:
            print(str(e))
            flag = -1
        if flag == 1:
            # s = str(json_)
            j = json.dumps(json_)
            sock.send(bytes(j, 'utf-8'))


        else:
            flag = -1
        return flag
# query.activater(self.username,self.mail_id,self.c)
# print("Failed")
# function("srirammaus@gmail.com")
# self.username, self.mail_id
# sock.send(bytes(0))
# data , addr = sock.recvfrom(1024)
# print(str(data))
# sock.send(bytes(str(json_),'utf-8'))
# if True:
#sock.send(bytes(str(json_), 'utf-8'))
# print(type(j))
# print(j)
# print(s)
# j2 = json.dumps(s)
# print(j2)
