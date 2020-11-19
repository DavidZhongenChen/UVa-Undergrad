n = int(input())
mylist = {}
for i in range(n):
    inpt = input()
    initials = (inpt[inpt.index(" ")+1] + inpt[0])
    mylist.update( {inpt : initials} )
    print(initials)
print(mylist)
list = list(mylist.keys())
print(list)
print(list.sort())
print(list)
print(list(mylist.values()).sort())

