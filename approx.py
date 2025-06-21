from sympy import symbols, Eq, solve, simplify

# Define symbols
a0, a1, x, x1, x2, u1, u2, L = symbols('a0 a1 x x1 x2 u1 u2 L')

# Define equations
eq1 = Eq(u1, a0 + a1*x1)
eq2 = Eq(u2, a0 + a1*x2)

# Solve for a0 and a1
solution = solve((eq1, eq2), (a0, a1))

# Substitute L = x2 - x1 into the solutions
a0_sol = solution[a0].subs(x2 - x1, L)
a1_sol = solution[a1].subs(x2 - x1, L)

# General expression for u(x)
u_x = a0_sol + a1_sol * x

# Factor out u1 and u2
#numerator = u_x * L  # Multiply by L to work with numerator
expanded_num = u_x.expand()  # Expand the numerator
factored_u_x = expanded_num.collect([u1, u2])  # Group terms with u1 and u2

# Display the result
print("Factored u(x):", factored_u_x)
print(simplify(factored_u_x))
