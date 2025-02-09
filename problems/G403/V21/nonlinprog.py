from sympy import Matrix, symbols

x1, x2 = symbols("x1:3")
f = -6*x1**2 - 4*x2**2 - 1*x1*x2 - 5*x1 - 2*x2
g1 = 6*x1 - 7*x2 + 7
g2 = 3*x1 + 7*x2 - 70
g3 = x1
g4 = x2
x0 = Matrix([0.5, 2])

sol_k = None
sol_lins = None