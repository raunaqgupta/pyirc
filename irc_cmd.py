
from glob_const import *

# all the callable irc commands

def cmd_nick(user_info):
	msg = CONST_NICK + CONST_SPACE + user_info['nick'] + CONST_CRLF
	return msg

def cmd_user(user_info):
	msg = CONST_USER + CONST_SPACE + user_info['username'] + CONST_SPACE + user_info['hostname'] + CONST_SPACE + user_info['servername'] + CONST_SPACE + CONST_COLON + user_info['realname'] + CONST_CRLF
	return msg

def cmd_join(chan_name):
	msg = CONST_JOIN + CONST_SPACE + chan_name + CONST_CRLF
	return msg
	
def cmd_pong(server):
	msg = CONST_PONG + CONST_SPACE + server + CONST_CRLF
	return msg

def cmd_part(chan_name):
	msg = CONST_PART + CONST_SPACE + chan_name + CONST_CRLF
	return msg

def cmd_quit():
	msg = CONST_QUIT + CONST_CRLF
	return msg

def cmd_privmsg(recv_name, data):
	msg = CONST_PRIVMSG + CONST_SPACE + recv_name + ' :' + data + CONST_CRLF
	print 'MSG: ' + msg
	return msg
