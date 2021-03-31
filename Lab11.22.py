#Name: Nguyen Vo
#PISD: 1673509


words = input().split()
for i in words:
    count = 0
    for j in words:
        if j == i:
            count += 1
    print(i, count)