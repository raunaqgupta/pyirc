from threading import Thread, Lock
 
class Response:
 
    def __init__(self):
        self.filestream = open('dummy.txt', 'w');
        self._lock = Lock()
   
    def resp_function(self, data):
        self._lock.acquire()
        try:
            str_data = str(data)
            self.filestream.write(str_data)
        finally:
            self._lock.release()

def foo1(resp, data):
	resp.resp_function(data)

def foo2(resp,data):
	data2 = data.upper()
	resp.resp_function(data2)

resp = Response()
thread1 = Thread(target=foo1, args=(resp,"hello\n"))
thread2 = Thread(target=foo2, args=(resp,"new world!\n"))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
