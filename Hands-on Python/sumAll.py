# 3.3.3.1. Interactive Sum Exercise
# sumAll.py

n = float(input('Please enter a non-zero number: '))
m = 0
while n != 0:
	sums = n + m # This is WRONG because the result will always be N + 0
				  # What we want is sums = New_n + the sum of Past_ns
	n = float(input('''Please enter another non-zero number, 
		or enter arabic zero to quit: '''))

print('The sum of all the your numbers is: ', end='')	
print(sums)


# ----   WRONG   -----
n = float(input('Please enter a non-zero number: '))
m = 0
while n != 0:
	n = n + m 
	n = float(input('''Please enter another non-zero number, 
		or enter arabic zero to quit: ''')) 
		# wrong, because the final value of n will be 0

print('The sum of all the your numbers is: ', end='')	
print(n)


# ----   WRONG  ------
n = float(input('Please enter a non-zero number: '))
m = 0
while n != 0: 	
	n = n + m # Still this will cause N always euqal N
	sums = n # Let the last but one value of N get passed to sums
	n = float(input('''Please enter another non-zero number, 
		or enter arabic zero to quit: ''')) 

print('The sum of all the your numbers is: ', end='')	
print(sums)


# -- CORRECT ONE ---
print('Please enter numbers.')
n = float(input('Please enter a number: '))
m = float(input('Next number or enter 0 to quit: '))
sums = m + n

while m != 0: 
	m = float(input('Next number or enter 0 to quit: '))
	sums = sums + m # after this line, since m != 0, the loop will start over again!


print('The sum of all your numbers is: ', end='')	
print(sums)


	
