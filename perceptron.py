import numpy as np
from math import sin, cos, pi, sqrt

def dot(ta, tb):
    return ta[0]*tb[0] + ta[1]*tb[1]

def misclassified(b0, b1, x, y):
    for i in range(len(x)):
        d = y[i]*(dot(x[i],b1) + b0)
        if (d <= 0):
            return i
    return -1

def adjust_b(b0, b1, x, y, idx):
    b0_new = b0 + rho * y[idx]
    b1_new = (b1[0] + rho * y[idx] * x[idx][0], b1[1] + rho * y[idx] * x[idx][1])
    return b0_new, b1_new

def yd(b0,  b1, x, y):
    ds = []
    for i in range(len(x)):
        ds.append(y[i]*(dot(x[i],b1) + b0)/sqrt(b1[0]*b1[0]+b1[1]*b1[1]))
    print("y.d = ", ds)

rho = 0.5
b0 = -0.5
b1 = (0, 1)
y = np.array([1,1,1,-1,-1])
x = np.array([(cos((4*x -3)*pi/10), sin((4*x-3)*pi/10)) for x in range(1,6)])

print ("x = ", x)
print ("y = ", y)

iter = 0
while misclassified(b0, b1, x, y) != -1:
    iter = iter + 1
    print ("iteration = ", iter)
    idx = misclassified(b0,b1,x,y)
    yd(b0,b1,x,y)
    print ("First misclassified point at index: ", idx)
    newb0, newb1 = adjust_b(b0,b1,x,y, idx)
    b0 = newb0
    b1 = newb1
    print ("New plane: ", b0, b1)
yd(b0,b1,x,y)
print ("No misclassified points left. Terminating")

