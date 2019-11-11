# 3.1.8.2. Is Number String Exercise
# isNumberString.py

def isNum(): 
	'''
	input: any legal python number: -1.5, .5, 1., -4
	output: True or False depending on the input
	'''
	testString = input('Please enter a number: ') 
	if testString.startswith('-') or testString.find('.') != -1:
		newString = testString.replace('.', '').replace('-', '')
		print(newString.isdigit())
	else:
		print(testString.isdigit())

for i in range(4):
	isNum()

# the above function works fine and it is short
# which goes along with Python's phylosophy
# while the below code is rubbish, written by me around one year ago
# it acts as very typical bad example of Python code

# isDecimalStr.py

def isDecimalStr():
	testString = input('Please enter a number: ')
	if testString.startswith('-') and testString.find('.') != -1: # or '.' is in testString
		newString = testString[1:]
		decimal = newString.find('.') 
		finalString = newString[0:decimal]+newString[decimal+1:]
		# print(finalString)
		print('The number is a decimal:', finalString.isdigit())

	elif testString.find('.') != -1:
		decimal = testString.find('.')
		finalString = testString[1:decimal]+testString[decimal+1:]
		print('The number is a decimal:', finalString.isdigit())
		
	else:
		print('The number is a decimal:', testString.isdigit())

# for i in range(3):
# 	isDecimalStr()