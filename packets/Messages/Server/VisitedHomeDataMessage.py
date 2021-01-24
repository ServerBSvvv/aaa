from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class VisitedHomeDataMessage(Message):
    def __init__(self, dataDB):
        super().__init__()
        self.id = 24113
        self.dataDB = dataDB

    def decode(self, buffer):
        Reader.__init__(self, buffer)

    def encode(self):
        Writer.__init__(self)
        self.writeVint(0)
        self.writeVint(self.dataDB["LowID"])

        self.writeVint(0)
        self.writeVint(0) # Count brawlers

        self.writeVint(14) # Count array
        for x in range(14):
            self.writeVint(x + 1) 
            self.writeVint(x)

        self.writeString(self.dataDB["name"])  # Name 
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeBool(False) # Is club
        self.writeVint(0)
