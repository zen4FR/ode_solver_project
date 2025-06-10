# ODE Solver Web Application

## Overview
This project is a web-based Ordinary Differential Equation (ODE) solver built with Python Flask. It currently supports Euler’s method for solving first-order ODEs and provides graphical and tabular results.

## Features
- Input any first-order ODE in the form `dy/dx = f(x,y)` via a user-friendly web form.
- Specify initial conditions (x0, y0), step size (h), and final x value.
- Generates solution plot dynamically using Matplotlib.
- Displays results in a well-formatted table.
- Allows saving results to CSV (`exports/results.csv`).
- Responsive and clean UI with CSS styling.
- Button to easily solve another equation without reloading the page.

## Requirements
- Python 3.x
- Flask
- Matplotlib
- Other dependencies listed in `requirements.txt`

## Installation

## Clone the repo
```
git clone https://github.com/your-username/ode-solver-web.git
cd ode-solver-web
```
## Create virtual environment
```
python -m venv venv
venv\Scripts\activate     # for Windows
 ```
or
```
source venv/bin/activate  # for Mac/Linux
```
## Install requirements
```
pip install -r requirements.txt
```
## Run the app
```
python app.py
```
Open http://127.0.0.1:5000 in your browser.

## Folder Structure
```
ode-solver-web/
├── app.py                     # Main Flask app
├── solver.py                  # Contains the Euler method function
├── utils.py                   # Contains plotting utilities
├── templates/
│ ├── form.html                # HTML form for user input
│ └── index.html               # Results page
├── static/
│ └── style.css                # CSS styling
├── exports/
│ ├── results.csv              # CSV file for results
│ └── static/
│ └── output.png               # Generated plot image
├── requirements.txt           # Project dependencies
├── README.md                  # This file
└── .gitignore, .gitattributes # Git config files

```
## Usage
```
Fill out the ODE equation, initial conditions, and step size in the form.
Click Solve to view the results.
A plot and data table will be generated and displayed.
Option to Solve another equation with the button on the results page.
```

## Instructor
```
- Project supervised by:
- Mr. Harish Bhandari
```
🔍 Example Input
```
Equation: dy/dx = x + y
x0 = 0
y0 = 1
h = 0.1
xf = 1
Method: Euler
```
##  Project Members
- Homraj Shahi
- Atul HUmagain
- Abishekh Joshi
- Shreyash Mahato
- Sugam Mahara

