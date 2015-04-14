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
		
	'''Checks to see if page is in physical M, if not will call function
	which simulates a page fault.'''
	def accessMem(self, process, pageNum):
		memAccess = (process, pageNum)
		if memAccess not in self.physM:
			self.pageFaults+=1
			print("Page Fault# ",self.pageFaults, " placed on page ",self.miss(memAccess))
		else:
			foundOn = self.hit(memAccess)
			print(memAccess, " already in M on page: ", foundOn)

	
	'''Refreshes page access time, moving to end of physM data structure
	also will return page in physical M where the page is located'''
	def hit(self, access):
		try:
			page = self.physM[access]
			self.physM[access] = page
			return page
		except KeyError:
			return -1
	
	'''Returns the vicitm that was selected if physical M is full, or 
	will return the page the item was placed on. Calls function to 
	update the PCB.'''
	def miss(self, access):
		try:
			page = self.physM.pop(access)
		except KeyError:
			if(len(self.physM)) >= (self.numPages):
				victim = self.physM.popitem(last=False)[1]
				self.physM[access] = victim
				self.updatePCB(access)
				return victim
			else:
				currPage = len(self.physM)
				self.physM[access] = currPage
				self.updatePCB(access)
				return currPage
				
	#Creates/updates the PCB as needed, manages processes' page tables
	def updatePCB(access):
		#needs to identify the process and update its page table/PCB
		#as needed, not sure how/why to do this really.
	
