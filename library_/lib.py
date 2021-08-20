#LIBRARY FOR NOFICATION PUSHER THROUGH MAIL OR ANYTHING
"""
---------------------------------------------------------------------------------------
    currently it is not in use ,plz don't confuse it with you present code

----------------------------------------------------------------------------------------"""

import smtplib
import asyncio
import socket
import time
from lathonia.library_ import  sql
db_ = sql.sql()
login_username = "srirammaus1@gmail.com"
login_password = "maussriram"
# reciver = "srirammaus1@gmail.com"
def mailing(user_id,pwd,mail_id,rd):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as obj:
            obj.login(user=user_id, password=pwd)
            obj.sendmail(user_id, mail_id, str(rd))
            print("succesfully sent")
            flag = 5

    except:
        print("Port Error")
        flag = -1

class mail_manager():
    #Listening Mode:
    def __init__(self,username = None,user_mail_id=None,reciever=None,ip_address=None):
        self.global_array=[]
        self.username = username
        self.mail_id = user_mail_id
        self.ip = ip_address
        self.reciever = reciever
        self.count = 0
        self.UDP()
        loop = asyncio.get_event_loop()
        try:
            asyncio.ensure_future(self.main_mailer())
            loop.run_forever()
        except KeyboardInterrupt as e:
            print(str(e))

    def UDP(self):
        try:
            socket_  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            print(socket.gethostname())
            socket_.bind(('127.0.0.1',4444))
            # socket_.listen()
            print("Tried")
        except socket.error as e:
            print(str(e))

        while True:
            print("Listening")
            data, addr = socket_.recvfrom(1024)
            print(str(data)+str(addr))
            time.sleep(1)
            socket_.close()
            self.UDP()
    async def main_mailer(self,recvv=None):
        while True:
            if recvv != None: #self.username != None and self.mail_id !=None
                self.count +=1
                mailing(login_username, login_password,recvv,"The Message New Number "+str(self.count))
                await asyncio.sleep(1)
            else:
                await asyncio.sleep(1)
                print("HAPPENED")
                self.main_mailer()
            # print("passing")

# if __name__ == '__main__':
#     mail_manager()#'username','string'

# We can Store it in DB and checking it continuos=usly by activity status if not put it in sleep