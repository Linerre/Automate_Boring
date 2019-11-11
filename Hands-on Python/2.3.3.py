dic = {'Girl-one': 'Yvonne', 'Girl-two': 'Elsie', 'Girl-three': 'Lulu'}

type(dic)

print('I know three girls. They are {Girl-one}, {Girl-two}, and {Girl-three}.'.format(**dic))
# result: I know three girls. They are Yvonne, Elsie, and Lulu.

# 2.3.3.1. Substring Locations Exercise
def printLocations(a, b):
	indexList = list()
	adjuster = 0
	repetitions = a.count(b)
	for i in range(repetitions):
		index = a.find(b, adjuster)
		indexList.append(index)
		adjuster = index + 1
	print(indexList)


'''suppose:
	              01234567890123
		string = 'This is a dish'
		substring = 'is'
		print the index'''

# need a loop initialization
		'''index1 = string.find('is', 0) + 1
		indexList.append(index1)
		index2 = string.find('is', index1)
		indexList.append(index2)
		print(indexList)
		'''

