from sympy import symbols, Eq, solve

# Define symbols
a0, a1, x1, x2, u1, u2, L = symbols('a0 a1 x1 x2 u1 u2 L')

# Define equations
eq1 = Eq(u1, a0 + a1*x1)
eq2 = Eq(u2, a0 + a1*x2)

# Solve for a0 and a1
solution = solve((eq1, eq2), (a0, a1))

# Substitute L = x2 - x1 into the solutions
a0_sol = solution[a0].subs(x2 - x1, L)
a1_sol = solution[a1].subs(x2 - x1, L)

# Display the solutions
print("a0 =", a0_sol)
print("a1 =", a1_sol)
