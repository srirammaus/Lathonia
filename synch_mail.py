#CHECK STR
#VALIDATE BY TRY EXCEP IN JSON DECODER
"""---------------------------------------------------------------------------------------------------
    * Run this as seperate server concurrently while pur main.py [Flask] server running , it will maange
all the mail related stuffs
    mailing:-
        * For Sending mail
    synch_mail:-
        * Server Socket
--------------------------------------------"""
from lathonia.library_ import queries
import socket,threading
import sys
import smtplib
import json
import time
login_username = "srirammaus1@gmail.com"
login_password = "maussriram"
user_id_ = login_username.strip()
pwd_ = login_password.strip()
host= '127.0.0.1'
port=4444
def mailing(username ="username",mail_id = "email" ,rd = "otp",user_id = user_id_,pwd = pwd_):
    flag = 0
    try:
        obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        obj.login(user=user_id, password=pwd)
        obj.sendmail(user_id, mail_id, str(rd))
        print("succesfully sent")
        flag = 1
    except socket.gaierror as e:
        f = open('logs/mail_err_log.txt', "a")
        f.write("Mail_Error _GiaErr=>" + str(e) + "\nDate Time :" + str(time.ctime(time.time())) + "\n\n")
        f.close()
        flag = -1
    except smtplib.SMTPConnectError as e:
        f = open('logs/mail_err_log.txt',"a")
        f.write("Mail_Error =>"+str(e)+"\nDate Time :"+str(time.ctime(time.time()))+"\n\n")
        f.close()
        flag = -1
    except smtplib.SMTPDataError as e:
        f = open('logs/mail_err_log.txt', "a")
        f.write("Mail_Error =>" + str(e)+"\nDate Time :"+str(time.ctime(time.time()))+"\n\n")
        f.close()
        flag = -1
    except :  #smtplib.SMTPConnectError as e
        f = open('logs/mail_err_log.txt', "a")
        f.write("Unknown Mail_Error =>" +"\n\n")
        f.close()
        flag = -1
    finally:
        mail_update = queries.queries(username)
        mail_update.mail_updater(username,mail_id,rd,flag)


class synch_mail():
    # ALLOWED IP'S SHOULD BE LIMITED
    # IP_1 = '127.0.0.1'
    # ALLOWED_IP = [IP_1]
    # ALLOWED_ARGS=['username','mail_id']
    def __init__(self):
        self.IP_1 = '127.0.0.1'
        self.ALLOWED_IP = [self.IP_1]
        self.ALLOWED_ARGS = ['username', 'mail_id','otp']
        self.loaded = 0
        self.type_len_flag = 0
        self.UDP()
    def UDP(self):
        flag =""
        e=""
        self.e = e
        try:
            socket_  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            socket_.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            socket_.bind(('127.0.0.1',4444))
            flag = 1
            print("Bound")
            f = open('logs/socket_log.txt', "a")
            f.write("Socket Enable at =>"+str(time.ctime(time.time()))+"\n\n")
            f.close()
        except socket.error as er:
            self.e = er
            f = open('logs/socket_log.txt', "a")
            f.write("Error in Socket => " + str(er)+"\nDate Time :"+str(time.ctime(time.time()))+"\n\n")
            f.close()
            time.sleep(1)
            self.UDP()
        except:
            f = open('logs/socket_log.txt', "a")
            error = [{
                "Unknown Error Happened in socket line 61": host
            }]
            f.write(str(error)+"\nDate Time :"+str(time.ctime(time.time()))+"\n\n")
            f.close()
            time.sleep(1)
            self.UDP()
        while flag ==1:
            print("Listening")  # str(sys.getrecursionlimit())
            data, addr = socket_.recvfrom(1024) #put try here also while buffer gets exceeded #IF HAPPEND IT WILL COME HERE AGAIN
            if self.len_calc(data) == 1:
                    # break
                    # time.sleep(.5)
                    # self.UDP()
                    # self.type_len_flag = 1
                    print("continuing")
                    continue
            else:
                data_ = data.decode('utf-8')
                print(len(data))
                print(type(data_))
                try:
                    json_ = json.loads(data_)
                    self.loaded = 1
                except json.decoder.JSONDecodeError as e:
                    if e != "":
                        print(str(e))
                        continue
                    else:
                        pass
                    # self.UDP()
                    # break
                if self.loaded == 1:
                    li = list(json_.keys())
                    cmp = set(li)
                    cmp1 =set(self.ALLOWED_ARGS)
                    if cmp == cmp1:
                        mailing(json_['username'], json_['mail_id'],json_['otp'])
                        self.temp(json_['username'], json_['mail_id']) # ,json_['otp']while take care without recursion
                    else:
                        pass

                    print(li)

                else:

                    # self.UDP()
                    continue #instead of pass it is better


        # if flag == 1:
        #     print("Listening" )  #str(sys.getrecursionlimit())
        #     data, addr = socket_.recvfrom(1024)
        #     data_ = data.decode('utf-8')
        #     json_= json.loads(data_)
        #     self.temp(json_['username'],json_['mail_id'])
        #     time.sleep(1)
        #     socket_.close()
        #     self.UDP()
        # else:
        #     # self.UDP()
        #     # print(self.e)
        #     time.sleep(1)
        #     self.UDP()

    def temp(self,username = None,mail_id =None):
        if username != None and mail_id != None:
            print(str(username))
            print(str(mail_id))
        else:
            pass
    def len_calc(self,data):
        if len(data) == None or len(data) == 0 or data == "":
            flag = 1
        else:
            flag = 0
        return  flag
if __name__ == '__main__':
    synch_mail()
# flag = ''
# try:
#     sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     sock.bind((host,port))
#
#     flag = 1
#     print("Bound")
# except socket.error as e:
#     print(str(e))
# if flag == 1:
    # sock.listen()
    # sock.accept()
    # data , addr = sock.recvfrom(1024)
    # print(sock.getsockname())
    # print(sock.getpeername())
#     print("Bonded ")
# else:
#     print("Abprted")
# socket_.listen()
# print(socket.gethostname())
 # socket_.sendto(bytes("messgae",'utf-8'),addr)
# json__ = json.dumps(json_)
# print(json_['username'])
# print(json_['mail_id'])
# print(type(json_))
# str_data = str(data.decode('utf-8'))
# li=list(str_data)
# print(type(li))
# print(li[0])
# print(len(data))
# # print(type(data_))
# # print(type(data))
# li= list(json_.values())  #check type