#Name: Nguyen Vo
#PISD: 1673509


numbers = input().split()
listNumber = []

for i in numbers:                       #convert from string to int so that any number greater than 0 will add to the list listNumber
    i = int(i)                    
    if i >= 0:
        listNumber.append(i)

listNumber.sort()                           #sort from least to greatest before print out 
for i in listNumber:
    print(i, end =' ')
