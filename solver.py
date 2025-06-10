def euler_method(f, x0, y0, h, xf):
    x_values = [x0]
    y_values = [y0]
    
    while x0 < xf:
        y0 += h * f(x0, y0)
        x0 += h
        x_values.append(x0)
        y_values.append(y0)
    
    return x_values, y_values
