import matplotlib.pyplot as plt
import io
import base64
import csv

def create_plot(x_vals, y_vals, method):
    plt.figure()
    plt.plot(x_vals, y_vals, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Solution using {method} Method')
    plt.grid(True)

    # Save plot as PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    # Save in exports/static/output.png too
    with open('static/output.png', 'wb') as f:
        f.write(img.getvalue())

    # Save the numerical results to exports/results.csv
    with open('exports/results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])
        for xi, yi in zip(x_vals, y_vals):
            writer.writerow([xi, yi])

    return plot_url
