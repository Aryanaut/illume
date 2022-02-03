class il_levels:
    def __init__(self):
        self.txt_dir = "game_levels/txt_files/"
        self.playerInv = {'items':[], 'keys':0}

    def show_title(self):
        titleFile = self.txt_dir + "template_title.txt"
        title = open(titleFile, 'r').read()
        # opening title
        print(title)

    def show_forest(self):
        forestFile = self.txt_dir + "forest_title.txt"
        title = open(forestFile, 'r').read()
        print(title)

    def show_market(self):
        forestFile = self.txt_dir + "market_title.txt"
        title = open(forestFile, 'r').read()
        print(title)

    def show_village(self):
        forestFile = self.txt_dir + "village_title.txt"
        title = open(forestFile, 'r').read()
        print(title)

    def end_screen(self):
        print("\nPrograming terminating...\n")
        endFile = self.txt_dir + "game_ended.txt"
        print(endFile)
        
        print("\nThank you for playing!\n")
