import numpy as np
import math

a = int(input())
b = []
for i in range (0,a):
    value = math.log((float(input())/440.0*32), 2)
    b.append(int(round((value - math.trunc(value))*12)))
print(b)

Major = [0, 2, 4, 5, 7, 9, 11]
Minor = [0, 2, 3, 5, 7, 8, 10]

myDict = {}

Majorkeys = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab']
Minorkeys = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab']
count = 0
for i in Majorkeys:
    myDict.update({i + ' major':np.mod(([x + count for x in Major]), 12)})
    count = count + 1
    
for i in Minorkeys:
    myDict.update({i + ' minor':np.mod(([x + count for x in Minor]), 12)})
    count = count + 1
mykey = 'hi'
canbekey = True
for key, x in myDict.items():
    canbekey = True
    for note in b:
        if not(note in x):
            canbekey = False
    if (canbekey and mykey == 'hi'):
        print("here")
        mykey = key
    if (canbekey and mykey != 'hi'):
        print('cannot determine key')
       # exit()
print("no key")
print(mykey)
print("no key")
sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
for i in b:
    print(sharps[i])
## Dictionary with two keys
#Dictionary = {'A': 'Geeks', 'B': 'For'}
#
## Printing keys of dictionary
#print("Keys before Dictionary Updation:")
#keys = Dictionary1.keys()
#print(keys)
#
## adding an element to the dictionary
#Dictionary1.update({'C':'Geeks'})
#
#print('\nAfter dictionary is updated:')
#print(keys)
#
#print(b)
#
myDict = {}

#
a = 0
a#bb = 1
b = 2
c = 3
c# = 4
d = 5
d# = 6
e = 7
f = 8
f# = 9
g = 10
g# = 11
