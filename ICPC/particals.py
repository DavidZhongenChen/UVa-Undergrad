from sympy import symbols, solve, Eq

x1,y1 = input().split(" ")
x2,y2 = input().split(" ")
x3,y3 = input().split(" ")
xdir,ydir,r = input().split(" ")
x1,y1 = int(x1),int(x2)
x2,y2 = int(x2),int(y2)
x3,y3 = int(x3),int(y3)
xdir,ydir,r = int(xdir),int(ydir),int(r)

x, y = symbols('x y')

m = (ydir/xdir)

#expr1a = Eq((x-x2)**2 + (y-y2)**2 - (2*r)**2)
#expr1b = Eq(- m*(x - x1)+(y - y1))
expr2a = Eq((x-x3)**2 + (y-y3)**2 - (2*r)**2)
expr2b = Eq(m*(x - x1) - (y - y1))

#sol1 = solve((expr1a, expr1b), (x,y))
sol2 = solve((expr2a, expr2b), (x,y))

#print(sol1)
print(sol2)
