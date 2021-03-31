#Name: Nguyen Vo
#PISD: 1673509


numbers = input().split()
listNumber = []

for i in numbers:
    i = int(i)
    if i >= 0:
        listNumber.append(i)

listNumber.sort()
for i in listNumber:
    print(i, end =' ')
