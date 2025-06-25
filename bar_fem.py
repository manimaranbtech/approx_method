from sympy import symbols, Eq, solve, simplify, expand, diff, integrate
import numpy as np
# Define symbols (like variables)
X1, a0, a1, x1, x2, u = symbols('X1 ao a1 x1 x2 u')
# Input parametres
EA=1
L=1
p=1*X1
nElements=4
# preliminary calculations
nNodes=nElements+1
# mesh_creation
l = np.linspace(0, L, nNodes)
# Global stifness matrix
Kg = np.zeros((nNodes, nNodes)) 
# Nodal force vector
nodalfg = np.zeros((nNodes, 1), dtype=object)
# Displacement equation
disp = Eq(u, a0 + a1*X1)

# solve for nodal displacement
eq1 = Eq(disp.rhs.subs(X1, l[0]), x1)  # When X1=0, u=x1
eq2 = Eq(disp.rhs.subs(X1, l[1]), x2)  # When X1=0.25, u=x2

# Solve the system of equations
solution = solve((eq1, eq2), (a0, a1))

# Substitute the solved a0 and a1 into the displacement equation
disp_solved = disp.subs({a0: solution[a0], a1: solution[a1]})

# Expand the equation to separate x1 and x2 terms
disp_expanded = expand(disp_solved.rhs)

# Extract coefficients of x1 and x2
N1 = disp_expanded.coeff(x1)  # Coefficient of x1
N2 = disp_expanded.coeff(x2)  # Coefficient of x2
Ni = np.array([N1, N2])

# Compute derivatives w.r.t X
dNi = np.array([diff(Ni[0], X1), diff(Ni[1], X1)])

# element stifness matrix
# Initialize a NumPy array to store results
Ke1 = np.zeros((len(dNi), len(dNi)), dtype=object)
for i in range(len(dNi)):
    for j in range(len(dNi)):
        Ke1[i, j] = integrate(EA * dNi[i] * dNi[j], (X1, l[0], l[1]))

# Nodal force vector
# Initialize a NumPy array to store results
nodalf1 = np.zeros(len(Ni), dtype=object) 
for j in range(len(Ni)):
    nodalf1[j]=integrate(p*Ni[j],(X1,l[0], l[1]))
    
# Convert to column matrix
nodalf1 = nodalf1.reshape(-1, 1)  # -1 means "infer size"

# Global matrix creation
# Indices where the small matrix will be placed (top-left corner at row=1, col=2)
start_row, start_col = 0, 0

# Replace values using slicing
Kg[start_row:start_row+2, start_col:start_col+2] = Ke1

# Global matrix creation
# Indices where the small matrix will be placed (top-left corner at row=1, col=2)
start_row, start_col = 0, 0

# Replace values using slicing
nodalfg[start_row:start_row+2, start_col:start_col+1] = nodalf1

print(nodalfg)

print(Kg)
