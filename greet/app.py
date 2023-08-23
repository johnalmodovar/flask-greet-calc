from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    """ Returns "welcome" """

    return "<html><body><h1>Welcome!</h1></body></html>"

@app.get("/welcome/home")
def welcome_home():
    """ Returns "welcome home" """

    return "<html><body><h1>Welcome Home!</h1></body></html>"

@app.get("/welcome/back")
def welcome_back():
    """ Returns "welcome back" """

    return "<html><body><h1>Welcome Back!</h1></body></html>"