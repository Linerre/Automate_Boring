# 1.13.8.2. Play Computer Error Exercise
def product (num):
    prod = 1 #Initializor should be outside the loop!
    for n in [5, 4, 6]:
        prod = prod*n
    return prod
product([5, 4, 6])

# 1.14.3.1. Floating Point Exercise
def discount(x, y):
	z = (1 - y/100)*x
	print(format(z, '.2f'))
	

print('Welcome! Please enter the price: $__')
x = float(input('>'))
# Here use 'if' funtion to judge if it is a number
print()
print('Please enter the discount: ')
y = int(input('>'))
print('Great! Your just need to pay: $', end='')
discount(x, y)

print('Hope you enjoy the product!')

# -----------------------------------------------

# The following code doesn't work as expected:
def discount(x, y):
	z = (1 - y/100)*x
	format(z, '.2f')
	print(float(z)) # Here we got a problem

print('Welcome! Please enter the price: $__')
x = float(input('>'))
# Here use 'if' funtion to judge if it is a number 
print()
print('Please enter the discount: ')
y = int(input('>'))
print('Great! Your just need to pay: $', end='')
discount(x, y)

print('Hope you enjoy the product!') 

# ------------------------------------------------

# 2.1.6.1. Underscore Exercise

print('Please enter the words you wanna say: ')

x = str(input('>'))
print('Please double check every single word in what you\'ve said')
y = x.split()
print(y)

print('We have Underscored your words ^_^ :')
'_'.join(y)

# 2.1.6.2. Acronym Exercise
def acronymize(word):
	n = 0
	for word in singlewords:
		capital = singlewords[n]
		firstletter = capital[0]
		letters.append(firstletter)
		n = n + 1
	acronym = ''.join(letters)
	print(acronym)

print('Please enter the words/phrase: ')
user_data = str(input('>'))
uppercase = user_data.upper()
singlewords = uppercase.split()
letters = []
print('The corresponding ancronym is: ')
acronymize(user_data)













