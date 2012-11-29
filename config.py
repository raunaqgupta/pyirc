import json
import logging

class config:
	
	def __init__(self, filename):
		
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Initialize")
		
		self._fileptr = open(filename)
		self._json_list = json.load(self._fileptr)
	
	def get_server_info(self):
		
		self.logger.debug("Entry")
		return self._json_list['server']
	
	def get_bot_info(self):
		
		self.logger.debug("Entry")
		return self._json_list['bot']
	
	def get_info(self, key):
		self.logger.debug("Entry")
		if key in self._json_list:
			return self._json_list[key]
		else:
			return -1
