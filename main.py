#!/usr/bin/python3
__author__ = "u/wontfixit"
__license__ = "GPL"
__version__ = "1.0.0"


import random
from datetime import datetime
prettytime = str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))		

def getMinMax(counter) -> tuple:
	'''This add the max and the min of a number given by the value
	ex: 
	1 = max 9 		min 1
	3 = max 999 	min 100
	5 = max 99999 	min 10000

	'''
	
	i=1
	j=1
	bigNumber=""
	smallNumber="1"
	while i <= counter:
		bigNumber=bigNumber+"9"
		i += 1

	while j <= counter-1:
		smallNumber=smallNumber+"0"
		j += 1

	return int(smallNumber),int(bigNumber)

def getExamples(first, second,counter,action=("x",":","+","-")):
	
	'''
	will retrun a .txt file with examples of Elementary arithmetic in it.
	
	
	
	getExamples(first, second,counter,action=("x",":","+","-"))
	
	first (int): count Digits of first Number
	second (int): count Digits of second Number
	counter (int): count of examples will produced
	action (list): Elementary arithmetic default: ("x",":","+","-")
	
	
	'''
	firstMinMax = getMinMax(first)
	secondMinMax = getMinMax(second)

	countertemp = counter

	text = ""
	for val in action:
		text = text	+"----------------    "+val+"    ----------------\n\r"
		while countertemp >= 1:
			
			RandFirst = random.randint(firstMinMax[0], firstMinMax[1])
			RandSecond = random.randint(secondMinMax[0], secondMinMax[1])
			
			if RandFirst > RandSecond:
				RandFirstTmp = RandFirst
				RandSecondTmp = RandSecond
			else:
				RandFirstTmp = RandSecond
				RandSecondTmp = RandFirst			
			
			if countertemp%5 == 1:
				text = text+str(RandFirstTmp)+" "+val+" "+str(RandSecondTmp)+"\n\r"
			else:
				text = text+str(RandFirstTmp)+" "+val+" "+str(RandSecondTmp)+"      "
			
			countertemp -=1	
		countertemp = counter

	text
	writeFile(text,first, second,counter)
	
def writeFile(k,first, second,counter):
	f = open(prettytime+"_fn-"+str(first)+"_sn-"+str(second)+"_ex-"+str(counter*4)+".txt", "a")
	f.write(k)
	f.close()


if __name__ == "__main__":
	
	getExamples(4,3,20)

