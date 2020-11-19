import math

bx, by = map(int, input().split(" "))
rect1x, rect1y, rect2x, rect2y = map(int, input().split(" "))

x_increament = bx/math.gcd(by, bx)
y_increament = by/math.gcd(by, bx)

if(not (rect1x <= x_increament and x_increament <= rect2x and rect1y <= y_increament and y_increament <= rect2y) and by > y_increament):
    print("No")
    print(int(x_increament), int(y_increament))
    exit()
if(not (rect1x <= bx  - x_increament and bx - x_increament <= rect2x and rect1y <= by - y_increament and by - y_increament <= rect2y) and bx  - x_increament > 0):
    print("No")
    if(rect2y/rect2x < by/bx):
        #point appears above box
        printy = int(rect2y / y_increament) * y_increament + y_increament
        printx = printy * x_increament / y_increament
        print(int(printx), int(printy))
        exit()
    else:
        printx = int(rect2x / x_increament) * x_increament + x_increament
        printy = printx * y_increament / x_increament
        print(int(printx), int(printy))
        exit()
print("yes")
