from flask import Flask, render_template, request, flash, redirect, url_for
from solver import euler_method, midpoint_method, heun_method, rk4_method, rk4_adaptive
from utils import create_plot, create_comparison_plot, save_results_to_csv
import os
import secrets
from math import *
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', secrets.token_hex(16))
app.jinja_env.globals.update(zip=zip)  # Make zip available in all templates

class Config:
    ALLOWED_EQUATION_CHARS = set('0123456789xy+-*/.()^ ')
    ALLOWED_FUNCTIONS = {
        'sin': sin, 'cos': cos, 'tan': tan,
        'exp': exp, 'log': log, 'sqrt': sqrt,
        'pi': pi, 'e': e
    }

def safe_eval_equation(equation):
    """Safely evaluate the ODE equation"""
    if not all(c in Config.ALLOWED_EQUATION_CHARS for c in equation):
        raise ValueError("Invalid characters in equation")
    
    try:
        code = compile(equation, '<string>', 'eval')
        for name in code.co_names:
            if name not in Config.ALLOWED_FUNCTIONS and name not in ['x', 'y']:
                raise ValueError(f"Use of '{name}' not allowed")
        return lambda x, y: eval(code, {'__builtins__': {}}, {**Config.ALLOWED_FUNCTIONS, 'x': x, 'y': y})
    except Exception as e:
        raise ValueError(f"Invalid equation: {str(e)}")

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        # Input validation
        equation = request.form['equation'].strip()
        x0 = float(request.form['x0'])
        y0 = float(request.form['y0'])
        h = float(request.form['h'])
        xf = float(request.form['xf'])
        method = request.form['method']
        compare_methods = request.form.get('compare_methods') == 'on'
        exact_solution = request.form.get('exact', '').strip()
        
        if h <= 0:
            raise ValueError("Step size must be positive")
        if xf <= x0:
            raise ValueError("Final x must be greater than initial x")

        # Safe equation parsing
        f = safe_eval_equation(equation)
        
        # Exact solution parsing if provided
        exact_func = None
        if exact_solution:
            try:
                exact_func = safe_eval_equation(exact_solution)
            except ValueError as e:
                app.logger.warning(f"Exact solution error: {str(e)}")

        # Method handling
        methods_to_run = [method]
        if compare_methods:
            methods_to_run = ['Euler', 'Midpoint', 'Heun', 'RK4', 'RK4 Adaptive']
        
        # Process all selected methods
        results = {}
        for m in methods_to_run:
            if m == "Euler":
                x, y = euler_method(f, x0, y0, h, xf)
            elif m == "Midpoint":
                x, y = midpoint_method(f, x0, y0, h, xf)
            elif m == "Heun":
                x, y = heun_method(f, x0, y0, h, xf)
            elif m == "RK4":
                x, y = rk4_method(f, x0, y0, h, xf)
            elif m == "RK4 Adaptive":
                x, y = rk4_adaptive(f, x0, y0, h, xf)
            else:
                continue
            results[m] = (x, y)

        # Generate plots
        plot_url = create_plot(results[method][0], results[method][1], method, exact_func)
        
        # Add comparison plot if needed
        comparison_plot = None
        if len(results) > 1:
            comparison_plot = create_comparison_plot(results, exact_func)
        
        # Save results
        save_results_to_csv(results[method][0], results[method][1])

        return render_template('index.html', 
                            plot_url=plot_url,
                            comparison_plot=comparison_plot,
                            x_vals=results[method][0],
                            y_vals=results[method][1],
                            method=method,
                            exact_errors=exact_func is not None)

    except ValueError as e:
        flash(str(e), 'error')
        return redirect(url_for('home'))
    except Exception as e:
        flash("An unexpected error occurred", 'error')
        app.logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return redirect(url_for('home'))

if __name__ == '__main__':
    if app.config['SECRET_KEY'].startswith('dev-'):
        print("Warning: Using development secret key - not suitable for production!")
    app.run(debug=True)