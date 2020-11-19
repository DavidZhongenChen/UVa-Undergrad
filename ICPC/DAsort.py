p = int(input())
out = []
for i in range(p):
    line1 = input().split()
    iter = int(line1[0])
    length = int(line1[1])
    nums = []
    for j in range(int((length + 9)/10)):
        nums = nums + input().split()
    min1 = int(nums[-1])
    min2 = 10**9 + 1
    count = 0
    for i in reversed(range(length - 1)):
        if min1 < int(nums[i]):
            count += 1
            if min2 > int(nums[i]):
                min2 = int(nums[i])
            nums.pop(i)
        else:
            min1 = int(nums[i])
    ind = len(nums) - 1
    while(ind >= 0 and int(nums[ind]) > min2):
        count += 1
        ind -= 1
    out.append(str(iter) + " " + str(count))
for line in out:
    print(line)