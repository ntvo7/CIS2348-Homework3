#Name: Nguyen Vo
#PISD: 1673509


#initialize dictionary of the team
teamDict = {}

for i in range(1, 6):                       #start at 1 because it wouldn't make sense if the folling statement start at 0 player 
    player = int(input('Enter player {}\'s jersey number:\n'.format(i)))            #A loop run 5 times for 5 players input
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()
    if player < 0 and player > 99 and rating < 0 and rating > 9:                  #create checking condition range for player (1-99) and rating (1-9)
        print('Invalid entry')                                               
        break
    else:
        teamDict[player] = rating
print('ROSTER')
for player, rating in sorted(teamDict.items()):                                 #add and sort player:rating to team dictionary 
    print('Jersey number: %d, Rating: %d' % (player, rating))

menu = ''
while menu != 'q':
    print('\nMENU\n'
        'a - Add player\n'
        'd - Remove player\n'                       #Create menu selection and each letter corresponding to any modification of the team dictionary
        'u - Update player rating\n'
        'r - Output players above a rating\n'
        'o - Output roster\n'
        'q - Quit\n')
    menu = input('Choose an option:\n')

    if menu == 'a':                 #add player 
        player = int(input('Enter a new player\'s jersey number:\n'.format(i)))
        rating = int(input('Enter the player\'s rating:\n'.format(i)))
        teamDict[player] = rating
    elif menu == 'd':              #remove a player from dict
        player = int(input('Enter a jersey number:\n'))
        if player in teamDict.keys():
            del teamDict[player]
    elif menu == 'u':              #update player rating 
        player = int(input('Enter a Jersey number:\n'))
        if player in teamDict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            teamDict[player] = rating
    elif menu == 'r':             #output player have above # rating 
        inputRating = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(inputRating))
        for player, rating in sorted(teamDict.items()):
            if rating > inputRating:
                print('Jersey number: %d, Rating: %d' % (player, rating))
    elif menu == 'o':             
        print('ROSTER')
        for player, rating in sorted(teamDict.items()):
            print('Jersey number: %d, Rating: %d' % (player, rating))




