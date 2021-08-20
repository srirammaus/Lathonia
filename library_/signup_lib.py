"""------------------------------------------------------------------------------------------
    Function Usage or purpose:-
        * Inserting Valid users to our DB
    function explanation:
        * insert - initiating args and queries module , start checking whether anyother users in same username or email
         then it will [var] return valus as -1 and if not then it will return values as 1 .ater then it will try insert
         users into db it will not activate by it own ,front end should call get otp by other API's ,you can also
         customize it by having a redirection to get otp .

------------------------------------------------------------------------------------------"""
from lathonia.library_ import sql,queries,Exceptor
import pymysql,time
db_=sql.sql()
class signup:
    def insert(self, name, username, password, mobile_number, mail_id, active=0,ip_addr="default"):
        self.name = name
        self.username = username
        self.password = password
        self.mobile_number = mobile_number
        self.mail_id = mail_id

        self.active = active
        # db = db_.function()
        # if db == -1:
        #     result = -3
        # else:
        qu = queries.queries(str(ip_addr))
        var = qu.dup_checker(self.username,self.mail_id)
        if var == 1 or var == 2:
            try:
                # with db.cursor() as cursor:
                db = db_.function()
                cursor = db.cursor()
                query = "INSERT INTO `users`(`name`, `username`, `password`, `mobile_number`, `mail_id`, `active`) VALUES (%s,%s,%s,%s,%s,%s)"
                parameters = (self.name, self.username, self.password, self.mobile_number, self.mail_id, self.active)
                cursor.execute(query, parameters)
                db.commit()
                result = 1

            except pymysql.Error as e:  # GET ERROR BY PYMYSQL.ERROR BUT THAT IS NOT NECESSARY
                f = open('logs/error.log.txt', 'a')
                f.write("[Error Handler : {Inserter Error  234:" + str(e) + "}\nDate Time : {" + str(
                    time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
                f.close()
                raise Exceptor.ISE()
            except:
                f = open('logs/error.log.txt', 'a')
                f.write("[{Unexpected Unknown error occured in Inserter Error  240 }" + "\nDate Time :  {" + str(
                    time.ctime(time.time())) + "}\nIP_ADDR :" + self.ip + "\nUsername : " + self.username + "]\n\n")
                f.close()
                raise Exceptor.ISE()
        elif var == -1:
            raise Exceptor.DupException()
        else:
            raise Exceptor.ISE()

        return result