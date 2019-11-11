# 3.3.3.3. Savings Exercise
# savings.py

principle = float(input('Please enter your principle: '))
annual_int = float(input('Please enter the annual interest: '))
target = float(input('How much you like to have in the end: '))

# suppose that the user always input the right data
i = 0
compound = principle * (1.00 + annual_int)**i

while compound < target:
	compound = principle * (1.00 + annual_int)**i
	i += 1
	final = str(compound).format('6.2f')
	print(final)

# or the last two lines:
	print(round(compound, 2))


# -----------------
principle = float(input('Please enter your principle: ')) #improve so that enter-erro-proof
annual_int = float(input('Please enter the annual interest: ')) #improve so that erro-proof
target = float(input('How much you like to have in the end: ')) #improve so that erro-proof

# suppose that the user always input the right data
i = 0
compound = principle * (1 + annual_int)**i

while compound < target:
	compound = principle * (1 + annual_int)**i
	i += 1
	final = '%.2r' % compound # 'f', NOT 'r'
	print(final) #!IMPORTANT

# -------------------

principle = float(input('Please enter your principle: ')) #improve so that enter-erro-proof
annual_int = float(input('Please enter the annual interest: ')) #improve so that erro-proof
target = float(input('How much you like to have in the end: ')) #improve so that erro-proof

# suppose that the user always input the right data
i = 0
compound = principle * (1 + annual_int)**i

while compound < target:
	compound = principle * (1 + annual_int)**i
	i += 1
	print('%.2f' % compound) #!IMPORTANT