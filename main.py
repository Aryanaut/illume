from game_levels.titles import il_levels

il_levels = il_levels()
il_levels.show_title()

# global variables 
playerInv = {'items':[], 'keys':0}
print("You wake up in a forest with five paths in five directions - North, South, East, West, Down. \n In front of you is a gate with a scroll attached to its side. \n \n What do you do now?")
print("\n Commands: \n use [itemname] \n go [direction] \n Type in 'look around' to search the area \n Type in 'END GAME' to end the game. \n")

playerInput = ""
gateReq = 3
currentLevel = 'forest'

enteredForest = True
enteredEast = False
enteredWest = False
enteredSouth = False
enteredDown = False
enteredNorth = False

'''
Format for items:
items = {level_name:{itemname:[list of commands for the item]}}
'''
items = {'forest':{'scroll': ['use', 'drop', 'pickup'], 'gate': ['open']}, 
        'east':{'trickster':['talk', 'play']}}

commands  = {'forest':['look', 'go', 'pickup', 'drop', 'use', 'open'],
            'east':['look', 'go', 'pickup', 'drop', 'give'],
            'down':['go', 'look'],
            'south':['look', 'go', 'talk', 'help']}

paths = {'forest':['north', 'south', 'east', 'west', 'down'], 'east':['west'],
        'west':['east'], 'down':['up'], 'south':['north'], 'north':['south']}

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

def noWinRPS(playerInput):
    switcher = {
        'rock':'paper',
        'paper':'scissors',
        'scissors':'rock'
    }
    response = switcher.get(playerInput)
    return response

finalItemList=['rock', 'paper', 'scissors', 'G_Key']
def south():
    global currentLevel

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
            print('You go {d} and meet {v2}.'.format(v2='Will', d='west'))
            print('{v2}: I was approached by merchant who offered me 3000p for 150 Carrots and 5 cattle.\n{v2}: Each carrot is worth 10p and each of my cattle is worth 250p.\n{v2}: Am I making a profit, loss, or am I breaking even?'.format(v2='Will'))
            while True:
                ans1=input('>>> ').lower()
                if 'profit' in ans1:
                    print('Will: Thank you so much!')
                    break
                else:
                    print('Are you sure about that? Try again.')
            print('{c}: Thank you for all your help! I do not actually have either of the keys. However please take this.\nA Golden Key has been added to your inventory.\n{c}: Go to the forest and then go down, when you get there give the merchant the items you have as well as the Golden Key.\n{c}: In return, he will give you the final 2 keys, and you can make your way to freedom.'.format(c='Cheifton'))
            playerInv['items'].append('G_Key')
            continue
        
        else:
            print('Alright, see you later then.')

        if len(ans.split()) > 1:
            prefix = ans.split()[0]
            suffix = ans.split()[1]
        else:
            prefix = ans.split()

        if prefix in commands['south']:
            if prefix == 'go':
                if suffix in paths['south']:
                    currentLevel = 'forest'
                    continue

                else:
                    print(errorMsg['directionError'])

            if prefix == 'help':
                print("Available commands: \n")
                for command in commands['south']:
                    print(command)

            if prefix == 'talk':
                print('{c}: Welcome to the our humble village of meridiem-occidens!\n{c}: I have a key which I am willing to trade for services rendered.\n{c}: Our villagers need some help calculating the worth of their produce. Are you willing to help us?'.format(c='Cheifton'))
                continue

        else:
            print(errorMsg['commandLVLunavailable'])

def west():
    print('{c}: Welcome to the our humble village of meridiem-occidens!\n{c}: I have a key which I am willing to trade for services rendered.\n{c}: Our villagers need some help calculating the worth of their produce. Are you willing to help us?'.format(c='Cheifton'))
    while True:
        ans=input('>>> ').lower()
        if ans=='yes':
            print('{c}: Splendid!\n{c}: Lets go meet our first villager, {v1}.'.format(c='Cheifton', v1='Will'))
            print('{v1}: I have 200 carrots which each go for 10p.\n{v1}: I need to plant some potatoes, and each of them goes for 15p.\n{v1}: I need to make at least 5000p.\n{v1}: At least how many potatoes should I plant?'.format(v1='Will'))
            while True:
                ans1=input('>>> ')
                if ans1=='200':
                    print('{v1}: Thank you so much!'.format(v1='Sal'))
                    break
                else:
                    print('Are you sure about that? Try again.')

            print('{c}: Thank you for your help with {v1}, now I just need some help with another villager, {v2}.\n{c}: He lives in the {d}, so you\'ll need to travel there.\n{c}: I can safely say that you will receive both the keys, for both the south, as well as the west if you do this.'.format(c='Cheifton', v1='Will', v2='Sal', d='south'))
            print('You go {d} and meet {v2}.'.format(v2='Sal', d='south'))
            print('{v2}: I was approached by merchant who offered me 3000p for 150 Carrots and 5 cattle.\n{v2}: Each carrot is worth 10p and each of my cattle is worth 250p.\n{v2}: Am I making a profit, loss, or am I breaking even?'.format(v2='Sal'))
            while True:
                ans1=input('>>> ')
                if 'profit' in ans1:
                    print('Sal: Thank you so much!')
                    break
                else:
                    print('Are you sure about that? Try again.')
            print('{c}: Thank you for all your help! I do not actually have either of the keys. However please take this.\nA Golden Key has been added to your inventory.\n{c}: Go to the forest and then go down, when you get there give the merchant the items you have as well as the Golden Key.\n{c}: In return, he will give you the final 2 keys, and you can make your way to freedom.'.format(c='Cheifton'))
            playerInv['items'].append('G_Key')
            break
        else:
            print('Are you sure? Try again.')

def down():
    global currentLevel
    print('{m}: Welcome to the underground market, I am the merchant.\n{m}: The Cheifton says you have items you would like to trade in exchange for the south and the west keys.\n{m}: Alright, let me examine the items.'.format(m='The Merchant'))

    if playerInv['items']==finalItemList:
        print('\nThe Merchant: Everything seems to be in order, here are the keys for your items.\n')
        playerInv['keys']+=2
    else:
        print('\nThe Merchant: You do not have the neccesary items.\n')

    playerInput = input(">>> ").lower()

    if len(playerInput.split()) > 1:
        prefix = playerInput.split()[0]
        suffix = playerInput.split()[1]
    else:
        prefix = playerInput.split()

    if prefix in commands['down']:
        if prefix == 'go':
            if suffix in paths['down']:
                currentLevel = 'forest'

            else:
                print(errorMsg['directionError'])

    else:
        print(errorMsg['commandLVLunavailable'])



game_ended = False
while game_ended == False:

    playerInput = input(">>> ").lower()

    if playerInput != "end game":
        
        if len(playerInput.split()) > 1:
            prefix = playerInput.split()[0]
            suffix = playerInput.split()[1]
        else:
            prefix = playerInput.split()
            
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
                            print("unavailable")
                        if suffix == 'south':
                            currentLevel = 'south'

                        if suffix == 'west':
                            currentLevel = 'west'

                        if suffix == 'down':
                            currentLevel = 'down'

                        if suffix == 'east':
                            currentLevel = 'east'
                            enteredEast = True
                    
                    else:
                        print(errorMsg['directionError'])

                    continue

                if prefix == 'use':
                    if suffix in level_items.keys():
                        if suffix in playerInv['items']:
                            msgs(suffix, 'usedItem')
                            if prefix in level_items[suffix]:
                                if suffix == 'scroll':
                                    print("The scroll reads: \n Find the five keys to open the gate \n and make your way home.")
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
                        print('- A', item.title())
                    print()
                
                if prefix == 'open':
                    if suffix == 'gate':
                        if playerInv['keys'] != 1:
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

            if enteredEast == True:
                print("\n Area: Trickster's lair \n")
                print("What do you do now? [type in 'help' to see options] \n")
                enteredEast = False

            if prefix == 'go':
                if suffix in paths['east']:
                    if suffix == 'west':
                        currentLevel = 'forest'
                        enteredForest = True
                else:
                    print(errorMsg['directionError'])
            
            if playerInput == 'talk':
                print("\n To? \n - The old hooded man [type in 'trickster'] \n Type in 'Exit' to cancel action." )
                playerInput = input(">>> ").lower()

                if playerInput == 'trickster':
                    print("\n Trickster: Greetings wanderer!")
                    print("\n Choose your response: \n [1] Say hello \n [2] Look around")
                    playerInput = input(">>> ").lower()

                    if playerInput == '1':
                        print("\n Trickster: I'd play for the key, but I'm missing a piece for my game. It's a pair of scissors. Have you seen it?")
                        playerInput = input("Yes or no? \n>>> ").lower()

                        if playerInput == 'yes':
                            if 'scissors' in playerInv['items']:
                                playerInv['items'].remove('scissors')
                                playerInput = input("\n Trickster: Thank you, wanderer. Would you like to play? Winner takes the key. (Yes or no?)\n>>> ").lower()
                                
                                if playerInput == 'yes':
                                    print("\n Trickster: Game's simple. Rock beats Scissors, Scissors cuts Paper, Paper covers rock. Winner takes key. \n")
                                    print("Enter your choice (Rock, Paper or Scissors)")
                                    print("game is still being built here.")

                                    continue
                                
                                if playerInput == 'no':
                                    print("\n Trickster: Later, then.")
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
                        print("\n From the old man's cloak, a golden key dangles. \n")
                        continue

                if playerInput == 'exit':
                    print("\n Action cancelled. \n")

                else:
                    print(errorMsg['unrecognizedCommand'])

            if playerInput == 'help':
                print("\nTalk to the old man and see what happens. \n")

                continue

            if playerInput == 'look around':
                print("You see an old hooded man seated next to a desk. On the desk are two rocks, two papers and a pair of scissors. \n")
                continue

        if currentLevel == 'south':
            south()
            continue

        if currentLevel == 'west':
            west()
            continue

        if currentLevel == 'down':
            down()
            continue
            
    else:
        print("Program terminating...")
        print("Thank you for playing!")
        break
        