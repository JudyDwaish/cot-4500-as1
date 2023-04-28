# Goudi Dwaish
# COT4500-23Spring 0001
# JAN 25, 2023
# Assignment 1
# Professor Juna Parra

import numpy as np

# Question 1
num = int('010000000111111010111001', 2)
print(round(np.float64(num), 5))

# Question 2
num = round(num / 1000) * 1000
print(round(np.float64(num), 5))

# Question 3
num = round(num / 1000 + 0.5) * 1000
print(round(np.float64(num), 5))

# Question 4
exact_val = np.float64(int('010000000111111010111001', 2))
rounded_val = round(exact_val / 1000 + 0.5) * 1000
abs_error = np.abs(exact_val - rounded_val)
rel_error = abs_error / exact_val
print(round(abs_error, 5))
print(round(rel_error, 5))

# Question 5
def f(x):
    return np.log(x)

n = 1
error = np.inf
while error > 1e-4:
    n += 1
    series_sum = np.sum([((-1)**(i+1))/i for i in range(1, n+1)])
    error = np.abs(f(1) - series_sum)
print(n)

# Question 6
def f(x):
    return x**3 + 4*x**2 - 10

# 6(a) Using the bisection method
a = -4
b = 7
error = np.inf
n = 0
while error > 1e-4:
    n += 1
    c = (a + b) / 2
    if f(c) == 0 or (b-a)/2 < 1e-4:
        break
    if np.sign(f(c)) == np.sign(f(a)):
        a = c
    else:
        b = c
    error = np.abs(f(c))
print(n)

# 6(b) Using the newton Raphson method
x = -4
n = 0
while True:
    n += 1
    x_new = x - f(x)/ (3*x**2 + 8*x)
    if np.abs(x_new - x) < 1e-4:
        break
    x = x_new
print(n)
