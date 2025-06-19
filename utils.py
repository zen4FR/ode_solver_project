import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend (important for macOS)

import matplotlib.pyplot as plt
import io
import base64
import csv

def create_plot(x_vals, y_vals, method):
    # Set up a headless plot
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, marker='o')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Solution using {method} Method')
    ax.grid(True)

    # Save plot to memory (for base64 string)
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)

    # Save the plot as a static file (optional)
    with open('static/output.png', 'wb') as f:
        f.write(img.getvalue())

    # Save results to CSV
    with open('exports/results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])
        for xi, yi in zip(x_vals, y_vals):
            writer.writerow([xi, yi])

    return plot_url
