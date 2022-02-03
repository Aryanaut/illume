inp_string = input("You wake up in a forest. What do you do? \n >>> ").lower()

if inp_string == 'go north':
    print("You are now at the base of a mountain")
if inp_string == 'go south':
    print("You are still in a forest")
if inp_string == 'go east':
    print("You arrive at a village and are greeted by a friendly old wizard.")
if inp_string == 'end game':
    print("Game ending...")
    print("Try again later!")    
else:
    print("You face a massive dungeon, its door sealed and guarded by two towering giants. The giants find your presense insulting and scare you away with massive clubs.")