from game_levels.titles import il_levels

il_levels = il_levels()
il_levels.show_title()

# global variables 
playerInv = {'items':[], 'keys':0}
print("You wake up in a forest with five paths in five directions - North, South, East, West, Down. \n In front of you is a gate with a scroll attached to its side. \n \n What do you do now?")
print("\n Commands: \n use [itemname] \n go [direction] \n Type in 'look around' to search the area \n Type in 'END GAME' to end the game. \n")

playerInput = ""
gateReq = 1

'''
Format for items:
items = {level_name:{itemname:[list of commands for the item]}}
'''
items = {'forest':{'scroll': ['use', 'drop', 'pick up'], 'gate': ['open']}}
paths = {'forest':['north', 'south', 'east', 'west', 'down']}

errorMsg = {'directionError':'You cannot go that way in this room'}

def msgs(item, msgType):
    switcher = {
        'dropitem':'You have dropped the '+item,
        'pickupItem':'You have picked up the '+item,
        'iteminInv':'You already have this item',
        'itemOutInv':'You do not have this item',
        'usedItem':'You used the '+item
    }
    print(switcher.get(msgType))

game_ended = False
while game_ended == False:
    playerInput = input(">>> ").lower()

    if playerInput != "end game":
        currentLevel = 'forest'
        prefix = playerInput.split()[0]
        suffix = playerInput.split()[1]

        if currentLevel == 'forest':
            level_items = items['forest']

            if prefix == 'go':
                if suffix in paths['forest']:
                    switcher = {
                        'north':'Unavailable',
                        'east':'Unavailable',
                        'west':'Unavailable',
                        'south':'Unavailable',
                        'down':'Unavailable'
                    }

                    print(switcher.get(suffix, errorMsg['directionError']))
                
                else:
                    print(errorMsg['directionError'])

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
                itemInInv = suffix in playerInv['items']
                if itemInInv == True:
                    msgs(suffix, 'iteminInv')
                else:
                    msgs(suffix, 'pickupItem')
                    playerInv['items'].append(suffix)
            
            if prefix == 'drop':
                itemInInv = suffix in playerInv['items']
                if itemInInv == True:
                    msgs(suffix, 'dropitem')
                    playerInv['items'].remove(suffix)
                else:
                    msgs(suffix, 'itemOutInv')
                    
            if playerInput == 'look around':
                print("\n You see: ")
                for item in level_items.keys():
                    print('- A', item.title())
            
            if prefix == 'open':
                if suffix == 'gate':
                    if playerInv['keys'] != 1:
                        print("The gate requires", gateReq, "keys to open.")
                    else:
                        print("The gate opens, and you walk through. You've made it home. Congratulations, player.")
                        il_levels.end_screen()
                        break
                if suffix == 'inventory':
                    print("\n Your Inventory: \n")
                    for itemType in playerInv:
                        print(itemType.title()+': ', playerInv[itemType])
                    print()

    else:
        print("Program terminating...")
        print("Thank you for playing!")
        break
