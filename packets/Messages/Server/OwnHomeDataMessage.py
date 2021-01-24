from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class OwnHomeData(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 24101
        self.player = player

    def decode(self, buffer):
        Reader.__init__(self, buffer)

    def encode(self):
        Writer.__init__(self)
        self.writeVint(2020007)
        self.writeVint(75158)  # timestamp
        
        self.writeVint(self.player.DataDB["score"]) # Trophies
        self.writeVint(self.player.DataDB["score"]) # Max Trophies
        
        self.writeVint(122)
        self.writeVint(99)
        self.writeVint(99999) # 1262469
        
        self.writeVint(28) # csvID player_thumbnails.csv
        self.writeVint(0) # Icon Id
        
        self.writeVint(43) # csvID name_colors.csv
        self.writeVint(0) # Color Id
        
        self.writeVint(0)
        for x in range(0):
            pass
        self.writeVint(0)
        for x in range(0):
            pass
        self.writeVint(0)
        for x in range(0):
            pass
        # LogicSkins
        self.writeVint(0) # Opened Skins
        for x in range(0):
            pass
            
        self.writeVint(0)
        self.writeVint(122)
        self.writeVint(0)
        self.writeVint(1)

        self.writeBool(True)
        
        self.writeVint(0) # doubler tokens
        self.writeVint(0) # league rewards end time
        self.writeVint(491279)
        
        self.writeVint(6037352)
        self.writeVint(200)
        self.writeVint(200)
        self.writeVint(5)
        for x in [93, 206, 456, 1001, 2264]:
            self.writeVint(x)

        self.writeByte(4) # 3 bool

        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(100) # available tokens
        self.writeVint(0)

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(100008)
        self.writeVint(0)
        
        self.writeVint(16) # csvID characters.csv
        self.writeVint(0) # Brawler in Menu
        
        self.writeString("RU")
        self.writeString("27")
        
        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(1)
        for x in range(1):
            self.writeVint(0) 
            self.writeVint(100) # brawl pass points

            self.writeVint(1) # level completed brawl pass
            self.writeVint(0) # Brawll pass rewards taken

            self.writeBool(False) # premium brawl pass

            self.writeVint(0)

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeBool(True)
        self.writeVint(0)

        self.writeBool(True)
        self.writeVint(0)

        self.writeVint(2020141)
        self.writeVint(100)
        self.writeVint(10)
        self.writeVint(0) # Big Box Amount
        self.writeVint(3) # Big Box Multiplier
        self.writeVint(0) # # Mega Box Amount
        self.writeVint(10)  # Mega Box Multiplier
        self.writeVint(40) # Doubler Tokens Amount
        self.writeVint(1000) # Doubler Tokens Count
        self.writeVint(550)
        self.writeVint(0)
        self.writeVint(999900)

        self.writeVint(6)
        for x in [0, 30, 80, 170, 350, 0]:
            self.writeVint(x)

        self.writeVint(8) # ???
        for x in range(8):
            self.writeVint(x)
        
        self.writeVint(4)
        for x in range(4):
            self.writeVint(0)
            self.writeVint(x)
            self.writeVint(0)
            self.writeVint(75992)
            self.writeVint(10)

            self.writeVint(15) # csv
            self.writeVint(x)

            self.writeVint(3)

            self.writeString()

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            for x in range(0):
                self.writeVint(x)

            self.writeVint(0)
            self.writeVint(0)

        # wtf supercell... who? why? chalanges? 
        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeVint(x)
            self.writeVint(0)
            self.writeVint(75992)
            self.writeVint(10)

            self.writeVint(49) # csv
            self.writeVint(x)

            self.writeVint(3)

            self.writeString()

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            for x in range(0):
                self.writeVint(x)

            self.writeVint(0)
            self.writeVint(0)

        
        self.writeVint(8) # ????
        for x in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(x)

        self.writeVint(8) # ????
        for x in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(x)

        self.writeVint(3)
        for x in [10, 30, 80]: # Tickets Amount
            self.writeVint(x)

        self.writeVint(3) 
        for x in [6, 20, 60]: # Tickets Count
            self.writeVint(x)

        self.writeVint(4) 
        for x in [20, 50, 140, 280]: # Gold Amount
            self.writeVint(x)

        self.writeVint(4)
        for x in [150, 400, 1200, 2600]: # Gold Count
            self.writeVint(x)


        self.writeVint(2)
        self.writeVint(200) # Max Tokens
        self.writeVint(20) # Plus Tokens
        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)

        self.writeByte(6) # bool

        self.writeVint(50)
        self.writeVint(604800)

        self.writeBool(True)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeInt32(0)
        self.writeInt32(1)

        self.writeVint(0)
        self.writeVint(-1)

        self.writeBool(False)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0) # high id
        self.writeVint(1) # low id

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeString(self.player.DataDB["name"]) # name player
        self.writeBool(self.player.DataDB["isName"]) # is there a name

        self.writeVint(-1207959552) # count commodity ??? 

        self.writeVint(4)

        #for x in [23, 0, 1, 23, 4, 1]:
            #self.writeVint(x)
        """
        Resoucres: 
           1 - Gold (points mini box),
           8 - upgradium (gold),
           9 - bolts (points big box),
           10 - HeroLvlUpMaterial (Star points)
        """
        for resource in self.player.DataDB['resources']:
            self.writeVint(5)  # resources.csv id
            self.writeVint(resource['id'])
            self.writeVint(resource['amount'])

        self.writeVint(0)
        for x in range(0):
            pass
        self.writeVint(0)
        for x in range(0):
            pass
        self.writeVint(0)
        for x in range(0):
            pass
        self.writeVint(0)
        for x in range(0):
            pass
        self.writeVint(0)
        for x in range(0):
            pass
        self.writeVint(0)
        for x in range(0):
            pass
        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(6666) # Gems
        self.writeVint(0)
        self.writeVint(99)
        self.writeVint(100)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        
        self.writeVint(1589967120)
