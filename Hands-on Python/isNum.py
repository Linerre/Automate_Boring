# 3.1.8.2. Is Number String Exercise
# isNumberString.py

def isNum(): # clearly this function can't deal with float numbers
	testString = input('Please enter a number: ') # what if I enter -3.5? False!
	if testString.startswith('-'):
		newString = testString[1:]
		print(newString.isdigit())
	else:
		print(testString.isdigit())

for i in range(3):
	isNum()

# An alternative approach:
def ISNum():
	userString = input('Please enter a number: ')
	if userString.count('-') == 0:
		newString = userString.replace('-', '', 1)
		print(newString.isdigit())
	else:
		print(userString.isdigit())

for i in range(3):
	isNum()

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

for i in range(3):
	isDecimalStr()