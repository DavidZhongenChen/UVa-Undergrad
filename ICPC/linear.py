def f(x):
    return -1
def g(x):
    return 4*x + 8
def h(x):
    return 2*x**2 - 2*x + 9
def i(x):
    return 4*x
def j(x):
    return 2*x**2 - 2*x + 9 - (10+1/3) - (4*x) * (-.5)
def inner(x, y):
    return x(-1)*y(-1) + x(0)*y(0) + x(1)*y(1)

print(inner(f,f))
print("1", inner(f, g)/inner(f, f))

print("2", inner(f, h)/inner(f, f))
print("2", inner(i, h)/inner(i, i))
print("3", inner(j,j))

#-1/sqrt(3)
#4x/sqrt(32)
#(2x^2 - 2x + 9 - (10+1/3) - (4x) * (-.5))/sqrt(2+2/3)
