import sys

def parseData(data):
	for line in data:
		#Strips newline character from each line, then each line is
		#split into a list.
		mAccess = line.rstrip().split()
		
		#Prints out process and page it is accessing. 
		#TODO: do I need this?
		print "Process "+mAccess[0].rstrip(':')+\
		" is accessing page "+str(int(mAccess[1], 2))
	

def main():
	#Takes input file from command line
	with open(sys.argv[-1], 'r') as f:
		mRefs = f.readlines()
		parseData(mRefs)

if __name__ == "__main__":
	main()