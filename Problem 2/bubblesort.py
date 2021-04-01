"""
bubblesort.py
implementation and analysis of bubble sort algorithm, meant to partially answer the
following question:
	Implement, numerically test, and explain two different sorting
    algorithms with different O() behaviors on randomly chosen
    lists of numbers with various sizes n. Use two different
    programming languages and coding styles. Show graphically
    that the expecected performance is consistent with your
    numerical experiments.

the bubble sort algorithm is defined as follows:

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list.

from Bubble Sort, Wikipedia. https://en.wikipedia.org/wiki/Bubble_sort

I also consulted notes I took during the algorithms class when writing the code that
measures the time it takes for the sort to run.

Nick Creel - Apr 11, 2020 - MIT License.
"""
import numpy as np
from numpy import *
from random import randint
import time
import matplotlib.pyplot as plt

def generateNLenList(n):
	"""
	this function takes an integer as input and returns a list of randomly
	generated numbers where the length of the list is equal to the value of the integer
	passed as an argument.

	>>> myList = generateNLenList(10)
	>>> len(myList)
	10

	"""
	randList = []
	for i in range(n):
		randList.append(randint(0,1000)) # large range more likely to be unsorted
	return randList

def makeLists(n, m):
	"""
	this function takes two integers, n and m, as input and returns a list of lists.
	n is the number of values in each individual list, and m is the number of lists
	nested within the larger list.

	>>> myLists = makeLists(3,5)
	>>> len(myLists)
	5
	>>> len(myLists[0])
	3
	"""
	listsList = []
	for i in range(0, m):
		listsList.append(generateNLenList(n))
	return listsList

def bubbleSort(intList):
	"""
	this function takes a list of integers as input and returns a tuple
	where the first element of the tuple is the list sorted from least to
	greatest, and the second element of the list is the runtime from start
	to end in seconds.

	>>> myList = [3,2,1]
	>>> bubbleSort(myList)[0]
	[1, 2, 3]
	"""
	startTime = time.time()
	isSorted = False
	sortedList = intList
	while isSorted == False:
		swap = False # if we go through the whole list with no swaps,
					 # then the list is sorted.
		for i in range(0, len(sortedList)-1):
			if sortedList[i] > sortedList[i+1]:
				swap = True
				temp = sortedList[i]
				sortedList[i] = sortedList[i+1]
				sortedList[i+1] = temp # now sortedList[i] < sortedList[i+1]
			else:
				continue
		if swap == False:
			isSorted = True
	endTime = time.time()
	runtime = endTime - startTime
	return (sortedList, runtime)

def main():
	runtimes = []
	# make a lot of lists of various lengths!
	list10s = makeLists(10,10)
	list30s = makeLists(30,10)
	list100s = makeLists(100,10)
	list300s = makeLists(300,10)
	list1000s = makeLists(1000,10)
	list3000s = makeLists(3000, 10)
	list10000s = makeLists(10000,10)
	list30000s = makeLists(30000,10)

	allLists = [list10s, list30s, list100s, list300s, list1000s, list3000s,
				list10000s, list30000s]

	sizes=[10,30,100,300,1000,3000,10000,30000]
	count=0
	for lists in allLists:
		runtime = []
		for aList in lists:
			runtime.append(bubbleSort(aList)[1])
		runtimes.append((sizes[count], runtime))
		count += 1

# 	!!!
#		I decided to move this to the .ipynb for this code so that the graph could be
#		modified without having to run the bubble sort unnecessarily.
#		but keeping the code here just in case.
#   !!!
# 	points_x = []
# 	points_y = []
# 	x = np.linspace(0,30000,200)
# 	y = x
# 	for runs in runtimes:
# 		for aRun in runs[1]:
# 			points_x.append(runs[0])
# 			points_y.append(aRun)
# 	print(points_x, '\n', points_y)
# 	figure = plt.figure(dpi=220, figsize=(3,2))
# 	axis = figure.add_subplot(111)
# 	axis.set(xlabel = "number of elements in list", ylabel = "runtime(s)",
# 			 title="Bubble Sort (Python3)")
# 	axis.plot(points_x, points_y, marker = ".", color = "red", linestyle = "none")
#
# 	plt.xscale("log") # log scale is more appropriate here
# 	plt.yscale("log")
#
# 	calculate best fit line
# 	in the worst case scenario, the bubble sort would have to swap an element n-1
# 	times to sort it to the right position. for example, in a reverse sorted list,
# 	the first value would have to be swapped with every value after it until it's
# 	swapped with the final element. In addition to swapping, the list must be traversed
# 	at least n times so that each element may be visited and swapped with the next.
# 	According to wikipedia, the bubble sort has a time complexity of O(n**2), which
# 	makes sense given the amount of times the list would have to be traversed in the
# 	worst case scenario
#
# 	fit_x = linspace(10, 30000)
# 	fit_y = (fit_x)**2
# 	axis.plot(fit_x, fit_y, color="green")
#
# 	plt.show()

main()

if __name__ == "__main__":
	import doctest
	doctest.testmod()
