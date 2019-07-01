#!/usr/local/python3
# This is program to practice the newton method to solve equation
# here we do a simple one-dimention exercise
# f(x) = x^3 - x + 1 = 0

# General solution
# 0. given a start trial root of f(x) = 0, x0
# 1. calculate f(x0) and check whether f(x0) = 0 
# 2. calculate derivative of f(x0), name as f'(x0)
# 3. get the next trial root x1 = x0 - f(x0)/f'(x0)
# 4. calculate f(x1) and chack whether f(x1) = 0
# 5. make x1 as x0 and repeat from 2. to 4. until f(x1) = 0

dx = 1.0e-6

def fun(x):
    fx = x**3 - x + 1
    return fx

def derivative(x):
    der = (fun(x+dx) - fun(x)) / dx
    return der

def push(x):
    xnext = x - fun(x) / derivative(x)
    return xnext

x = 50.0
n = 0
print(("%5s %10s %25s %7s %25s") % \
        ("Loop", "old x", "old function value", "new x", "new function value"))

while True:
    n += 1
    print("%05d    %10.5f        %10.5f    %10.5f    %10.5f" \
            % (n, x, fun(x), push(x), fun(push(x))))
    if (abs(fun(x)) <= dx):
        break
    x = push(x)
#print(n+1, fun(x))
#print(fun(x), derivative(x), next(x) )

