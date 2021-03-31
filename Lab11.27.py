#Name: Nguyen Vo
#PISD: 1673509


teamDict = {}

for i in range(1, 6):
    player = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()
    if player < 0 and player > 99 and rating < 0 and rating > 9:
        print('Invalid entry')
        break
    else:
        teamDict[player] = rating
print('ROSTER')
for player, rating in sorted(teamDict.items()):
    print('Jersey number: %d, Rating: %d' % (player, rating))

menu = ''
while menu != 'q':
    print('\nMENU\n'
        'a - Add player\n'
        'd - Remove player\n'
        'u - Update player rating\n'
        'r - Output players above a rating\n'
        'o - Output roster\n'
        'q - Quit\n')
    menu = input('Choose an option:\n')

    if menu == 'a':
        player = int(input('Enter a new player\'s jersey number:\n'.format(i)))
        rating = int(input('Enter the player\'s rating:\n'.format(i)))
        teamDict[player] = rating
    elif menu == 'd':
        player = int(input('Enter a jersey number:\n'))
        if player in teamDict.keys():
            del teamDict[player]
    elif menu == 'u':
        player = int(input('Enter a Jersey number:\n'))
        if player in teamDict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            teamDict[player] = rating
    elif menu == 'r':
        inputRating = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(inputRating))
        for player, rating in sorted(teamDict.items()):
            if rating > inputRating:
                print('Jersey number: %d, Rating: %d' % (player, rating))
    elif menu == 'o':
        print('ROSTER')
        for player, rating in sorted(teamDict.items()):
            print('Jersey number: %d, Rating: %d' % (player, rating))




