
from glob_const import *

class msgparser:
	
	def __init__(self, in_msg):
		self._in_msg = in_msg
		self._msg_list = self._in_msg.split()
	
	#get command
	def fn_get_cmd(self):
		
		if(self._msg_list[0][:1] == CONST_COLON):
			return self._msg_list[1]
		else:
			return self._msg_list[0]
	
	#search command
	# todo
	def fn_search_cmd(self, in_cmd):
		
		msg_cmd = ''
		if(self._msg_list[0] == CONST_PING):
			msg_cmd = CONST_PING
		else:
			msg_cmd

# parse message
def fn_msg_parser(in_msg):
	msg_list = in_msg.split()
	
