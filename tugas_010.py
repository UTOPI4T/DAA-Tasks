# pip install pulp
# Linear Programming

import pulp
model = pulp.LpProblem("Profit", pulp.LpMaximize)

A = pulp.LpVariable('A',lowBound=0, cat='Integer')
B = pulp.LpVariable('B',lowBound=0, cat='Integer')

model += 4200 * A + 2800 * B,"Pr32ofit"

model += 3 * A + 2 * B <= 20
model += 4 * A + 3 * B <= 30
model += 4 * A + 3 * B <= 44

model.solve()
pulp.LpStatus[model.status]

print(A.varValue)
print(B.varValue)

print(pulp.value(model.objective))

# Latihan No 1
import pulp

model = LpProblem(name="persamaan", sense=LpMinimize)

x = LpVariable(name="x")
y = LpVariable(name="y")

model += 4 * x + 3 * y == 34

model.solve()

print("x = ",x.varValue)
print("y = ",y.varValue)

# Latihan No 2
import pulp

model = LpProblem(name="persamaan", sense=LpMinimize)

x = LpVariable(name="x")
y = LpVariable(name="y")

model += 5 * x + 1 * y == 37

model.solve()

print("x = ",x.varValue)
print("y = ",y.varValue)

# Latihan Cerita No1 (cara 1)

import pulp
model = pulp.LpProblem("Profit", pulp.LpMaximize)

P = pulp.LpVariable('P',lowBound=0, cat='Integer')
B = pulp.LpVariable('B',lowBound=0, cat='Integer')

model += 2 * P + 6 * B,"Pr32ofit"

model += 3 * P + 4 * B == 11000
model += 1 * P + 7 * B == 15000


model.solve()
pulp.LpStatus[model.status]

print("1 P =",P.varValue)
print("1 B =",B.varValue)

print("\nTotal 2P dan 6B = ",pulp.value(model.objective))

# Latihan Cerita No1 (cara 2)

import pulp

model = LpProblem(name="persamaan", sense=LpMinimize)

P = LpVariable(name="P")
B = LpVariable(name="B")

model += 3 * P + 4 * B == 11000
model += 1 * P + 7 * B == 15000

model.solve()

print("1 P = ",P.varValue)
print("1 B = ",B.varValue)

# Latihan Cerita No2 (cara 2)

import pulp

model = LpProblem(name="persamaan", sense=LpMinimize)

P = LpVariable(name="P")
L = LpVariable(name="L")

model += (2 * P) + (2 * L) == 44
model += L == P - 6

model.solve()

print("P = ",P.varValue)
print("L = ",L.varValue)

# Import Scipy dan linprog

import numpy as np
from scipy.optimize import linprog

A = np.array([[1,0],[2,3],[1,1],[-1,0],[0,-1]])
b = np.array([16,19,8,0,0])
c = np.array([-5,-7])

x1_bounds = (0,None)
x2_bounds = (0,None)

res = linprog(c,A_ub=A, b_ub=b)


print('Optimal Value: ', round(res.fun*-1, ndigits=2),
      '\nx values: ',res.x,
      '\nNumber pf Iteration Performed:', res.nit,
      '\nStatus:',res.message)

print("Optimal Solution:")
print("x1 =",res.x[0])
print("x2 =",res.x[1])
print("Max z =",-res.fun)
