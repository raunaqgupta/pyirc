
#todo: import global constants and user information
#from glob import constants, user_info
from glob_const import *
import irc_cmd

# class definition
class help:
	
	def __init__(self):
		print 'general_module loaded'
	
	def get_irc_cmds(self):
		irc_cmds = ['PRIVMSG']
		return irc_cmds
	
	def run_module(self, msg, sock_send, bot_info):
		print 'help.run_module'
		data = msg.split()[2]
		
		sock_send(irc_cmd.cmd_privmsg(channel, msg))
	
# store class name in this variable
# what are the security risks in this?
Class = help
