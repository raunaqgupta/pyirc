
#todo: import global constants and user information
#from glob import constants, user_info
from glob_const import *
import irc_cmd

import logging

# class definition
class greetings:
	
	def __init__(self):
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Initialize")
	
	def get_irc_cmds(self):
		irc_cmds = ['JOIN', 'PART']
		return irc_cmds
	
	def run_module(self, msg, sock_send, bot_info):
		self.logger.debug("Entry")
		
		if msg.find( CONST_JOIN ) != -1:
			username = (msg.split()[0]).split('!')[0][1:]
			print username
			print bot_info
			if username != bot_info['nick']:
				channel = msg.split()[2]
				if channel[:1] == ':':
					channel = channel[1:]
				msg = 'Hello ' + username + '. Welcome to the ' + channel + ' channel.'
				sock_send(irc_cmd.cmd_privmsg(channel, msg))
	
# store class name in this variable
# what are the security risks in this?
Class = greetings
