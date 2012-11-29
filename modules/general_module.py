
#todo: import global constants and user information
#from glob import constants, user_info
from glob_const import *
import irc_cmd

import logging

# class definition
class general_module:
	
	def __init__(self):
		
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Initialize")
	
	def get_irc_cmds(self):
		irc_cmds = ['PING']
		return irc_cmds
	
	def run_module(self, msg, sock_send, bot_info):
		self.logger.debug("Entry")
		if msg.find( CONST_PING ) != -1:
			sock_send(irc_cmd.cmd_pong(msg.split()[1]))
	
# store class name in this variable
# what are the security risks in this?
Class = general_module
