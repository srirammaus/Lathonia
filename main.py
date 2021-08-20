"""---------------------------------------------------------------------------------------
         The main class is used to run corresponding program belongs to the user's http request and it will

provide proper response by the cor
------------------------------------------------------"""
from lathonia.library_ import otp,signup,login,OAuth
from flask import Flask
import subprocess
print("done")
app = Flask(__name__)
@app.route('/signup',methods=['GET'])
def sign_up():
    return signup.signup()
@app.route('/get_otp',methods=['GET'])
def get_otp():
    return otp.otp()

@app.route('/validate',methods=['GET'])
def validate():
    return otp.validate()
@app.route('/signin',methods=['GET'])
def signin():

    return login.login()
@app.route('/OAuth/refresh',methods=['GET'])
def OAuth_refresh():
    # return oauth
    return OAuth.OAuth()

if __name__ == '__main__':
    # subprocess.call(['python', 'synch_mail.py'])
    # subprocess.call('dir && where python && set path = r"C:\\Users\srira\PycharmProjects\pythonProject4\venv\Scripts" && python synch_mail.py',shell=True)
    app.run()