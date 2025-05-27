import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # make sure this includes or extends form.html

def euler_method(f_str, x0, y0, xf, h):
    steps = []
    try:
        # Safely evaluate the function string
        f = lambda x, y: eval(f_str, {
            "x": x, "y": y,
            "sin": math.sin, "cos": math.cos,
            "exp": math.exp, "log": math.log,
            "sqrt": math.sqrt, "pow": pow,
            "__builtins__": {}
        })

        x = x0
        y = y0
        while x <= xf:
            steps.append((round(x, 4), round(y, 4)))
            y = y + h * f(x, y)
            x = x + h

        return steps
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/solve', methods=['POST'])
def solve():
    try:
        x0 = float(request.form['x0'])
        y0 = float(request.form['y0'])
        h = float(request.form['h'])
        xf = float(request.form['xf'])
        equation = request.form['equation']
        method = request.form['method'].strip().lower()

        if method == "euler":
            result = euler_method(equation, x0, y0, xf, h)
            if isinstance(result, str):  # error message
                return result
            return f"<h2>Euler's Method Result:</h2>" + "<br>".join([f"x = {x}, y = {y}" for x, y in result])
        else:
            return "Only Euler method is supported for now. More coming soon."
    except Exception as e:
        return f"Input Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
