'''
Each level has the following:

itemList
directions to go
available commands

for items, it's best to define each item as a function. the function is called whenever the item is used. 

'''


playerInv = {'items':[], 'keys':0}
goVar = ['Go', 'go', 'GO']
useVar = ['Use', 'use', 'USE']
northVar = ['North', 'north', 'NORTH']
southVar = ['South', 'south', 'SOUTH']
eastVar = ['east', 'East', 'EAST']
westVar = ['west', 'West', 'WEST']
downVar = ['down', 'Down', 'DOWN']

itemList = ['cloth', 'scroll']

print("You wake up in a forest with five paths in five directions - North, South, East, West, Down. \n In front of you is a gate with a scroll attached to its side. \n \n What do you do now?")

print("\n Commands: \n use [itemname] \n go [direction] \n Type in 'look around' to search the area \n Type in 'END GAME' to end the game. \n")

playerInput = ""
while playerInput != "END GAME":
    playerInput = input(">>> ")
    prefix = playerInput.split()[0]
    suffix = playerInput.split()[1]
    if prefix in goVar:
        if suffix in northVar:
            print('ok')
        if suffix in southVar:
            print('eeh')
        if suffix in westVar:
            print('west')
        if suffix in downVar:
            print('down')
        if suffix in eastVar:
            print('east')
    elif prefix in useVar:
        if suffix in itemList:
            if suffix in playerInv['items']:
                print("You used the", suffix)
            else:
                print("Item isn't in your inventory")
        else:
            print("Item isn't in your inventory")
    if playerInput == 'look around':
        print("You find the following items in the area: ", end='')
        for item in itemList:
            print(item, end=', ')
        print()
