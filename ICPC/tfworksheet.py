import numpy as np
inp = input().split()
n,m = int(inp[0]), int(inp[1])
sames = []
diffs = []
dic = []
dic2 = []
for i in range(n):
    dic.append(0)
    dic2.append(0)
for i in range(n):
    line = input.split()
    start, end = int(line[0]), int(line[1])
    if start == end:
        continue
    if line[2][0] == 's':
        sames.append([start, end])
        cur = i
        if dic[start] != 0:
            cur = dic[start]
        end_val = [dic[end]]
        if end_val != 0:
            end_ind = end
            while(end_ind < n and dic[end_ind] == end_val)
                dic[end_ind] = cur
                end_ind += 1
        for j in range(start,end):
            dic[j] = cur
    else:
        diffs.append([start, end])
        for j in range(start + 1, end)
        dic2


#same: / range
# different / 2