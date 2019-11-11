# safeDecimal.py

def safeDecimal():
	user_deci = input('Please enter a decimal: ')
	while user_deci.find('.') == -1: # wrong eg: fsfd, 123, -123, 123.5g
		print('Oops! {} is NOT a decimal.'.format(user_deci))
		user_deci = input('Please try again: ')

	while user_deci.find('.') != -1:
		dot = user_deci.find('.')
		new_user_deci = user_deci[:dot]+user_deci[dot+1:]
		if new_user_deci[1:].isdigit():
			print('Great! {} is a decimal'.format(user_deci))
			user_deci = input('Enter another one or press enter to quit: ')
		else:
			print('Oops! {} is NOT a decimal.'.format(user_deci))
			user_deci = input('Please try again: ')

	if user_deci == '':
		print('Thanks! See you next time ^_^') 

# --------- version 0.2 ----------

def safeDecimal():
	user_deci = input('Please enter a decimal: ')
	while user_deci.find('.') == -1: # wrong eg: fsfd, 123, -123, 123.5g
		print('Oops! {} is NOT a decimal.'.format(user_deci))
		user_deci = input('Please try again: ')

	while user_deci.find('.') != -1:
		dot = user_deci.find('.')
		new_user_deci = user_deci[:dot]+user_deci[dot+1:]

		if dot == 0 and user_deci[1:].isdigit():
			print('Great! {} is a decimal'.format(user_deci))
			user_deci = input('Enter another one or press enter to quit: ')

		elif new_user_deci[1:].isdigit():
			print('Great! {} is a decimal'.format(user_deci))
			user_deci = input('Enter another one or press enter to quit: ')
			
		else:
			print('Oops! {} is NOT a decimal.'.format(user_deci))
			user_deci = input('Please try again: ')

	if user_deci == '':
		print('Thanks! See you next time ^_^') 