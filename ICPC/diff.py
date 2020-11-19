import math
def differences(diff,i,s):
    for d in s:
        diff.add(abs(i - d))

a = input().split(" ")
s = set()
dif = set()

start = int(a[0])
s.add(start)
m = int(a[1])
if start == m:
    print(1)
    quit()
loops = 1
lastelem = start
i = 1    
while(True):
    if not (i in s) and not (i in dif):
        s.add(i+lastelem)
        lastelem = i + lastelem
        differences(dif,lastelem,s)
        loops = loops + 1                
        if lastelem == m:
            print(loops)
            quit()
        if m in dif:
            print(loops)
            quit()
    i = i + 1
print('oh no')