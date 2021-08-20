""" ------------------------------------------------------------------------------------------
            * This is to get new session by deactivating old session by using oauth_lib module which will
        provide return as new session info.Proper return code number is still pending.

        Modules Used:-
            oauth-lib => varible => O_auth =>var
------------------------------------------------------------------------------------------"""
from lathonia.library_ import Exceptor,oauth_lib
from flask import request,Response
def OAuth():
    args = request.args
    args_keys=request.args.keys()
    List = ['username', 'refresh_token']
    List1 = ['mail_id', 'refresh_token']
    List2= list(args_keys)
    cmp1 = set(List)
    cmp2 =set(List1)
    cmp3 = set(List2)
    if len(args_keys) == 2:
        if cmp1 == cmp3:
            try:
                username = args['username']
                refresh_token = args['refresh_token']
                O_auth = oauth_lib.main()
                var= O_auth.refresh_(username=username,user_refresh_token=refresh_token)
                # print(str(var[0]))
                if var[0] == 1:
                    json_=[{
                        "status":var[0],
                        "access_token":var[1],
                        "refresh_token":var[2],
                        "Username or E-mail":var[3]
                    }]
                    return Response(str(json_),200)
                else:
                    json_ = [{
                        "Error":"Server Error",
                        "Code":-1
                    }]
                    return Response(str(json_), 200)
            except Exception as e:
                json_ = [{
                    "Error":str(e),
                    "Code":-1
                }]
                return Response(str(json_),200)
            except:
                json_ = [{
                    "Error":"Something Went Wrong ,Try Again...",
                    "Code":-2
                }]
                return Response(str(json_),200)
        elif cmp2 == cmp3:
            try:
                mail_id = args['mail_id']
                refresh_token = args['refresh_token']
                O_auth = oauth_lib.main()
                var= O_auth.refresh_(mail_id=mail_id,user_refresh_token=refresh_token)
                # print(str(var[0]))
                if var[0] == 1:
                    json_=[{
                        "status":var[0],
                        "access_token":var[1],
                        "refresh_token":var[2],
                        "Username or E-mail":var[3]
                    }]
                    return Response(str(json_),200)
                else:
                    json_ = [{
                        "Error":"Server Error",
                        "Code":-1
                    }]
                    return Response(str(json_), 200)
            except Exception as e:
                json_ = [{
                    "Error":str(e),
                    "Code":-1
                }]
                return Response(str(json_),200)
            except:
                json_ = [{
                    "Error":"Something Went Wrong ,Try Again...",
                    "Code":-2
                }]
                return Response(str(json_),200)
        else:
            json_=[{
                "Error" : "Invalid Arguments",
                "code" : -1
            }]
            return Response (str(json_),406)

    else:
        json_ = [{
            "Error": "Invalid Arguments",
            "code": -1
        }]
        return Response(str(json_), 406)