"""------------------------------------------------------------------------------------------
        API - Usage :-
            *To signup
        required args:-
            * username
            * password
            * mobile number
            * mail
            * name
        Modules used :-
            * signup_lib=>sq => insert

        pending:-
            * Code Values are still pending i.e[1,2,3,-1,-2] and http codes are also pending
------------------------------------------------------------------------------------------"""
from flask import *
from lathonia.library_ import queries,signup_lib

def signup():
    IP_ADDR=request.remote_addr
    argumnets = request.args
    argumnets_keys = argumnets.keys()
    List = ['username','name', 'password', 'mobile_number', 'mail_id']
    List2 = list(argumnets_keys)
    cmp1 =set(List)
    cmp2=set(List2)
    if len(argumnets) == 5:
        if cmp1 == cmp2:
            # query_ = queries.queries(str(IP_ADDR))
            name=argumnets['name']
            username=argumnets['username']
            password=argumnets['password']
            mobile_number=argumnets['mobile_number']
            mail_id=argumnets['mail_id']
            try:
                sq=signup_lib.signup()
                Insert = sq.insert(name, username, password, mobile_number, mail_id,ip_addr=str(IP_ADDR))
                if Insert == 1:
                    json_ = [{
                        "status": "profile inserted",
                        "Code":1
                    }]
                    return Response(str(json_), 200)
                else:
                    json_ = [{
                        "status": "Internal Sever Error",
                        "Code":-1
                    }]
                    return Response(str(json_), 406)
            except Exception as e:
                json_ = [{
                    "Status":str(e),
                    "code" : 0
                }]
                return Response(str(json_),406)
            except :
                json_ = [{
                    "Status": "something went wrong"
                }]
                return Response(str(json_),406)
        else:
            json_ = [{
                "status": "parameters name invalid",
                "Code":0
            }]
            return Response(str(json_),406)
    else:
        json_=[{
            "status":"not enough arguments",
            "Code" : 0
        }]
        return Response(str(json_),406)

# app=Flask(__name__)
# @app.route('/get_otp',methods=['GET'])
# def func():
#     return  otp.otp()
# @app.route('/signup',methods=['GET'])
#
# if __name__ == '__main__':
#     app.run()
# --------------------------------------------GARBAGE-----------------------------------------------
# username=request.args['username']
    # password=request.args['password']
    # mobile_number=request.args['mobile_number']
    # mail_id=request.args['mail_id']
    # List.append(name)
    # List.append()
# app = Flask(__name__)
#app.route('/videos/<string_>') -- Gonna use in videos API
# def dict_keys_(dict):
#     return dict.keys()
# print( list(pair.values()))
# print(jsonify(request.args))
#print(json.dumps(request.args))
        #print("This is request args ".format(request.args))
# elif 'username' and 'name'and 'password'and 'mobile_number'and 'mail_id'and 'instagram' in argumnets:
            #     object_ = queries(argumnets['username'])
            #     name = argumnets['name']
            #     username = argumnets['username']
            #     password = argumnets['password']
            #     mobile_number = argumnets['mobile_number']
            #     mail_id = argumnets['mail_id']
            #     instagram = argumnets['instagram']
            #     Insert = object_.insert(name, username, password, mobile_number, mail_id,instagram = instagram)
            # elif 'username' and 'name' and 'password' and 'mobile_number' and 'mail_id' and 'twitter' in argumnets:
            #     object_ = queries(argumnets['username'])
            #     name = argumnets['name']
            #     username = argumnets['username']
            #     password = argumnets['password']
            #     mobile_number = argumnets['mobile_number']
            #     mail_id = argumnets['mail_id']
            #     twitter = argumnets['twitter']
# result = all(1 ==1 for List in List2)
# query_.insert(name, username, password, mobile_number, mail_id)