
#todo: import global constants and user information
#from glob import constants, user_info
from glob_const import *
import irc_cmd

import logging

# class definition
class repeater:
	
	def __init__(self):
		self.logger = logging.getLogger(__name__)
		self.logger.info("Initialize")
	
	def get_irc_cmds(self):
		
		self.logger.info("entry: get_irc_cmds")
		irc_cmds = ['PRIVMSG']
		return irc_cmds
	
	def run_module(self, msg, sock_send, bot_info):
		
		self.logger.info("entry: repeater.run_module")
		
		username = (msg.split()[0]).split('!')[0][1:]
		data = ' '.join(msg.split()[3:])[1:]
		channel = msg.split()[2]
		if channel[:1] == ':':
			channel = channel[1:]
		
		self.logger.info(data)
		if data.find(bot_info['nick']) != -1:
			self.logger.info("nick has been found")
			data = data.replace(bot_info['nick'], username)
			sock_send(irc_cmd.cmd_privmsg(channel, data))
	
# store class name in this variable
# what are the security risks in this?
Class = repeater
