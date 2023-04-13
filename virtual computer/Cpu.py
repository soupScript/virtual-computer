from gpu import *
from ram import *


def newprocess(linked, name):
	global processes
	global processlimit
	global processInCreation
	global processInCreation
	#create a new process with properties
	processInCreation.append(linked)
	processInCreation.append(name)
	finalcreation = [name, processInCreation[0]]
	###
	if processInCreation[0] < processlimit:
		processes.append(finalcreation)
		processInCreation.clear()

def emergencyCleanout():
	global processes
	processes.clear()


	
	
	





