
#todo: import global constants and user information
#from glob import constants, user_info
from glob_const import *
import irc_cmd

import logging
import os

# class definition
class chan_log:
	
	def __init__(self):
		
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Initialize")
		
		# configure via config.json
		self._conf = config_obj.get_info("chan_log")
		if self._conf != -1:
			dir_path = os.path.abspath(self._conf["path"])
			self.logger.debug(dir_path)
			
			if not os.access(dir_path, os.F_OK):
				os.mkdir(dir_path)
			
			server_name = config_obj.get_server_info()["name"]
			
			server_dir_path = dir_path + "/" + server_name
			if not os.access(server_dir_path, os.F_OK):
				os.mkdir(server_dir_path)
			
			chan_list = config_obj.get_server_info()["channels"]
			self._chan_dict = {}
			for channel in chan_list:
				self._chan_dict[channel] = [server_dir_path + "/" + channel]
				if not os.access(chan_dict[channel][0], os.F_OK | os.W_OK):
					if self._conf["overwrite"] == "0":
						self._chan_dict[channel].append(open(chan_dict[channel][0], "a"))
					else:
						self._chan_dict[channel].append(open(chan_dict[channel][0], "w"))
			
	
	def get_irc_cmds(self):
		irc_cmds = ["PRIVMSG", "NOTICE", "JOIN", "PART"]
		return irc_cmds
	
	def run_module(self, msg, sock_send, bot_info):
		self.logger.debug("Entry")
		
		
		
	
# store class name in this variable
# what are the security risks in this?
Class = chan_log
