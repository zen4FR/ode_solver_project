import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend (important for macOS)

import matplotlib.pyplot as plt
import io
import base64
import csv
import numpy as np
def create_plot(x_vals, y_vals, method, exact_func=None):
    """Create solution plot with optional exact solution"""
    plt.figure(figsize=(10, 6))
    
    # Numerical solution
    plt.plot(x_vals, y_vals, 'b-o', markersize=4, linewidth=1.5, label=f'{method} Solution')
    
    # Exact solution if available
    if exact_func:
        x_exact = np.linspace(min(x_vals), max(x_vals), 100)
        y_exact = [exact_func(x, 0) for x in x_exact]  # 0 is dummy for y
        plt.plot(x_exact, y_exact, 'r-', linewidth=2, label='Exact Solution')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'ODE Solution using {method} Method')
    plt.legend()
    plt.grid(True)
    
    # Save to bytes
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=150, bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

def create_comparison_plot(results, exact_func=None):
    """Create comparison plot of multiple methods"""
    plt.figure(figsize=(10, 6))
    
    # Plot each method
    for method, (x, y) in results.items():
        plt.plot(x, y, '-o', markersize=3, linewidth=1.5, label=method)
    
    # Exact solution if available
    if exact_func:
        x_min = min(min(x) for x, _ in results.values())
        x_max = max(max(x) for x, _ in results.values())
        x_exact = np.linspace(x_min, x_max, 100)
        y_exact = [exact_func(x, 0) for x in x_exact]  # 0 is dummy for y
        plt.plot(x_exact, y_exact, 'k--', linewidth=2, label='Exact Solution')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('ODE Solution Method Comparison')
    plt.legend()
    plt.grid(True)
    
    # Save to bytes
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=150, bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

def save_results_to_csv(x_vals, y_vals):
    """Save results to CSV file"""
>>>>>>> 52c414d ( completed the project)
    with open('exports/results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])
        for xi, yi in zip(x_vals, y_vals):
            writer.writerow([xi, yi])