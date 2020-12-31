from os import system, name
import requests
import itertools
import threading
import time
import sys

#color

def default(text):
		return '\033[0m'+str(text)
		
def fail(text):
		print('\033[91m'+str(text))
	
def blue(text):
		print('\033[94m'+str(text))
		
def success(text):
		print('\033[92m'+str(text))
		
def warning(text):
		print('\033[93m'+str(text))


def clear():
	if(name == "nt"):
		return system('cls')
	else:
		return system('clear')
		
	
#animasi loading
def connect(url):
	for c in itertools.cycle(['|', '/', '-', '\\']):
		try :
			req = requests.get(url)
			return req.status_code
			break
		except:
			pass
		sys.stdout.write('\r'+c)
		sys.stdout.flush()
		time.sleep(0.1)
		#sys.stdout.write('\rDone!	')
