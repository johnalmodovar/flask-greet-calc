# Put your app in here.
from flask import Flask

app = Flask(__name__)

from flask import request

from operations import add, sub, mult, div



@app.get('/add')
def add_nums():
    """add the two provided numbers"""
    print(request.args)
    term1 = int(request.args["a"])
    term2 = int(request.args["b"])
    answer = add(term1, term2)

    return str(answer)

@app.get('/sub')
def sub_nums():
    """subtract the two provided numbers"""
    print(request.args)
    term1 = int(request.args["a"])
    term2 = int(request.args["b"])
    answer = sub(term1, term2)

    return str(answer)

@app.get('/mult')
def mult_nums():
    """multiply the two provided numbers"""
    print(request.args)
    term1 = int(request.args["a"])
    term2 = int(request.args["b"])
    answer = mult(term1, term2)

    return str(answer)

@app.get('/div')
def div_nums():
    """divide the two provided numbers"""
    print(request.args)
    term1 = int(request.args["a"])
    term2 = int(request.args["b"])
    answer = div(term1, term2)

    return str(answer)



