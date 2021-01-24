from packets.Messages import Message
from packets.Messages.Server.LoginOkMessage import LoginOk
from packets.Messages.Server.OwnHomeDataMessage import OwnHomeData


class LoginMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 18101
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)
        highID = self.readUInt32()
        lowID = self.readUInt32()
        token = self.readString()  # Pass Token
        major = self.readUInt32()
        revision = self.readUInt32()
        build = self.readUInt32()
        master_hash = self.readString()
        phone_model = self.readString()
        locale_key = self.readShort()
        language = self.readString()
        os_version = self.readString()
        is_android = self.readBool()
        self.readString()
        android_device_id = self.readString()
        self.readBool()  # isAdvertisingTrackingEnabled
        self.readString()  # vendor_uuid
        self.readUInt32()
        self.readUByte()
        version = self.readString()

        [self.readByte() for x in range(49)]  # idk what is it

        if self.readBool():  # Ultra info
            self.readString()

        self.player.Token = token
        self.player.HighID = highID
        self.player.LowID = lowID
        self.player.get_info()

    def process(self):
        login_ok = LoginOk(self.player)
        login_ok.encode()
        login_ok.pack()

        ohd = OwnHomeData(self.player)
        ohd.encode()
        ohd.pack()
        self.buffer = login_ok.buffer
        self.buffer += ohd.buffer
