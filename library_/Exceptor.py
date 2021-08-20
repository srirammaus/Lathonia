"""--------------------------------------------------------------------------------------------------------
    * This Class is used for Exception Handling .All the Exceptions should be store here
--------------------------------------------------------------------------------------------------------"""

class LoginUserException(Exception):
    def __init__(self):
        self.ErrMsg = "User Does Not Exists"
    def __str__(self):
        return self.ErrMsg
class ActivationErr(Exception):
    def __init__(self):
        self.ErrMsg="Your Acc Wasn't Activated"
    def __str__(self):
        return self.ErrMsg
class ISE(Exception):
    def __init__(self):
        self.ErrMsg1= "Server Error"
    def __str__(self):
        return self.ErrMsg1
class InfoError(Exception):
    def __init__(self):
        self.ErrMsg= "User Info Got None"
    def __str__(self):
        return self.ErrMsg
class DupException(Exception):
    def __init__(self):
        self.ErrMsg="Username Has Already Taken"
    def __str__(self):
        return self.ErrMsg
class Handler(Exception):
    def __init__(self,Err):
        self.ErrMsg = Err
    def __str__(self):
        return self.ErrMsg
class UnknownErr(Exception):
    def __init__(self):
        self.ErrMsg = "Something Went Wrong"
    def __str__(self):
        return self.ErrMsg
class QTypeErr(Exception):
    def __init__(self):
        self.ErrMsg = "QTErr ,Something Went Wrong"
    def __str__(self):
        return self.ErrMsg
class I_Err(Exception):  #Index error if number greater than or lesser than
    def __init__(self):
        self.ErrMsg = "I_Err,Something Went Wrong"
    def __str__(self):
        return self.ErrMsg
class SessionAct(Exception):
    def __init__(self):
        self.ErrMsg = "Session already DeActivated"
    def __str__(self):
        return self.ErrMsg
class PasswordIncorrect(Exception):
    def __init__(self):
        self.ErrMsg = "Password Incorrect"
    def __str__(self):
        return self.ErrMsg
class InvalidSesion(Exception):
    def __init__(self):
        self.ErrMsg = "User's Session Invalid or User's Session Does not Exists"
    def __str__(self):
        return self.ErrMsg
class OTP(Exception):
    def __init__(self):
        self.ErrMsg = "Authentication failed,Invalid Credentials!"
    def __str__(self):
        return self.ErrMsg
# class VerfiacationException(Exception):
#     def __init__(self):
#         self.ErrMsg=""