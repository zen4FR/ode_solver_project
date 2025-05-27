🔧 How to Run
bash
Copy
Edit
# Step 1: Clone the repo
git clone https://github.com/your-username/ode-solver-web.git
cd ode-solver-web

# Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate   # on macOS/Linux

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the app
python app.py
Then open http://127.0.0.1:5000 in your browser.

📂 Folder Structure
csharp
Copy
Edit
ode-solver-web/
│
├── app.py                # Main Flask app
├── requirements.txt      # Python dependencies
├── templates/
│   ├── index.html        # Homepage
│   └── result.html       # Result display (if used)
├── static/
│   └── styles.css        # Optional CSS
└── exports/              # (Optional) Output CSVs/images
📚 What We Learned
Flask basics and backend routing

HTML forms and POST handling

Implementing numerical methods from scratch

Safe use of eval() in Python

Exporting CSV files and dynamic images via web

Working with virtual environments and GitHub collaboration

🧪 Sample Equation
Try solving:

text
Copy
Edit
dy/dx = x + y
x₀ = 0, y₀ = 1
h = 0.1, x_f = 1
Method: Euler
