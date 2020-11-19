import numpy as np
from sys import stdin, stdout
import gmpy2

prime = 2
n = stdin.readline()
n = int(n)
lines = stdin.readlines()

m = np.zeros((n, 1))
i = 0
for line in lines:
    m[i] = int(line)
    i = i + 1

count = np.zeros((n, 1))
ret = np.ones((n, 1))
index = 0
# print(m.all() != 1)
# print(index < primes.shape[0])
# print(m.all())

while(not np.array_equal(m, np.ones((n,1)))):
    
    power = np.zeros((n, 1)) #keep track of the powers of primes
    mods = np.mod(m, prime) #0 if factor
    mods = np.logical_not(mods) #1 if factor
    count = count + mods  #adds 1s to count
    while(not np.array_equal(mods, np.zeros((n,1)))):
        power = power + mods #increments power by 1 everytime
        mods = mods * prime + np.logical_not(mods)
        m = m / mods
        mods = np.mod(m, prime)
        mods = np.logical_not(mods)
    ret = ret * (power + 1)
    prime = gmpy2.next_prime(prime)

ret = ret - count

for i in range(0,n):
    if i == 1:
        if(int(lines[i]) in primes):
            print(1)
        else:
            print(2)
    else:
        print(int((ret[i])[0]))

