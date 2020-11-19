a = input().split(" ")
num_owners = int(a[0])
size_team = int(a[1])
listofprios = []
listofteams = []
for i in range(num_owners):
    listofprios.append(input().split(" "))
    listofteams.append("")
#    listofprios[i].
rankings = []
index = 0
used = set([])
num_players = int(input())
for i in range(num_players):
    rankings.append(input)
for i in range(size_team):
    for j in range(num_owners):
        if len(listofprios[j]) > 1:
            name = listofprios[j].pop(1)
            if i == 0:
                listofteams[j] = name
            else:
                listofteams[j] = listofteams[j] + " " + name
        else:
            print(index)
            temp = str(rankings[index])
            index += 1
            while(temp in used):
                print(index)
                temp = str(rankings[index])
                index += 1
            name = temp
            if i == 0:
                listofteams[j] = str(name)
            else:
                listofteams[j] = listofteams[j] + " " + str(name)
        for k in range(num_owners):
            if name in listofprios[k]:
                listofprios[k].remove(name)
        used.add(str(name))
        print(used)

for i in range(num_owners):
    print(listofteams[i])

