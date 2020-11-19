def prettyprint(votes):
    for line in votes:
        print(line)
def addchildren(canbeat,man):
    for kid in range(len(canbeat)):
        
    return canbeat[man]
def canwin(winnable,man,canbeat,ballots):
    for i in canbeat[man]:
        if winnable[i] == True:
            winnable[man] = True
            return
    
    for i in canbeat[man]:
        
    for i in range(ballots):
        if not (i in canbeat):
            cannotbeat.append(i)
    
    
a = input().split()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(a[0])
ballots = int(a[1])
votes = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    votes.append(temp)
    
for i in range(ballots):
    line = input().split()
    v = int(line[0])
    s = line[1]
    index = 0
    #for each line of input do this:
    for left in range(n):
        leftman = s[left]
        leftmanindex = letters.index(leftman + "")
        for right in range(left,n):
            rightman = s[right]
            rightmanindex = letters.index(rightman + "")
            print(leftman,rightman,v)
            votes[leftmanindex][rightmanindex] = votes[leftmanindex][rightmanindex] + v
print('votes')
prettyprint(votes)
canbeat = []
total = votes[0][0]
for i in range(ballots):
    temp = []
    for j in range(ballots):
        if votes[i][j] > total/2 or votes[i][j] == total/2:
            if not (i is j):
                temp.append(j)
    canbeat.append(temp)
            
print('can beat:' )
prettyprint(canbeat)
winnable = []
for i in range(ballots):
    winnable.append([None])
for i in range(ballots):
    canwin(winnable,i,canbeat,ballots)

print(winnable)