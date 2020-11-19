a = int(input())
b = [int(i) for i in (input().split(" "))]
c = b[0]
b = b[1:len(b)]
b.sort(reverse = True)

maxcount = 0
count = 0
while (c+1 not in b):
    maxnum = int(max(b))
    # print(count)
    # print(b)
    maxcount = 0
    for x in b:
        if (maxnum == x):
            maxcount = maxcount + 1
    skipcount = (maxcount)//2
    # print("max " + str(maxnum))
    # print("skip " + str(skipcount))
    for i in range(len(b)):
        if (b[i] == maxnum and skipcount == 0):
            continue
        if (b[i] == maxnum and skipcount > 0):
            skipcount = skipcount - 1
        b[i] = b[i] + 1
    count = count + 1
    # if(len(set(b))==1):
    #     print(count + 2*(c - b[0]))
    #     exit()
print(count-1)

