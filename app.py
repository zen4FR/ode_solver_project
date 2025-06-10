from flask import Flask, render_template, request
from solver import euler_method
from utils import create_plot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/solve', methods=['POST'])
def solve():
    # Grab input values from the form
    equation = request.form['equation']
    x0 = float(request.form['x0'])
    y0 = float(request.form['y0'])
    h = float(request.form['h'])
    xf = float(request.form['xf'])
    method = request.form['method']

    # Convert equation to a function
    f = eval("lambda x, y: " + equation)
    
    # Call Euler method
    if method == "Euler":
        x_vals, y_vals = euler_method(f, x0, y0, h, xf)
    else:
        x_vals, y_vals = [], []  # Placeholder for future methods

    # Create plot
    plot_url = create_plot(x_vals, y_vals, method)
    
    # Save results to CSV (exports/results.csv)
    with open('exports/results.csv', 'w') as file:
        file.write("x,y\n")
        for x, y in zip(x_vals, y_vals):
            file.write(f"{x},{y}\n")
    #above point we add to make the zip point working for the image and the output
    return render_template('index.html', plot_url=plot_url, x_vals=x_vals, y_vals=y_vals, zip=zip)
    # problem occur in this related to jinja2thing
    # return render_template('index.html', plot_url=plot_url, x_vals=x_vals, y_vals=y_vals)

if __name__ == '__main__':
    app.run(debug=True)
