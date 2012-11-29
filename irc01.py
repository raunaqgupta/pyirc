#!/usr/bin/env python

from os import path
from threading import Thread

from glob_const import *
import numeric_resp
import module
import config
import connection
import irc_cmd
import msgparser

import logging
import argparse

def main(args):
	
	# initialize logging
	if args.log != 'OFF':
		
		numeric_level = getattr(logging, args.log.upper())
		if not isinstance(numeric_level, int):
			numeric_level = getattr(logging, "INFO")
			raise ValueError("Invalid log level: %s" % args.log)
		
		logging.basicConfig(filename="pyirc_log.log", level=numeric_level, filemode="w", format="%(asctime)s - %(module)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s")
	
	logger = logging.getLogger(__name__)
	logger.debug("Starting pyIRC")
	
	# get configuration information
	server_info = config_obj.get_server_info()
	bot_info = config_obj.get_bot_info()
	
	# load modules
	try:
		module_obj = module.module(path.abspath('modules'))
	except ValueError:
		logger.critical("Bad module path")
		return -1
	
	if(module_obj.load_module()):
		mod_dict = module_obj.get_module_dict()
	
	
	# create server socket
	server_obj = connection.connection(server_info)
	server_obj.connect_server()
	# method object created for module security
	sock_send = server_obj.socket_send
	
	# send nick and user commands
	sock_send(irc_cmd.cmd_nick(bot_info))
	sock_send(irc_cmd.cmd_user(bot_info))
	
	# connect to channels
	for channel_name in server_info['channels']:
		sock_send(irc_cmd.cmd_join(channel_name))
	
	# main execution loop
	while True:
		
		# incoming message
		in_msg = server_obj.socket_recv()
		
		# parse data
		msgparser_obj = msgparser.msgparser(in_msg)
		in_cmd = msgparser_obj.fn_get_cmd()
		
		# create threads, call modules
		for key in iter(mod_dict):
			logger.debug('KEY: ' + key)
			if key == 'ALL' or key == in_cmd:
				for registered_module in mod_dict[key]:
					
					logger.debug(registered_module)
					thread = Thread(target=registered_module.run_module, args=(in_msg, sock_send, bot_info))
					thread.start()
					thread.join()
				
	
	return 0

if __name__ == '__main__':
	
	argParser = argparse.ArgumentParser(description="A python based IRC bot.")
	argParser.add_argument('--log', default='OFF')
	main(argParser.parse_args())
