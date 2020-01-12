from flask import Flask, request
from fractions import Fraction
from decimal import Decimal
app = Flask(__name__)
@app.route('/')
def index():
    return 'Usage;\nOperation?A=<First_Value>&B=<Second_Value>\n'

@app.route('/add')
def Addition():
    try:
        First_Value=request.args.get('A',default = 0, type = Fraction)
    except ZerodivisionError as error:
        First_Value='None'
    try:
        Second_Value=request.args.get('B',default = 0, type = Fraction)
    except ZerodivisionError as error:
        Second_Value='None'
    if First_Value == 'None' or Second_Value == 'None' :
        return 'None'
    else:
        n = Fraction(First_Value)
        d = Fraction(Second_Value)
        result = n+d
        return str(float(result))#removed round funntion and results in float

@app.route('/sub')
def Subtraction():
    try:
        First_Value=request.args.get('A',default = 0, type = Fraction)
    except ZerodivisionError as error:
        First_Value='None'
    try:
        Second_Value=request.args.get('B',default = 0, type = Fraction)
    except ZerodivisionError as error:
        Second_Value='None'
    if First_Value == 'None' or Second_Value == 'None' :
        return 'None'
    else:
        n = Fraction(First_Value)
        d = Fraction(Second_Value)
        result = n-d
        return str(float(result))


@app.route('/mul')
def Multiplication():
    try:
        First_Value=request.args.get('A',default = 0, type = Fraction)
    except ZerodivisionError as error:
        First_Value='None'
    try:
        Second_Value=request.args.get('B',default = 0, type = Fraction)
    except ZerodivisionError as error:
        Second_Value='None'
    if First_Value == 'None' or Second_Value == 'None' :
        return 'None'
    else:
        n = Fraction(First_Value)
        d = Fraction(Second_Value)
        result = n*d
        return str(float(result))

@app.route('/div')
def division():
    try:
        First_Value=request.args.get('A',default = 0, type = Fraction)
    except ZerodivisionError as error:
        First_Value='None'
    try:
        Second_Value=request.args.get('B',default = 0, type = Fraction)
    except ZerodivisionError as error:
        Second_Value='None'
    if First_Value == 'None' or Second_Value == 'None' :
        return 'None'
    else:
        n = Fraction(First_Value)
        d = Fraction(Second_Value)
        try:
            result = n/d
            return str(float(result))
        except ZerodivisionError as error:
            return 'None'

if __name__ == "__main__":
    app.run()
