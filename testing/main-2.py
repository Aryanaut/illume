from game_levels.titles import il_levels

il_levels = il_levels()
il_levels.show_title()

class Illume:
    def __init__(self):
        self.playerInv = {'items':[], 'keys':0}
        print("You wake up in a forest with five paths in five directions - North, South, East, West, Down. \n In front of you is a gate with a scroll attached to its side. \n \n What do you do now?")
        print("\n Commands: \n use [itemname] \n go [direction] \n Type in 'look around' to search the area \n Type in 'END GAME' to end the game. \n")

        self.items = {'forest':{'scroll': ['use', 'drop', 'pick up'], 'gate': ['open']}, 
        'east':{'trickster':['talk', 'play']}}

        self.errorMsg = {'directionError':'You cannot go that way in this room', 
            'unrecognizedCommand':'The game does not recognize this command.',
            'actionNotForItem':'This action cannot be performed on this item.',
            'commandLVLunavailable':'This action cannot be performed in this level.'}

        self.debugging_commands = {'debugadd':'debugadd [itemname]', 'debugremove':'debugremove [itemname]'}

        self.paths = {'forest':['north', 'south', 'east', 'west', 'down'], 
                        'east':['west'],
                        'west':['east']}

        self.commands  = {'forest':['look', 'go', 'pickup', 'drop', 'use', 'open'],
            'east':['look', 'go', 'pickup', 'drop', 'give']}

        self.gateReq = 1
        self.currentLevel = 'forest'

        self.entered = {
                        "forest":True,
                        "south":False,
                        "east":False,
                        "west":False,
                        "north":False,
                        "down":False
        }
        self.finalItemList = ['rock', 'paper', 'scissors', 'G_Key']

        self.game_ended = False

    def msgs(self, item, msgType):
        switcher = {
            'dropitem':'You have dropped the '+item,
            'pickupItem':'You have picked up the '+item,
            'iteminInv':'You already have this item',
            'itemOutInv':'You do not have this item',
            'usedItem':'You used the '+item
        }
        print(switcher.get(msgType))

    def levelSwitcher(self, currentLevel, enteredLevel):
        self.entered[currentLevel] = False
        self.entered[enteredLevel] = True

    def noWinRPS(self, playerInput):
        switcher = {
            'rock':'paper',
            'paper':'scissors',
            'scissors':'rock'
        }
        response = switcher.get(playerInput)
        return response

    def south(self):

        print('{c}: Welcome to the our humble village of meridiem-occidens!\n{c}: I have a key which I am willing to trade for services rendered.\n{c}: Our villagers need some help calculating the worth of their produce. Are you willing to help us?'.format(c='Cheifton'))
        while True:
            ans=input('>>> ').lower()
            if ans=='yes':
                print('{c}: Splendid!\n{c}: Lets go meet our first villager, {v1}.'.format(c='Cheifton', v1='Sal'))
                print('{v1}: I have 200 carrots which each go for 10p.\n{v1}: I need to plant some potatoes, and each of them goes for 15p.\n{v1}: I need to make at least 5000p.\n{v1}: At least how many potatoes should I plant?'.format(v1='Sal'))
                while True:
                    ans1=input('>>> ')
                    if ans1=='200':
                        print('{v1}: Thank you so much!'.format(v1='Sal'))
                        break
                    else:
                        print('Are you sure about that? Try again.')
                print('{c}: Thank you for your help with {v1}, now I just need some help with another villager, {v2}.\n{c}: He lives in the {d}, so you\'ll need to travel there.\n{c}: I can safely say that you will receive both the keys, for both the south, as well as the west if you do this.'.format(c='Cheifton', v1='Sal', v2='Will', d='West'))
                print('You go {d} and meet {v2}.'.format(v2='Will', d='west'))
                print('{v2}: I was approached by merchant who offered me 3000p for 150 Carrots and 5 cattle.\n{v2}: Each carrot is worth 10p and each of my cattle is worth 250p.\n{v2}: Am I making a profit, loss, or am I breaking even?'.format(v2='Will'))
                while True:
                    ans1=input('>>> ')
                    if 'profit' in ans1:
                        print('Will: Thank you so much!')
                        break
                    else:
                        print('Are you sure about that? Try again.')
                print('{c}: Thank you for all your help! I do not actually have either of the keys. However please take this.\nA Golden Key has been added to your inventory.\n{c}: Go to the forest and then go down, when you get there give the merchant the items you have as well as the Golden Key.\n{c}: In return, he will give you the final 2 keys, and you can make your way to freedom.'.format(c='Cheifton'))
                self.playerInv['items'].append('G_Key')
                break
            else:
                print('Are you sure? Try again.')

    def west(self):

        print('{c}: Welcome to the our humble village of meridiem-occidens!\n{c}: I have a key which I am willing to trade for services rendered.\n{c}: Our villagers need some help calculating the worth of their produce. Are you willing to help us?'.format(c='Cheifton'))
        while True:

            ans=input('>>> ').lower()
            if len(ans.split()) > 1:
                prefix = ans.split()[0]
                suffix = ans.split()[1]
            else:
                prefix = ans.split()

            if prefix == 'go':
                if suffix in self.paths['west']:
                    self.levelSwitcher('west', 'forest')


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
                self.playerInv['items'].append('G_Key')
                break
            else:
                print('Are you sure? Try again.')

    def down(self):
        print('{m}: Welcome to the underground market, I am the merchant.\n{m}: The Cheifton says you have items you would like to trade in exchange for the south and the west keys.\n{m}: Alright, let me examine the items.'.format(m='The Merchant'))
        if self.playerInv['items'] == self.finalItemList:
            print('\nThe Merchant: Everything seems to be in order, here are the keys for your items.\n')
            self.playerInv['keys']+=2
        else:
            print('\nThe Merchant: You do not have the neccesary items.\n')

    def forest(self):
        while True:
            playerInput = input(">>> ").lower()
            level_items = self.items['forest']

            if len(playerInput.split()) > 1:
                prefix = playerInput.split()[0]
                suffix = playerInput.split()[1]
            else:
                prefix = playerInput.split()
                
            # fix the level switcher
            if prefix in self.commands['forest']:
                if prefix == 'go':
                    if suffix in self.paths['forest']:
                        if suffix == 'north':
                            print("unavailable")

                        if suffix == 'south':
                            self.levelSwitcher('forest', 'south')

                        if suffix == 'west':
                            self.levelSwitcher('forest', 'west')

                        if suffix == 'down':
                            self.levelSwitcher('forest', 'down')

                        if suffix == 'east':
                            self.levelSwitcher('forest', 'east')
                    
                    else:
                        print(self.errorMsg['directionError'])

                    continue

                if prefix == 'use':
                    if suffix in level_items.keys():
                        if suffix in self.playerInv['items']:
                            self.msgs(suffix, 'usedItem')
                            if prefix in level_items[suffix]:
                                if suffix == 'scroll':
                                    print("The scroll reads: \n Find the five keys to open the gate \n and make your way home.")
                            else:
                                print("This command is not available for this item")
                        else:
                            self.msgs(suffix, 'itemOutInv')

                if prefix == 'pickup':
                    if 'pickup' in level_items[suffix]:
                        itemInInv = suffix in self.playerInv['items']
                        if itemInInv == True:
                            self.msgs(suffix, 'iteminInv')
                        else:
                            self.msgs(suffix, 'pickupItem')
                            self.playerInv['items'].append(suffix)
                    else:
                        print(self.errorMsg['actionNotForItem'])
                
                if prefix == 'drop':
                    if 'drop' in level_items[suffix]:
                        itemInInv = suffix in self.playerInv['items']
                        if itemInInv == True:
                            self.msgs(suffix, 'dropitem')
                            self.playerInv['items'].remove(suffix)
                        else:
                            self.msgs(suffix, 'itemOutInv')
                    else:
                        print(self.errorMsg['actionNotForItem'])
                        
                if playerInput == 'look around':
                    print("\n You see: ")
                    for item in level_items.keys():
                        print('- A', item.title())
                    print()
                
                if prefix == 'open':
                    if suffix == 'gate':
                        if self.playerInv['keys'] != 1:
                            print("The gate requires", self.gateReq, "keys to open.")
                        else:
                            print("The gate opens, and you walk through. You've made it home. Congratulations, player.")
                            il_levels.end_screen()
                            self.game_ended = True
                            break
                    else:
                        print(self.errorMsg['unrecognizedCommand'])
            else:
                print(self.errorMsg['commandLVLunavailable'])

    def east(self):
        while True:
            playerInput = input(">>> ").lower()

            level_items = self.items['east']

            if len(playerInput.split()) > 1:
                prefix = playerInput.split()[0]
                suffix = playerInput.split()[1]
            else:
                prefix = playerInput.split()

            if enteredEast == True:
                print("\n Area: Trickster's lair \n")
                print("What do you do now? [type in 'help' to see options] \n")
                enteredEast = False

            if prefix == 'go':
                if suffix in self.paths['east']:
                    if suffix == 'west':
                        currentLevel = 'forest'
                        enteredForest = True
                else:
                    print(self.errorMsg['directionError'])
            
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
                            if 'scissors' in self.playerInv['items']:
                                self.playerInv['items'].remove('scissors')
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
                                    print(self.errorMsg['unrecognizedCommand'])
                                    continue
                            else:
                                print(self.msgs('scissors', 'itemOutInv'))
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
                    print(self.errorMsg['unrecognizedCommand'])

            if playerInput == 'help':
                print("\nTalk to the old man and see what happens. \n")

                continue

            if playerInput == 'look around':
                print("You see an old hooded man seated next to a desk. On the desk are two rocks, two papers and a pair of scissors. \n")
                continue

    def mainLoop(self):
        while self.game_ended == False:
            if self.currentLevel == 'forest':
                self.forest()
            elif self.currentLevel == 'south':
                self.south()
            elif self.currentLevel == 'east':
                self.east()
            elif self.currentLevel == 'west':
                self.west()
            elif self.currentLevel == 'down':
                self.down()


def main():
    game = Illume()
    game.mainLoop()

if __name__ == '__main__':
    main()