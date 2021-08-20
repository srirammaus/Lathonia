"""------------------------------------------------------------------------------------------
            Handle Request and Response using flask module and verifying it with corresponding library like login_lib!

Code number for each response is still pending !if you are using in production kindly requesting you to plz check

 code number or append your code with it by updating this login.py and corresponding library
------------------------------------------------------------------------------------------
"""
from lathonia.library_ import login_lib
from flask import *

# db_ = sql.sql()
login_  = login_lib.login()
def login():
    """
    :Using: Libraries and their location:

        login_lib - library_ = variable used here is 'login_' to initiate and to run you have used 'var'

    :return:
    """
    argumnets = request.args
    argumnets_keys = argumnets.keys()
    List = ['username', 'password']
    List1 = ['mail_id','password']
    # List2 = ['mobile_number','password'] For Now It is Optional
    List3 = list(argumnets_keys)
    cmp1 = set(List)
    cmp2 = set(List1)
    cmp3 = set(List3)
    if len(argumnets) == 2:
        if cmp1 == cmp3:
            username = argumnets['username']
            password = argumnets['password']
            try:
                var = login_.login(password,username=username)
                if var[0] == 1:
                    # flag = 1
                    json_ = [{
                        "access_key":var[1],
                        "refresh_key":var[2],
                        "Username or Email":var[3],
                        "status": "Success",
                        "Code":1
                    }]
                    return Response(str(json_), 200)
                else:
                    json_ = [{
                        "status": "Server Error"
                    }]
                    return Response(str(json_), 200)
            except Exception as e:
                print(str(e))
                json_=[{
                    "Error":str(e),
                    "code": 0
                }]
                return Response(str(json_), 200)
            except:
                json_ = [{
                    "Status": "something went wrong",
                    "code": -2
                }]
                return Response(str(json_), 406)

        elif cmp2 == cmp3:
            mail_id = argumnets['mail_id']
            password = argumnets['password']
            try:
                var = login_.login(password,mail_id = mail_id)
                if var[0]==1:
                    json_ = [{
                        "access_key": var[1],
                        "refresh_key": var[2],
                        "Username or Email": var[3],
                        "status": "Success",
                        "Code": 1
                    }]
                    return Response(str(json_), 200)
                else:
                    json_ = [{
                        "status": "Server Error",
                        "code": - 1
                    }]
                    return Response(str(json_), 200)
            except Exception as e:
                # print(e)
                json_ = {
                    "status": str(e),
                    "code": 0
                }
                return Response(str(json_),200)
            except :
                json_ = [{
                    "Status": "something went wrong",
                    "code" : -2
                }]
                return Response(str(json_),406)

        else:
            json_={
                "status":"Invalid Parmaters",
                "code":-3
            }
            return Response(str(json_),406)
    else:
        json_={
            "status":"Arguments Failed",
            "code": -4
        }
        return Response(str(json_),406)
    # if flag == 1:
    #     # json_ = [{
    #     #     "status": "logged in"
    #     # }]
    #     # return Response(str(json_),200)
    # else:
    #     json_ = [{
    #         "status" : "not verified"
    #     }]
    #     return Response(str(json_),200)