def euler_method(f, x0, y0, h, xf):
    """Euler's method for solving ODEs"""
    x_vals = [x0]
    y_vals = [y0]
    while x_vals[-1] < xf:
        x = x_vals[-1]
        y = y_vals[-1]
        step = min(h, xf - x)  # Adjust last step
        y_next = y + step * f(x, y)
        x_vals.append(round(x + step, 10))
        y_vals.append(y_next)
    return x_vals, y_vals

def midpoint_method(f, x0, y0, h, xf):
    """Midpoint method (RK2) for solving ODEs"""
    x_vals = [x0]
    y_vals = [y0]
    while x_vals[-1] < xf:
        x = x_vals[-1]
        y = y_vals[-1]
        step = min(h, xf - x)
        k1 = f(x, y)
        k2 = f(x + step/2, y + (step/2)*k1)
        y_next = y + step * k2
        x_vals.append(round(x + step, 10))
        y_vals.append(y_next)
    return x_vals, y_vals

def heun_method(f, x0, y0, h, xf):
    """Heun's method for solving ODEs"""
    x_vals = [x0]
    y_vals = [y0]
    while x_vals[-1] < xf:
        x = x_vals[-1]
        y = y_vals[-1]
        step = min(h, xf - x)
        k1 = f(x, y)
        k2 = f(x + step, y + step*k1)
        y_next = y + (step/2) * (k1 + k2)
        x_vals.append(round(x + step, 10))
        y_vals.append(y_next)
    return x_vals, y_vals

def rk4_method(f, x0, y0, h, xf):
    """Classic RK4 method for solving ODEs"""
    x_vals = [x0]
    y_vals = [y0]
    while x_vals[-1] < xf:
        x = x_vals[-1]
        y = y_vals[-1]
        step = min(h, xf - x)
        k1 = f(x, y)
        k2 = f(x + step/2, y + step*k1/2)
        k3 = f(x + step/2, y + step*k2/2)
        k4 = f(x + step, y + step*k3)
        y_next = y + (step/6) * (k1 + 2*k2 + 2*k3 + k4)
        x_vals.append(round(x + step, 10))
        y_vals.append(y_next)
    return x_vals, y_vals

def rk4_adaptive(f, x0, y0, h, xf, tol=1e-6, h_min=1e-5, h_max=None):
    """
    RK4 adaptive step size method.
    
    Args:
        f: function f(x,y)
        x0, y0: initial conditions
        h: initial step size
        xf: final x value
        tol: tolerance for error
        h_min: minimum allowed step size
        h_max: maximum allowed step size (optional)
    Returns:
        (x_vals, y_vals): lists of x and y points
    """
    x_vals = [x0]
    y_vals = [y0]
    h_actual = h
    if h_max is None:
        h_max = h * 10
    
    while x_vals[-1] < xf:
        x = x_vals[-1]
        y = y_vals[-1]
        if x + h_actual > xf:
            h_actual = xf - x  # last step adjust
        
        # One full step of size h_actual
        k1 = f(x, y)
        k2 = f(x + h_actual/2, y + h_actual*k1/2)
        k3 = f(x + h_actual/2, y + h_actual*k2/2)
        k4 = f(x + h_actual, y + h_actual*k3)
        y_full = y + (h_actual/6)*(k1 + 2*k2 + 2*k3 + k4)
        
        # Two half steps of size h_actual/2
        h_half = h_actual / 2
        
        k1 = f(x, y)
        k2 = f(x + h_half/2, y + h_half*k1/2)
        k3 = f(x + h_half/2, y + h_half*k2/2)
        k4 = f(x + h_half, y + h_half*k3)
        y_half_step = y + (h_half/6)*(k1 + 2*k2 + 2*k3 + k4)
        
        x_mid = x + h_half
        
        k1 = f(x_mid, y_half_step)
        k2 = f(x_mid + h_half/2, y_half_step + h_half*k1/2)
        k3 = f(x_mid + h_half/2, y_half_step + h_half*k2/2)
        k4 = f(x_mid + h_half, y_half_step + h_half*k3)
        y_two_half = y_half_step + (h_half/6)*(k1 + 2*k2 + 2*k3 + k4)
        
        # Error estimate
        error = abs(y_two_half - y_full)
        
        if error < tol:
            # Accept the step
            x_vals.append(x + h_actual)
            y_vals.append(y_two_half)
            
            # Increase step size cautiously
            h_actual = min(h_max, h_actual * min(2, 0.9 * (tol / error)**0.25))
        else:
            # Reject step, reduce h_actual
            h_actual = max(h_min, h_actual * max(0.1, 0.9 * (tol / error)**0.25))
            # Do not advance x or y (retry with smaller step)
        
        # Safety check to avoid infinite loop if step size is too small
        if h_actual < h_min:
            raise RuntimeError("Step size became too small.")
    
    return x_vals, y_vals
