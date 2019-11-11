# 3.1.4.1. Graduate Exercise
# graduate.py
print('How many credit have you had obtained for now?')
credits = int(input('My credits in total is: '))

# if-else
if credits >= 120:
	print('Congrats! You have the enough credits for your degree!')
else:
	short = 120 - credits
	print('Oops! You still need', short, 'credits if you want to graduate from the university')

# 3.1.4.2. Head or Tails Exercise
# eadstails.py
import random

# if-else:
def flip():
	x = random.randrange(2)
	if x == 0:
		print('Heads')
	else:
		print('Tails')

def main():
	for i in range(10):
		flip()

main()

# The following code does not work as expected:
# ------------------------------------------
import random
x = int(random.randrange(0, 2, 1)) 

# if-else:
def flip(x): # x is unnecessary
	if x == 0:
		print('Heads')
	else:
		print('Tails')

def main():
	for x in range(20): # here i should be used instead of x
		flip(x)

main()
Heads
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails

import random
x = random.randrange(2) # should be changed into local type

# if-else:
def flip(x):
	if x == 0:
		print('Heads') # if you are going to use a local var and its value is 
	else:              # automatically assigned, then no need to declare it in the function name
		print('Tails')

def main():
	for x in range(10):
		flip(x)

main()
Heads
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
Tails
# --------------------------------------------


# 3.1.4.3. Strange Function Exercise
# jumpFuncStub.py --> jumpFunc.py

# 3.1.5.1. Sign Exercise


def judge(x):
	print('Please enter a random number: ', end='')
	x = float(input('>'))
	if x == 0:
		print('zero')
	elif x < 0:
		print('negative')
	else:
		print('positive')
		print()

for i in range(3):
	judge(x)

# 3.1.5.2. Grade Exercise
# wages2.py

def calcWeeklyWages(totalHours, hourlyWage):
	'''eturn the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''
	if totalHours <= 40:
		totalWages = hourlyWage * totalHours
	elif totalHours <= 60:
		totalWages = (totalHours - 40) * hourlyWage * 1.5 + 40 * hourlyWage
	else:
		totalWages = (totalHours - 60) * hourlyWage * 2 + 30 * hourlyWage + 40 * hourlyWage
	return totalWages

def main():
	hours = float(input('Enter hours worked: '))
	wage = float (input('Enter dollars paid per hour: '))
	total = calcWeeklyWages(hours, wage)
	print('Wages for {hours} hours at ${wage: 6.2f} per hour are ${total: 6.2f}.'
		.format(**locals())) # learn this style

for i in range(3):
	main()



# 3.1.6.1. Short String Exercise
# short.py
sList1 = ['just',
 'three',
 'days',
 'after',
 'she',
 'pulled',
 'a',
 'vote',
 'on',
 'the',
 'Brexit',
 'deal',
 'in',
 'Parliament',
 'and',
 'only',
 'a',
 'day',
 'after',
 'she',
 'won',
 'a',
 'tight',
 'confidence',
 'vote',
 'in',
 'her',
 'party']

def printShort(strings):
	'''Given a list of strings,
	print the ones with at most three characters.
	>>> printShort(['a', 'long', one'])
	a
	one
	'''
	for s in strings:
		if len(s) <= 3:
			print(s)

printShort(sList1)

# 3.1.6.2. Even Print Exercise
# even1.py

def printEven(nums):
	'''Given a list of integers nums, 
	print the even ones.

	>>> printEven([4, 1, 3, 2, 7])
	4
	2
	'''
	for num in nums:
		if num % 2 == 0:
			print(num)

# figure out why the result is None
import random
nums = []
for i in range(5):
	num = int(random.randrange(0, 10, 1))
	newnums = nums.append(num)
print(newnums)

for n in range(4):
	 printEven(newnums)
# --------------------------------

# 3.1.6.3. Even List Exercise
# even2.py

def chooseEven(nums):
	'''Given a list of integers, nums, 
	return a list containing only the even ones.

	>>> chooseEven([4, 1, 3, 2, 7])
	[4, 2]
	'''
	newnums = []
	for num in nums:
		if num % 2 == 0:
			newnums.append(num)
	return newnums

# 3.1.6.4. Unique List Exercise
# ---------------------------------------------------
''' 
The madlib2.py
Interactive display of a mad lib, which is provided as a Python format string,
with all the cues being dictionary formats, in the form {cue}.

In this version, the cues are extracted from the story automatically,
and the user is prompted for the replacements.

Original version adapted from code of Kirby Urner
'''

def getKeys(formatString):
	'''fromatingString is a format string with embedded dictionary keys.
	Return a set containing all the keys from the format string.'''

	keyList = list()
	end = 0
	repetitions = formatString.count('{')
	for i in range(repetitions):
		start = formatString.find('{', end) + 1 # pass the '{'
		end = formatString.find('}', start)
		key = formatString[start : end]
		if key not in keyList:
			keyList.append(key) # may add duplicates

	return keyList #removes duplicates: no duplicates in a set


def addPick(cue, dictionary): # from madlibDicty.py
	'''Prompt for a user repsonse useing the cue string,
	and place the cue-response pair in the dictionary.
	'''

	promptFormat = 'Enter a specific example for {name}: '
	prompt = promptFormat.format(name = cue)
	response = input(prompt)
	dictionary[cue] = response

def getUserPicks(cues):
	'''Loop through the collection of cue keys and get user choices.
	Return the resulting dictionry.
	'''

	userPicks = dict()
	for cue in cues:
		addPick(cue, userPicks)
	return userPicks

def tellStory(storyFormat):
	'''stroyFromat is a string with Python dictionary refereces embedded,
	in the form {cue}. Prompt the user for the mad lib substituions
	and then print the resulting story with the substitutions.
	'''
	cues = getKeys(storyFormat) # cues = ['animal', 'food', 'city']
	userPicks = getUserPicks(cues) 
	story = storyFormat.format(**userPicks)
	print(story)

def main():
	originalStoryFormat = '''
Once upon a time, deep in an ancient jungle,
there lived a {animal}.  This {animal}
liked to eat {food}, but the jungle had
very little {food} to offer.  One day, an
explorer found the {animal} and discovered
it liked {food}.  The explorer took the
{animal} back to {city}, where it could
eat as much {food} as it wanted.  However,
the {animal} became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of {food}.

The End
'''
	tellStory(originalStoryFormat)
	input('Press Enter to end the program.')

main()

# ---------------------------------------------------

def getKeys(formatString):
	'''fromatingString is a format string with embedded dictionary keys.
	Return a set containing all the keys from the format string.'''

	keyList = list()
	end = 0
	repetitions = formatString.count('{')
	for i in range(repetitions):
		start = formatString.find('{', end) + 1 # pass the '{'
		end = formatString.find('}', start)
		key = formatString[start : end]
		keyList.append(key) # may add duplicates

def uniqueList(aList):
	'''Return a new List that includes the first occurrence of each value
	in aList, and omits later repeats. The returned List should include
	the first occurrences of values in aList in their original order

	>>> vals = ['cat', 'dog', 'cat', 'bug', 'dog', 'dog', 'ant', 'dog', 'bug']
	>>> uniqueList(vals)
	['cat', 'dog', 'bug', 'ant']
	'''
	nList = list()
	for ele in aList:
		if ele not in nList: # no need to judge if its value is True or False
			nList.append(ele)
	return nList

	# 3.1.7.1. Congress Exercise
	# congress.py
def eligible():
	name = input('Enter your name: ')
	age = int(input('Enter your age '))
	UScitizenship = int(input('Enter the year of your citizenship: '))

	if age >= 30 and UScitizenship >= 9:
		print('Congrats!', name, 'You are eligible for both the House and Senate.')
	elif age >= 25 and UScitizenship >= 7:
		print(name, 'You eligible only for the House.')
	else:
		print('Sorry', name, 'You are ineligible for Congress.')

for i in range(3):
	eligible()



