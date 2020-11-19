rects = []
area = 0
for i in range(3):
    inp = input().split()
    x, y = int(inp[0]), int(inp[1])
    rects.append(sorted([x, y], reverse=True))
    area += x * y

rects_sorted = sorted(rects, key=lambda l: l[0], reverse=True)
if int(area**.5) < area**.5:
    print("NO")

else:
    side_1 = area**.5
    side_2 = area**.5
    for r in rects_sorted[0:2]:
        if r[0] == side_1:
            side_2 -= r[1]
        elif r[0] == side_2:
            side_1 -= r[1]
        elif r[1] == side_1:
            side_2 -= r[0]
        elif r[1] == side_2:
            side_1 -= r[0]
    if rects[2][0] == max(side_1,side_2) and rects[2][1] == min(side_1,side_2):
        print("YES")
    else:
        print("NO")