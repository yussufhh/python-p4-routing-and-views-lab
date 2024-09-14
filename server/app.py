from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_param(param):
    print(param)
    return param

@app.route('/count/<int:num>')
def count(num):
    # Ensure the final result ends with a newline character
    return '\n'.join(str(i) for i in range(num)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    # Handle both operation names and symbols
    if operation == 'add' or operation == '+':
        result = num1 + num2
    elif operation == 'subtract' or operation == '-':
        result = num1 - num2
    elif operation == 'multiply' or operation == '*':
        result = num1 * num2
    elif operation == 'divide' or operation == '/':
        result = num1 / num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == 'mod' or operation == '%':
        result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(debug=True)
