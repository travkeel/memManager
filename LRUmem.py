from datetime import datetime
import collections

#class which will act as the PCB for each process
class PCB(object):
	def __init__(self, procNum):
		self.procNum = procNum
		self.space = self.space
		
		self.pageTable = {}

'''Sets up OrderedDict to keep least recently used item in front of the
object. Makes choosing a victim trivial.'''
class LRUm(collections.OrderedDict):
	
	def __setitem__(self, key, value):
		if key in self:
			del self[key]
		collections.OrderedDict.__setitem__(self, key, value)

'''Simulate memory that will use a LRU page replacement algorithm, also
contains a list of page tables.'''
class Memory(object):
	def __init__(self, KBs, pageSize):
		
		self.space = KBs*1024
		self.numPages = self.space/(pageSize*1024)
		self.pageFaults = 0
		#Uses LRUm class to keep LRU item in front of data structure
		self.physM = LRUm()
		
		#list of dictionaries, each dictionary will be a process table
		self.pageTables = []
		
	#Should look at PCB for the process, create PCB if one does not exist
	def accessMem(self, process, pageNum):
		memAccess = (process, pageNum)
		if memAccess not in self.physM:
			self.pageFaults+=1
			print("Page Fault#", self.pageFaults,
			" adding", memAccess, " to M")
			(self.miss(memAccess))
		else:
			foundOn = self.hit(memAccess)
			print(memAccess, " already in M on page: ", foundOn)

	
	#Returns page in physical M where request was found
	def hit(self, access):
		try:
			page = self.physM[access]
			self.physM[access] = page
			return page
		except KeyError:
			return -1
	
	#Will return page # in physical M where page is placed.
	def miss(self, access):
		try:
			page = self.physM.pop(access)
		except KeyError:
			if(len(self.physM)) >= (self.numPages):
				page = self.physM.popitem(last=False)[1]
				self.physM[access] = page
			else:
				self.physM[access] = len(self.physM)
	
