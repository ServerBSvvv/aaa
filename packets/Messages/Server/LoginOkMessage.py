from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class LoginOk(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 20104
        self.player = player
        print(self.player.Token)

    def decode(self, buffer):
        Reader.__init__(self, buffer)

    def encode(self):
        Writer.__init__(self)
        self.writeInt32(0)
        self.writeInt32(self.player.LowID)
        # HighID, lowID
        self.writeInt32(0)
        self.writeInt32(self.player.LowID)
        # HighID, lowID
        self.writeString(self.player.Token)  # Token
        self.writeString()
        self.writeString()
        self.writeInt32(27)  # MajorVersion
        self.writeInt32(0)  # Build
        self.writeInt32(0)  # MinorVersion
        self.writeString("prod")  # Environment
        self.writeInt32(1) 
        self.writeInt32(1)  
        self.writeInt32(62) 
        self.writeString()  
        self.writeString() 
        self.writeString()  
        self.writeInt32(0)
        self.writeString() 
        self.writeString("IL")
        self.writeString()
        self.writeInt32(1)
        self.writeString()  
        self.writeString() 
        self.writeString() 
        self.writeVint(0)
        self.writeString()
        self.writeVint(1)
