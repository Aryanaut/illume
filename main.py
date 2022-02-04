from game_levels.titles import il_levels

il_levels = il_levels()
il_levels.show_title()
import time
import random

# global variables 
playerInv = {'items':[], 'keys':0}
print("You wake up in a forest with four paths in four directions - North, South, East, and Down. \nIn front of you is a gate with a scroll attached to its side. \n \n What do you do now?")
print("\n Commands: \n open inventory \n use [itemname] \n go [direction] \n Once you enter a level, to return to the forest, type go [the direction cardinally opposite]. \n Type in 'look around' to search the area \n Type in 'END GAME' to end the game. \n")

playerInput = ""
gateReq = 3
currentLevel = 'forest'

enteredForest = True
enteredEast = False
enteredSouth = False
enteredDown = False
enteredNorth = False

'''
Format for items:
items = {level_name:{itemname:[list of commands for the item]}}
'''
items = {'forest':{'scroll': ['use', 'drop', 'pickup'], 'gate': ['open'], 'scissors':['pickup']}, 
        'east':{'trickster':['talk', 'play']}}

commands  = {'forest':['look', 'go', 'pickup', 'drop', 'use', 'open'],
            'east':['look', 'go', 'pickup', 'drop', 'give'],
            'down':['go', 'look'],
            'south':['look', 'go', 'talk', 'help']}

paths = {'forest':['north', 'south', 'east', 'down'], 'east':['west'], 'down':['up'], 'south':['north'], 'north':['south']}

errorMsg = {'directionError':'You cannot go that way in this room', 
            'unrecognizedCommand':'The game does not recognize this command.',
            'actionNotForItem':'This action cannot be performed on this item.',
            'commandLVLunavailable':'This action cannot be performed in this level.'}

debugging_commands = {'debugadd':'debugadd [itemname]', 'debugremove':'debugremove [itemname]'}
currentLevel = 'forest'

def msgs(item, msgType):
    switcher = {
        'dropitem':'You have dropped the '+item,
        'pickupItem':'You have picked up the '+item,
        'iteminInv':'You already have this item',
        'itemOutInv':'You do not have this item',
        'usedItem':'You used the '+item
    }
    print(switcher.get(msgType))

rps = ['rock', 'paper', 'scissors']
rpsWin = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
finalItemList=['rock', 'paper', 'scissors', 'g_key']

game_ended = False
while game_ended == False:

    playerInput = input(">>> ").lower()

    if playerInput != "end game":
        
        if len(playerInput.split()) > 1:
            prefix = playerInput.split()[0]
            suffix = playerInput.split()[1]
        else:
            prefix = playerInput.split()[0]
            
        if playerInput == 'open inventory':
            print("\n Your Inventory: \n")
            for itemType in playerInv:
                print(itemType.title()+': ', playerInv[itemType])
            print()
            continue

# debugging code
        if prefix == "debug":
            print("\n Commands available: \n")
            for command in debugging_commands:
                print(command, "Usage:", debugging_commands[command])
            print()
            continue

        if prefix == 'debugadd':
            if suffix == 'key':
                playerInv['keys'] += 1
            else:
                playerInv['items'].append(suffix)
            
            print('{} has been added to inventory'.format(suffix))
            continue

        if prefix == 'debugremove':
            if suffix == 'key':
                playerInv['keys'] -= 1
            else:
                playerInv['items'].remove(suffix)
            
            print('{} has been removed from inventory'.format(suffix))
            continue
            

# forest code
        if currentLevel == 'forest':
            
            level_items = items['forest']
            
            if prefix in commands['forest'] or prefix in debugging_commands.keys():
                if prefix == 'go':
                    if suffix in paths['forest']:
                        if suffix == 'north':
                            print("The Path is blocked by a gate. (Hint: Collect the 3 keys to open the gate by finishing the levels, and if you've collected the keys, type open gate!)")
                        if suffix == 'south':
                            print('Welcome to the south! Try using commands like \'look around\' or \'talk\'')
                            currentLevel = 'south'
                            continue

                        if suffix == 'west':
                            currentLevel = 'west'
                            continue

                        if suffix == 'down':
                            print('Welcome to the Underground! Try using commands like \'talk\'')
                            currentLevel = 'down'
                            continue

                        if suffix == 'east':
                            print('Welcome to the east! Try using commands like \'look around\' or \'talk\'')
                            currentLevel = 'east'
                            enteredEast = True
                            continue
                    
                    else:
                        print(errorMsg['directionError'])

                    continue

                if prefix == 'use':
                    if suffix in level_items.keys():
                        if suffix in playerInv['items']:
                            msgs(suffix, 'usedItem')
                            if prefix in level_items[suffix]:
                                if suffix == 'scroll':
                                    print("The scroll reads: \n Find the three keys to open the gate \n and make your way home.\n")
                            else:
                                print("This command is not available for this item")
                        else:
                            msgs(suffix, 'itemOutInv')

                if prefix == 'pickup':
                    if 'pickup' in level_items[suffix]:
                        itemInInv = suffix in playerInv['items']
                        if itemInInv == True:
                            msgs(suffix, 'iteminInv')
                        else:
                            msgs(suffix, 'pickupItem')
                            playerInv['items'].append(suffix)
                    else:
                        print(errorMsg['actionNotForItem'])
                
                if prefix == 'drop':
                    if 'drop' in level_items[suffix]:
                        itemInInv = suffix in playerInv['items']
                        if itemInInv == True:
                            msgs(suffix, 'dropitem')
                            playerInv['items'].remove(suffix)
                        else:
                            msgs(suffix, 'itemOutInv')
                    else:
                        print(errorMsg['actionNotForItem'])
                        
                if playerInput == 'look around':
                    print("\n You see: ")
                    for item in level_items.keys():
                        print(item.title(), end=': ')
                        print(items['forest'][item])
                    print("\nYou also see paths: \n")
                    for item in paths['forest']:
                        print(item.title())
                    print("Use the go (usage: go [direction]) command to travel these paths.\n")
                
                if prefix == 'open':
                    if suffix == 'gate':
                        if playerInv['keys'] != gateReq:
                            print("The gate requires", gateReq, "keys to open.")
                        else:
                            print("The gate opens, and you walk through. You've made it home. Congratulations, player.")
                            il_levels.end_screen()
                            break
                    else:
                        print(errorMsg['unrecognizedCommand'])
            else:
                print(errorMsg['commandLVLunavailable'])
    
# east code
        if currentLevel == 'east':

            level_items = items['east']
            rpsWon = False

            if prefix == 'go':
                if suffix in paths['east']:
                    if suffix == 'west':
                        print('Welcome back to the forest!')
                        currentLevel = 'forest'
                        enteredForest = True
                else:
                    print(errorMsg['directionError'])
            
            if playerInput == 'talk':
                print("\n Area: Trickster's lair \n")
                print("What do you do now? [type in 'help' to see options] \n")
                print("\n To? \n - The old hooded man [type in 'trickster'] \n Type in 'Exit' to cancel action.\n" )
                playerInput = input(">>> ").lower()

                if playerInput == 'trickster':

                    if rpsWon == False:

                        print("\n Trickster: Greetings wanderer!")
                        print("\n Choose your response: \n [1] Say hello \n [2] Look around\n")
                        playerInput = input(">>> ").lower()

                        if playerInput == '1':
                            print("\n Trickster: I'd offer you to play a game with me, but I'm looking for a pair of scissors I lost in the forest. Seen it anywhere?")
                            playerInput = input("Yes or no? \n>>> ").lower()

                            if playerInput == 'yes':
                                if 'scissors' in playerInv['items']:
                                    playerInv['items'].remove('scissors')
                                    playerInput = input("\n Trickster: Thank you, wanderer. Would you like to play? Winner takes the key. (Yes or no?)\n>>> ").lower()
                                    
                                    if playerInput == 'yes':
                                        playerWins = 0
                                        triWins = 0
                                        print("\n Trickster: Game's simple. Rock beats Scissors, Scissors cuts Paper, Paper covers rock. First to five points wins. Winner takes key. \n")
                                        
                                        while playerWins != 5:
                                            playerChoice = input("Enter your choice (Rock, Paper or Scissors): ").lower()
                                            triChoice = random.choice(rps)
                                            
                                            if playerChoice == triChoice:
                                                print("\nDraw! \n")

                                            elif playerChoice == 'rock':
                                                if triChoice == 'paper':
                                                    print("\nPaper covers rock, player loses!\n")
                                                    triWins += 1
                                                    print("Player score:", playerWins)
                                                    print("Trickster's score: ", triWins)
                                                    print()
                                                if triChoice == 'scissors':
                                                    print("\nRock crushes scissors, trickster loses!")
                                                    playerWins += 1
                                                    print("Player score:", playerWins)
                                                    print("Trickster's score: ", triWins)
                                                    print()

                                            elif playerChoice == 'scissors':
                                                if triChoice == 'rock':
                                                    print("\nRock crushes scissors, player loses!\n")
                                                    triWins += 1
                                                    print("Player score:", playerWins)
                                                    print("Trickster's score: ", triWins)
                                                    print()
                                                if triChoice == 'paper':
                                                    print("\nScissors cuts paper, trickster loses!")
                                                    playerWins += 1
                                                    print("Player score:", playerWins)
                                                    print("Trickster's score: ", triWins)
                                                    print()

                                            elif playerChoice == 'paper':
                                                if triChoice == 'scissors':
                                                    print("\nScissors cuts paper, player loses!\n")
                                                    triWins += 1
                                                    print("Player score:", playerWins)
                                                    print("Trickster's score: ", triWins)
                                                    print()
                                                if triChoice == 'rock':
                                                    print("\nPaper covers rock, trickster loses!")
                                                    playerWins += 1
                                                    print("Player score:", playerWins)
                                                    print("Trickster's score: ", triWins)
                                                    print()

                                            play_again = input("Play again? (y/n): ").lower()

                                            if playerWins == 5:
                                                print("\nPlayer wins!\n")
                                                playerInv['items'].extend(['scissors', 'paper', 'rock'])
                                                msgs('scissors', 'pickupItem')
                                                msgs('paper', 'pickupItem')
                                                msgs('rock', 'pickupItem')
                                                playerInv['keys'] += 1
                                                print("\nTrickster: Fair enough. Have the key.\n")
                                                print("A key has been added to your inventory!\n")
                                                rpsWon = True
                                                paths['forest'].pop(paths['forest'].index('east'))
                                                break
                                            
                                            if triWins == 5:
                                                print("\nTrickster: Better luck next time, traveller.\n")
                                                break
                                            
                                            if play_again == 'n':
                                                break

                                        continue
                                    
                                    if playerInput == 'no':
                                        print("\n Trickster: Later, then.\n")
                                        continue

                                    else:
                                        print(errorMsg['unrecognizedCommand'])
                                        continue
                                else:
                                    print(msgs('scissors', 'itemOutInv'))
                                    continue

                            if playerInput == 'no':
                                print("\n Trickster: Find me the scissors to play. \n")
                                continue

                        if playerInput == '2':
                            print("\n From the old man's cloak, a key dangles. \n")
                            continue

                    if rpsWon == True:
                        print("\nTrickster: Good job on the win, traveller. I don't have much else to say to you.\n")
                        continue

                if playerInput == 'exit':
                    print("\n Action cancelled. \n")

                else:
                    print(errorMsg['unrecognizedCommand'])

            if playerInput == 'help':
                print("\nTalk to the old man and see what happens. \n")

                continue

            if playerInput == 'look around':
                print("\nYou see an old hooded man seated next to a desk. On the desk are two rocks, two papers and a pair of scissors. \n")
                continue
            
# south code
        if currentLevel == 'south':

            if prefix in commands['south']:
                if prefix == 'go':
                    if suffix in paths['south']:
                        print('Welcome back to the forest!')
                        currentLevel = 'forest'

                    else:
                        print(errorMsg['directionError'])
                if prefix=='look':
                    print("\nYou have now entered the south. You see a village and a gathering of people around the farmland.\n")

                if prefix == 'help':
                    print("Available commands: \n")
                    for command in commands['south']:
                        print(command.title())
                    print()

                if prefix == 'talk':
                    print('{c}: Welcome to the our humble village of meridiem-occidens!\n{c}: I have a key which I am willing to trade for services rendered.\n{c}: Our villagers need some help calculating the worth of their produce. Are you willing to help us?'.format(c='Cheifton'))

                    while currentLevel == 'south':
                        ans=input('>>> ').lower()
                        if ans=='yes':
                            print('{c}: Splendid!\n{c}: Lets go meet our first villager, {v1}.'.format(c='Cheifton', v1='Sal'))
                            print('{v1}: I have 200 carrots which each go for 10p.\n{v1}: I need to plant some potatoes, and each of them goes for 15p.\n{v1}: I need to make at least 5000p.\n{v1}: At least how many potatoes should I plant?'.format(v1='Sal'))
                            while True:
                                ans1=input('>>> ').lower()
                                if ans1=='200':
                                    print('{v1}: Thank you so much!'.format(v1='Sal'))
                                    break
                                else:
                                    print('Are you sure about that? Try again.')
                            print('{c}: Thank you for your help with {v1}, now I just need some help with another villager, {v2}.\n{c}: He lives in the {d}, so you\'ll need to travel there.\n{c}: I can safely say that you will receive both the keys, for both the south, as well as the west if you do this.'.format(c='Cheifton', v1='Sal', v2='Will', d='West'))
                            time.sleep(1.5)
                            print('Go {d} and meet {v2}.'.format(v2='Will', d='west'))
                            print("\nPlayer: Thank you.\n")
                            print("A farmer approaches.")
                            time.sleep(1.5)
                            print('{v2}: I was approached by merchant who offered me 3000p for 150 Carrots and 5 cattle.\n'.format(v2='Will'))
                            print("{v2}: Each carrot is worth 10p and each of my cattle is worth 250p.\n".format(v2="Will"))
                            print("{v2}: Am I making a profit, loss, or am I breaking even?\n".format(v2="Will"))
                            print("")
                            while True:
                                ans1=input('>>> ').lower()
                                if 'profit' in ans1:
                                    print('Will: Thank you so much!')
                                    break
                                else:
                                    print('Are you sure about that? Try again.')
                            print('{c}: Thank you for all your help!'.format(c='Cheifton'))
                            time.sleep(1.5)
                            playerInv['items'].append('g_key')
                            print("{c}: I do not actually have either of the keys.".format(c="Chiefton"))
                            time.sleep(1.5)
                            print("{c}: A Golden Key has been added to your inventory.".format(c="Chiefton"))
                            time.sleep(1.5)
                            print("{c}: Go to the forest and then go down, when you get there give the merchant the items you have as well as the Golden Key.".format(c="Chiefton"))
                            time.sleep(2.5)
                            print("{c}: In return, he will give you the final 2 keys, and you can make your way to freedom.\n{c}: Now type go north, to return to the forest.".format(c="Chiefton"))
                            paths['forest'].pop(paths['forest'].index('south'))
                            break
                        
                        elif ans == 'no':
                            print('Alright, see you later then.')
                            print('Welcome back to the forest!')
                            currentLevel='forest'

                        else:
                            print(errorMsg['unrecognizedCommand'])

            else:
                print(errorMsg['commandLVLunavailable'])

# down code
        if currentLevel == 'down':

            print('\n{m}: Welcome to the underground market, I am the merchant.\n{m}: The Cheifton says you have items you would like to trade in exchange for the south and the west keys.\n{m}: Alright, let me examine the items.\n'.format(m='The Merchant'))
            boolean=False
            for i in finalItemList:
                if i in playerInv['items']:
                    boolean=True
                elif boolean==False:
                    break
                else:
                    boolean=False
            if boolean==True:
                print('\nThe Merchant: Everything seems to be in order, here are the keys for your items.\n')
                playerInv['keys']+=2
                print('The Merchant: Now go up, and return to the forest. Then go north and complete the game!')
                playerInv['items'].clear()
                paths['forest'].pop(paths['forest'].index('down'))
            else:
                print('\nThe Merchant: You do not have the neccesary items.\n The Merchant: Go up and finish the other levels first, and collect the items!')

            playerInput = input(">>> ").lower()

            if len(playerInput.split()) > 1:
                prefix = playerInput.split()[0]
                suffix = playerInput.split()[1]
            else:
                prefix = playerInput.split()

            if prefix in commands['down']:
                if prefix == 'go':
                    if suffix in paths['down']:
                        print('Welcome back to the forest!')
                        currentLevel = 'forest'

                    else:
                        print(errorMsg['directionError'])

            else:
                print(errorMsg['commandLVLunavailable'])
            continue
            
    else:
        il_levels.end_screen()
        break
