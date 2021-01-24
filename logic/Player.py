from database.player import *
from random import choice
from string import ascii_uppercase

class Player:
	Token = None
	HighID = None
	LowID = None
	DataDB = None

	def __init__(self):
		self.Token = Player.Token
		self.HighID = Player.HighID
		self.LowID = Player.LowID
		self.DataDB = Player.DataDB
		self.db = None

	def get_info(self):
		if self.Token:
			print('[INFO-DEBUG] Player::get_info()')
			db = DataBase()
			self.DataDB = json.loads(db.get_player_db(self.Token)[0][2])
			self.db = db
		else:
			print('[INFO-DEBUG-ERROR] Player::get_info() - Token is null')
			if self.LowID == 0:
				db = DataBase()
				self.db = db
				self.LowID = db.low_id_desc_db()
				self.Token = ''.join(choice(ascii_uppercase) for i in range(30))
				data = {'LowID': self.LowID,
							   'HighID': 0,
							   'name': 'NoName',
							   'resources': [
                                    {
                                        'id': 1, 
                                        'amount': 10000
                                    },
                                    {
                                        'id': 8, 
                                        'amount': 10000
                                    },
                                    {
                                        'id': 9, 
                                        'amount': 10000
                                    },
                                    {
                                        'id': 10, 
                                        'amount': 10000
                                    }
                               ],
							   'alliance': {},
							   'starPower': [],
							   'isName': 0,
							   'score': 5000,
							   'expLevel': 50,
							   'brawlers': [{'id': 0, 'powerPoints': 0, 'progress': 0, 'score': 0, 'stars': []}],
							   'banned': 0,
							   'gameRoom': {},
							   'homeBrawler': 0}
				db.create_player_db(self.LowID, self.Token, data)
				self.DataDB = json.loads(db.get_player_db(self.Token)[0][2])
				print(f'[INFO-DEBUG] Player::get_info() - creating account, TOKEN: {self.Token}')

	def set_name(self, name: str):
		self.DataDB["name"] = name
		self.DataDB["isName"] = 1
		self.db.update_data_db(self.DataDB, self.Token)

	def get_data_by_lowID(self, lowID: int):
		return json.loads(self.db.get_player_lowID_db(lowID)[0][2])

