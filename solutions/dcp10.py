'''
#10 [Medium]

asked by Apple


Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

'''


import threading
from datetime import datetime
import time

threadCount = 0

def scheduler(f,n):
	global threadCount
	while True:
		t = threading.Thread(target = f)
		t.start()
		time.sleep(n/1000)
		threadCount+=1


def job():
	id = threadCount
	print()
	print("Job instance #"+str(id)+" started at",datetime.now())
	time.sleep(10)
	print()
	print("Job instance #"+str(id)+" ended at",datetime.now())



if __name__ == "__main__":
	scheduler(job,5000)