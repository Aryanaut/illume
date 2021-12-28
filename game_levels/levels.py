class il_levels:
    def __init__(self):
        self.txt_dir = "game_levels/txt_files/"
        self.playerInv = {'items':[], 'keys':0}

    def show_title(self):
        titleFile = self.txt_dir + "template_title.txt"
        title = open(titleFile, 'r').read()
        # opening title
        print(title)
