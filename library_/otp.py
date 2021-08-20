"""-----------------------------------------------------------------------------------------

    Functions or purpose:-
        * will send OTP while request happening
        * validate by mail.py module's mail activater and OTP is get activate by using query.activater
    construction of this API:-
        * As usual init and then required parms or args were given ,then functions are given below.
        OTP():
            * Mail using mailer {[mail.py in library_]-> will validate whether user exists or not}!
        VALIDATE():
            * validate by mail.py module's mail activater
            *OTP is get activate by using query.activater
        pending works:
            * Code Values are still pending i.e[1,2,3,-1,-2] and http codes are also pending
-----------------------------------------------------------------------------------------"""
from lathonia.library_ import sql,queries,mail
db_ = sql.sql()
query = queries.queries('srirammaus')
from flask import *
mailer = mail.mail()
def otp ():
    args = request.args
    args_keys = args.keys()
    args_key = list(args_keys)
    checker_ = ['username','mail_id']
    cmp = set(checker_)
    cmp1 = set(args_key)
    len_args =len(args)
    if len_args == 2:
        if cmp == cmp1:
            username =args['username']
            mail_id=args['mail_id']
            # otp = args['otp']
            try:
                send = mailer.mailer(username,mail_id)
                if send == 1:
                    json_=[{
                        "status": "your otp was sent "
                    }]
                    return Response(str(json_),200)
                elif send == 2:
                    json_ = [{
                        "status": "already verified "
                    }]
                    return Response(str(json_), 200)
                else:
                    json_ = [{
                        "error": "something went wrong"
                    }]
                    return Response(str(json_), 302)
            except Exception as e:
                json_=[{
                    "Error":str(e)
                }]
                return  Response(str(json_),302)
            except:
                json_ = [{
                    "error": "something went wrong"
                }]
                return Response(str(json_),302)
        else:
            json_ = [{
                "error": "Invalid Arguments"
            }]
            return Response(str(json_), 406)
    else:
        json_ = [{
            "error" : "Invalid Arguments"
        }]
        return Response(str(json_),406)

def validate():
    args = request.args
    args_keys = args.keys()
    args_key = list(args_keys)
    checker_ = ['username', 'mail_id','otp']
    cmp = set(checker_)
    cmp1 = set(args_key)
    len_args = len(args)
    if len_args ==3:
        if cmp ==cmp1:
            username=args['username']
            mail_id=args['mail_id']
            otp=args['otp']
            try:
                validater = mailer.mail_activater(username,mail_id,otp)
                if validater[0] == 1 :
                    # db = db_.function()
                    verification_status =query.activater(validater[1],validater[2])
                    if verification_status == 1:
                        json_=[{
                            "status": "verified"
                        }]

                        return  Response(str(json_),200)
                    else:
                        json_ = [{
                            "status" : "server error"
                        }]
                        return Response(str(json_),500)
                else:
                    json_ = [{
                        "status": "invalid"
                    }]
                    return Response(str(json_), 200)
            except Exception as e:
                json_=[{
                    "Error":str(e),
                    "Code": -1
                }]
                return Response(str(json_),406)
            except:
                json_=[{
                    "Error":"Something Went Wrong",
                    "code":-1
                }]
                return Response(str(json_),406)
        else:
            json_ = [{
                "status": "invalid arguments"
            }]
            return Response(str(json_), 200)
    else:
        json_ = [{
            "status": "invalid arguments"
        }]
        return Response(str(json_), 200)


# @app.route('/validate',methods=['GET'])
# app = Flask(__name__)
# @app.route('/get_otp',methods = ['GET'])
# if __name__ == '__main__':
#     app.run()
# if query.verfication('srirammaus','xx@xx.com',db_.function()) == 1:
#     print("i am Back")
# elif query.verfication('srirammaus','xx@xx.com',db_.function()) == -1:
#     print("i am 0 now")