"""------------------------------------------------------------------------------------------
        This is OAuth Library ,uses are below:-
            * To initiate a new Session
            * To get new Session by using old refresh token

        functions:-
            * Deactivating old session
            * Initiate session
            * refresh session
            * Having Own Refresh generator
            * Having Own Acess Ganerator
        Libraries used:-
            * Queries => variable  =>qu = > used as var
            * Exceptor is used
        description:-
            For Refresh :
              * :return values is a tuple containing access,refresh,identity and other possible info
              * if Exception Handler function is removed it will raise a err after then it will caught by except in refresh_
            if it happens then return json will have this err and user will see this .[int object is not subscript-able ]
        function Explanation:-
            * access_generator and refresh_generator is used to create random string which temporary ,will soon i update
            it by my own random geneator or algorithmic generators

            * main- To initiate a new session to Db  :return are result,access,refresh,identity others are exception
            which will caught by API's .

            * access - To check,if valid check then you can ahead with your API -Not in use ,Use when you need .If you
            need to try this jus check create a Worthy APi's use this module you will get :return as code ,if success
            let user to use you service

            * refresh -  return whether users session is active or not by db's own value 0 or 1

            * refresh_ - used to get new session by deactivating old and initiate new session by self.main(**kwargs)
            refresh function is used here to validate !
        Pending:-
            * Access Enhancement !!!
"""
# from lathonia.library_ import queries
import requests
# from random_words import random_words
# from random_word import RandomWords
import random
import string
from lathonia.library_ import queries, Exceptor


class main():
    def __init__(self):
        pass

    def refresh_generator(self, length, username=None, mail_id=None):  # WE WILL OPTIMIZE THIS RANDOM LATER
        if username != None or mail_id != None:
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(length))
            rs = 'r.' + str(result_str)
            result = str(rs)
        else:
            result = "default"
        return result

    def access_generator(self, length, username=None, mail_id=None):
        if username != None or mail_id != None:
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(length))
            rs = 'a.' + str(result_str)
            result = str(rs)
        else:
            result = "default"
        return result

    def main(self, mail_id=None, username=None): #INSERTER
        qu = queries.queries()
        if username != None and mail_id == None:
            var = qu.verfication(username=username)
            if var == 1:
                access = self.access_generator(30, username=username)
                refresh = self.refresh_generator(30, username=username)
                if access != "default" and refresh != "default":
                    access_t = str(access)
                    refresh_t = str(refresh)
                    add_session = qu.session_manager_1(access_token=access_t, refresh_token=refresh_t,
                                                       username=username)
                    if add_session == 1:
                        access_token = str(access)
                        refresh_token = str(refresh)
                        result = 1
                        return result, access_token, refresh_token,username
                    else:
                        raise Exceptor.ISE()
                else:
                    raise Exceptor.ISE()
            elif var == 0:
                raise Exceptor.ActivationErr()
            elif var == -1 or var == -2 or var == -3:
                raise Exceptor.LoginUserException()
            else:
                raise Exceptor.ISE()
        elif username == None and mail_id != None:
            var = qu.verfication(mail_id=mail_id)
            if var == 1:
                refresh = self.refresh_generator(30, mail_id=mail_id)
                access = self.access_generator(30, mail_id=mail_id)
                if access != "default" and refresh != "default":
                    access_t = str(access)
                    refresh_t = str(refresh)
                    add_session = qu.session_manager_1(access_token=access_t, refresh_token=refresh_t,
                                                       mail_id=mail_id)
                    if add_session == 1:
                        access_token = str(access)
                        refresh_token = str(refresh)
                        result = 1
                        return result, access_token, refresh_token,mail_id
                    else:
                        raise Exceptor.ISE()
                else:
                    raise Exceptor.ISE()
            elif var == 0:
                raise Exceptor.ActivationErr()
            elif var == -1 or var == -2 or var == -3:
                raise Exceptor.LoginUserException()
            else:
                raise Exceptor.ISE()
        else:
            raise Exceptor.ISE()
            # return result,access_token,refresh_token

    def access(self, user_access_token, username=None, mail_id=None): #ACCESS VALIDATER
        qu = queries.queries()
        if username != None and mail_id == None:
            try:
                # self.main(username=username)
                getter = qu.session_getter(user_access_token, username)
                if getter[0] == 1:
                    if type(getter[1]) == list:
                        if getter[1] >0:
                            try:
                                access_token = getter[1][0]['access_token']
                                refresh_token = getter[1][0]['refresh_token']
                                # print("ONE" + access_token) return result
                            except Exception as e:
                                raise Exceptor.Handler(str(e))
                            except :
                                raise Exceptor.UnknownErr()
                        else:
                            raise Exceptor.QTypeErr()
                    else:
                        raise Exceptor.LoginUserException()
                else:
                    # print("I am ")
                    raise Exceptor.I_Err()
            except Exception as e:
                # print("I AM")
                raise Exceptor.Handler(str(e))
        elif username == None and mail_id != None:
            try:
                # self.main(username=username)
                getter = qu.session_getter(user_access_token, mail_id=mail_id)
                if getter[0] == 1:
                    c = getter[1]
                    if type(getter[1]) == list:
                        if len(c) > 0:
                            try:
                                access_token = getter[1][0]['access_token']
                                refresh_token = getter[1][0]['refresh_token']
                                # print("TWO" + access_token)
                            except Exception as e:
                                raise Exceptor.Handler(str(e))
                            except:
                                raise Exceptor.UnknownErr()
                        else:
                            raise Exceptor.QTypeErr()
                    else:
                        raise Exceptor.LoginUserException()
                else:
                    # print("I am ")
                    raise Exceptor.I_Err()
            except Exception as e:
                # print("I AM")
                raise Exceptor.Handler(str(e))
        return access_token,refresh_token

    def refresh(self, user_refresh_token, username=None, mail_id=None): #GET ACCES BY REFRESH
        qu = queries.queries()
        if username != None and mail_id == None:
            try:
                # self.main(username=username)
                getter = qu.session_changer_1(user_refresh_token, username)
                if getter[0] == 1:
                    # print("Base")
                    if type(getter[1]) == list:
                        # print("adv")
                        if len(getter[1]) > 0:
                            # print("adv2")
                            try:
                                active = getter[1][0]['active']
                                # print("ONE" + str(active))
                                return active
                            except Exception as e:
                                raise Exceptor.Handler(str(e))
                            except:
                                raise Exceptor.UnknownErr()
                        else:
                            raise Exceptor.QTypeErr()
                    else:
                        raise Exceptor.InvalidSesion()
                else:
                    # print("I am ")
                    raise Exceptor.I_Err()
            except Exception as e:
                print("I AM")
                raise Exceptor.Handler(str(e))
        elif username == None and mail_id != None:
            try:
                # self.main(username=username)
                getter = qu.session_changer_1(user_refresh_token, mail_id=mail_id)
                if getter[0] == 1:
                    c = getter[1]
                    # print(c)
                    if type(getter[1]) == list:
                        if len(c) > 0:
                            try:
                                active = getter[1][0]['active']
                                # print("TWO" + active)
                                return active
                            except Exception as e:
                                raise Exceptor.Handler(str(e))
                            except:
                                raise Exceptor.UnknownErr()
                        else:
                            raise Exceptor.QTypeErr()
                    else:
                        raise Exceptor.LoginUserException()
                else:
                    # print("I am ")
                    raise Exceptor.I_Err()
            except Exception as e:
                # print("I AM")
                raise Exceptor.Handler(str(e))
        else:
            raise Exceptor.UnknownErr()
        # print("I am active"+str(active))
        return active

    def refresh_(self,user_refresh_token,username=None, mail_id=None):
        qu = queries.queries()
        if username != None and mail_id == None:
            try:
                var=self.refresh(user_refresh_token=user_refresh_token,username=username)
                print("i am var "+str(var))
                if var == 1:
                    deactivate =qu.deactivate_session(refresh_token=user_refresh_token,username=username)
                    if deactivate == 1:
                        return self.main(username=username)
                    else:
                        raise Exceptor.ISE()
                else:
                    raise Exceptor.SessionAct()
            except Exception as e:
                raise Exceptor.Handler(str(e))
        elif username == None and mail_id != None:
            # print("hey ther")
            try:
                # print("E")
                var = self.refresh(user_refresh_token=user_refresh_token, mail_id=mail_id)
                # print(str(var))
                if var == 1:
                    deactivate = qu.deactivate_session(refresh_token=user_refresh_token,mail_id=mail_id)
                    if deactivate == 1:
                        return self.main(mail_id=mail_id)
                    else:
                        raise Exceptor.ISE()
                else:
                    raise Exceptor.SessionAct()
            except Exception as e:
                raise Exceptor.Handler(str(e))
        else:
            raise Exceptor.ISE()
# if __name__ == '__main__':
    # # obj = main().main(username="Karthick")
    # # # if obj == "default":
    # # print(str(obj))
    # try:
    #     # obj = main().refresh(user_refresh_token="a.aiellasimclqkljfuuqidwyshxfpsy",mail_id="xx@xx.com")
    #     obj = main().refresh_(user_refresh_token="a.aiellasimclqkljfuuqidwyshxfpsy",mail_id="xx@xx.com")
    # except Exception as E:
    #
    #     # print("zss")
    #     print(E)
    # else:
    #     print("no")
