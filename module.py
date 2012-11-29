
import os
import json

import logging

# load modules
class module:
	
	def __init__(self, module_path):
		
		self.logger = logging.getLogger(__name__)
		self.logger.info("Initializing")
		
		if(os.access(module_path, os.F_OK | os.R_OK)):
			self._module_path = module_path
			self._module_list = []
			self._module_name = []
			
		else:
			self.logger.critical("Bad path to modules")
			raise ValueError('Bad path to modules')
	
	# dynamic module loading
	def load_module(self):
		
		self.logger.info("Start")
		
		# read module.json
		active_modules = json.load(open('modules/modules.json'))['modules']
		self.logger.debug(active_modules)
		
		for filename in os.listdir(self._module_path):
			
			mod_name = filename[:-3]
			if(filename[-3:] == ".py" and filename != '__init__.py' and (mod_name in active_modules)):
				self.logger.debug(filename)
				self._module_name.append('modules.' + mod_name)
				self.logger.debug(self._module_name)

		# read about map function
		self._module_list = map(lambda x: __import__(x, fromlist='*'), self._module_name)
		
		self.logger.info("End")
		return 1
	
	## create dict for command-module mapping
	def get_module_dict(self):
		
		module_dict = {}
		
		# populate dict with keywords
		key_list = ['ALL', 'PRIVMSG', 'NOTICE', 'PART', 'JOIN', 'PING']
		
		# initialize module_dict
		for key in key_list:
			module_dict[key] = []
		
		for module in self._module_list:
			obj = module.Class()
			cmd_list = obj.get_irc_cmds()
			for cmd in cmd_list:
				if cmd in module_dict:
					module_dict[cmd].append(obj)
		
		self.logger.debug(module_dict)
		return module_dict
	
	# reload module
	# todo
		
