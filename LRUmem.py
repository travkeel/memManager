from datetime import datetime
import collections
import json
from pprint import pprint

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
		for i in range(self.numPages):
			self.physM["Empty page:"+str(i)] = i
		
		#dictionary of page tables
		self.PCBs = {}
		
	'''Checks to see if page is in physical M, if not will call function
	which simulates a page fault.'''
	def accessMem(self, process, pageNum):
		
		memAccess = str((process, pageNum))
		
		if memAccess not in self.physM:
			self.pageFaults+=1
			print 'Page Fault#: ' + str(self.pageFaults)
			page = self.miss(memAccess)
			print str(memAccess)+ " placed on page "+str(page)
			self.updatePCB(process, pageNum, page)
			choice = raw_input("Press 'M' to see physical M, 'P' for page Tables, Enter to skip to next fault\n")
			self.showM(choice)
		else:
			foundOn = self.hit(memAccess)
			print str(memAccess)+ " already in M on page "+str(foundOn)
	
		return self.physM
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
				victim = self.physM.popitem(last=False)
				print "Replaced entry: "+str(victim[0])
				self.physM[access] = victim[1]
				return victim[1]
			else:
				print "No victim"
				currPage = len(self.physM)
				self.physM[access] = currPage
				return currPage
				
	#Creates/updates the PCB as needed, manages processes' page tables
	def updatePCB(self, process, pageNum, memPage):
		#adds page table for process if one doesn't exist
		if process not in self.PCBs.keys():
			self.PCBs[process] = []
		
		self.PCBs[process].append((pageNum, memPage))
		
		#removes old entry from page table if there was one
		for pageTable in self.PCBs.values():
			for pair in pageTable:
				if pair[1] == memPage and self.PCBs[process]!= pageTable:
					pageTable.remove(pair)
					
	#Prints various parts of M depending on user input
	def showM(self, choice):
		if choice == 'M':
			print '\n\n (procNum, pageNum), Physical page'
			print(json.dumps(self.physM,indent=4))
		elif choice == 'P':
			print "\n\n [Process: (procPage, physicalPage)]"
			pprint(self.PCBs)
			
		print '****************\n\n'
