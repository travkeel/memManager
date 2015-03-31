from datetime import datetime

#class which will act as the PCB for each process
class PCB(object):
	def __init__(self, procNum):
		self.procNum = procNum
		self.space = space
		
		#using timestamps to determine LRU as of now
		#might want to switch to logical timestamp
		self.timestamp = datetime.now()
		
		self.pageTable = {}

#Simulate memory that will use a LRU page replacement algorithm, also
#contains a list of page tables.		
class LRUmem(object):
	def __init__(self, space):
		self.space = space
		
		#list to simulate pages of virtual memory
		self.memPages = []
		
		#list of dictionaries, each dictionary will be a process table
		self.pageTables = []
	
	
		
