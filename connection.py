
import socket
import re
from threading import Lock

from glob_const import *

import logging

# connection class
class connection:
	
	def __init__(self, server_info):
		
		
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Initialize")
		
		self._server_info = server_info
		self._server_addr = self._server_info['address']
		try:
			self._server_port = int(self._server_info['port'])
		except ValueError:
			self.logger.critical("Error in connection initialization")
			return -1
		
		self._lock = Lock()
		self._sock = 0
	
	def socket_recv(self):
		self._lock.acquire()
		try:
			recv_data = self._sock.recv(4096)
			while(recv_data.endswith(CONST_CRLF) != True):
				recv_data = recv_data + self._sock.recv(4096)
			
			self.logger.debug(recv_data)
			# data_list = recv_data.split()
			# self.logger.debug(data_list)
			return recv_data
		finally:
			self._lock.release()
		
	
	def socket_send(self, data):
		data_length = len(data)
		bytes_sent = 0

		while bytes_sent < data_length:
			data = data[bytes_sent:]
			data_length = len(data)
			bytes_sent = self._sock.send(data)

	def connect_server(self):
		self._sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self._sock.connect( (self._server_addr, self._server_port) )
	
	def disconnect_server(self):
		self._sock.close()
