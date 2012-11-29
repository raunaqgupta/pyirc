
#todo: import global constants and user information
#from glob import constants, user_info
import glob_const

#class definition
class jerpeater:
	
	def __init__(self):
		print 'jerpeater module loaded'

	def func1(self):
		print "hello, world!"
	
	def get_irc_cmds(self):
		irc_cmds = ['PRIVMSG', 'NOTICE']
		return irc_cmds
	
	def run_module(self, msg, sock_send):
		if data.find( 'PRIVMSG' ) != -1:
				nick = data.split('!')[0].replace(':','')
				channel = data.split()[2]
				command = data.split()[1]
				message = ':'.join( data.split(':')[2:] )
		if nick != binfo['nick']:
			sock_send( CONST_PRIVMSG + CONST_SPACE + channel + ' :' + nick + ' said ' + message + CONST_CRLF )
			return 1
                return 0
	
# store class name in this variable
# what are the security risks in this?
Class = jerpeater
