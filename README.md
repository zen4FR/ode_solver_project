🧮 ODE Solver Web App
A simple Flask web app to solve first-order differential equations using numerical methods.

✅ Features
Choose from methods like:

Euler’s Method

Midpoint Method

Heun’s Method

Runge-Kutta (RK4)

Input your equation, initial values, and step size

Get results and plots in your browser

🏁 How to Run
# Clone the repo
```
git clone https://github.com/your-username/ode-solver-web.git
cd ode-solver-web
```
# Create virtual environment
```
python -m venv venv
venv\Scripts\activate     # for Windows
 ```
or
```
source venv/bin/activate  # for Mac/Linux
```
# Install requirements
```
pip install -r requirements.txt
```
# Run the app
```
python app.py
```
Open http://127.0.0.1:5000 in your browser.

📁 Folder Structure
```
ode-solver-web/
│
├── app.py                  # Main Flask backend
├── requirements.txt        # Libraries to install
├── templates/              # HTML files
│   ├── index.html
│   └── form.html
└── static/                 # CSS or images (optional)
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
