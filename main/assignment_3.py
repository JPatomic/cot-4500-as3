# Assignment 3
# JP O'Toole

import numpy as np

# Defines the function for both questions
def f(t, y):
    return t - y**2

# Question 1
def euler_method(f, t0, y0, t_end, n):

    # Defines step size
    h = (t_end - t0) / n

    # Creates matrices
    t_values = np.linspace(t0, t_end, n+1)
    y_values = np.zeros(n+1)

    # Creates starting y value in the matrix
    y_values[0] = y0

    # Computes the y values
    for i in range(n):
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    # Prints final Result
    print(y_values[n])

# Question 2
def runge_kutta_method(f, t0, y0, t_end, n):

    # Defines step size
    h = (t_end - t0) / n

    # Creates matrices
    t_values = np.linspace(t0, t_end, n+1)
    y_values = np.zeros(n+1)

    # Creates starting y value in the matrix
    y_values[0] = y0

    # Computes the y values
    for i in range(n):
        t, y = t_values[i], y_values[i]
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y_values[i+1] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    # Prints final Result
    print(y_values[n])

# Parameters
t0, y0, t_end, n = 0, 1, 2, 10

# Compute solutions
euler_method(f, t0, y0, t_end, n)
runge_kutta_method(f, t0, y0, t_end, n)
