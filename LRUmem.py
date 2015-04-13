from datetime import datetime
import collections

#class which will act as the PCB for each process
class PCB(object):
	def __init__(self, procNum):
		self.procNum = procNum
		self.space = self.space
		
		#using timestamps to determine LRU as of now
		#might want to switch to logical timestamp
		self.timestamp = datetime.now()
		
		self.pageTable = {}

#Simulate memory that will use a LRU page replacement algorithm, also
#contains a list of page tables.		
class LRUmem(object):
	def __init__(self, KBs, pageSize):
		self.space = KBs*1024
		self.numPages = self.space/(pageSize*1024)
		#list to simulate pages of virtual memory
		self.memPages = collections.OrderedDict()
		
		#list of dictionaries, each dictionary will be a process table
		self.pageTables = []
		
	
	#Should look at PCB for the process, create PCB if one does not exist
	def accessMem(self, process, pageNum):
		memAccess = (process, pageNum)
		if memAccess not in self.memPages:
			#
			(self.pageFault(memAccess))
		else:
			print(memAccess, " already in mem")
			#update timestamp for that page here
	
	#occurs when m access results in a page fault, checks for PCB, pageTable
	#and will update as needed
	def pageFault(self, access):
		if len(self.memPages) >= (self.numPages):
    		#add LRU replacement method here
			print("Memory currently full.")
		else:
			print("Adding ", access, " to mem")
			(self.updateMem(access))
			
	def updateMem(self, access):
		if access in (self.memPages):
			print("test")