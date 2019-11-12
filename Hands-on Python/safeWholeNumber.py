# 3.3.3.2. Safe Number Input Exercise
# a

def safeWholeNumber():
	user_whole = input('Please enter a whole number: ')

	if user_whole.startswith('-'):
		new_user_whole = user_whole[1:]
		while new_user_whole.isdigit():
			print('Great!', user_whole, ' is a whole number!')
			print()
			user_whole = input('Enter another one or press enter to quit: ')

	elif user_whole.isdigit():
		while user_whole.isdigit():
			print('Great!', user_whole, ' is a whole number!')
			print()
			user_whole = input('Enter another one or press enter to quit: ')

	else:
		print('Oops', user_whole, ' is not a whole number.') # this merges both illegal num and quit command
		user_whole = input('Pleanse try again: ')
		while not user_whole.isdigit():
			print('Oops', user_whole, 'is not a whole number.')
			user_whole = input('Pleanse try again: ')

# ----------

safeWholeNumber()

'''
Please enter a whole number: -12345
Great! -12345 is a whole number!


Enter another one or press enter to quit: 12345
Great! 12345 is a whole number!


Enter another one or press enter to quit: 123a
Great! 123a is a whole number!


Enter another one or press enter to quit: 
Great!  is a whole number!
'''

Enter another one or press enter to quit: ---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
~/anaconda3/lib/python3.6/site-packages/ipykernel/kernelbase.py in _input_request(self, prompt, ident, parent, password)
    728             try:
--> 729                 ident, reply = self.session.recv(self.stdin_socket, 0)
    730             except Exception:

~/anaconda3/lib/python3.6/site-packages/jupyter_client/session.py in recv(self, socket, mode, content, copy)
    802         try:
--> 803             msg_list = socket.recv_multipart(mode, copy=copy)
    804         except zmq.ZMQError as e:

~/anaconda3/lib/python3.6/site-packages/zmq/sugar/socket.py in recv_multipart(self, flags, copy, track)
    465         """
	466         parts = [self.recv(flags, copy=copy, track=track)]
    467         # have first part already, only loop while more to receive

zmq/backend/cython/socket.pyx in zmq.backend.cython.socket.Socket.recv()

zmq/backend/cython/socket.pyx in zmq.backend.cython.socket.Socket.recv()

zmq/backend/cython/socket.pyx in zmq.backend.cython.socket._recv_copy()

~/anaconda3/lib/python3.6/site-packages/zmq/backend/cython/checkrc.pxd in zmq.backend.cython.checkrc._check_rc()

KeyboardInterrupt: 

During handling of the above exception, another exception occurred:

KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-217-1a9836581275> in <module>()
----> 1 safeWholeNumber()

<ipython-input-216-2fc47c9d0521> in safeWholeNumber()
      7                         print('Great!', user_whole, 'is a whole number!')
      8                         print()
----> 9                         user_whole = input('Enter another one or press enter to quit: ')
     10 
     11         elif user_whole.isdigit():

~/anaconda3/lib/python3.6/site-packages/ipykernel/kernelbase.py in raw_input(self, prompt)
    702             self._parent_ident,
    703             self._parent_header,
--> 704             password=False,
    705         )
    706 

~/anaconda3/lib/python3.6/site-packages/ipykernel/kernelbase.py in _input_request(self, prompt, ident, parent, password)
    732             except KeyboardInterrupt:
    733                 # re-raise KeyboardInterrupt, to truncate traceback
--> 734                 raise KeyboardInterrupt
    735             else:
    736                 break

KeyboardInterrupt: 
"""

# -----------------------------------------------------------
def safeWholeNumber():
	user_whole = input('Please enter a whole number: ')

	if user_whole.startswith('-'):
		new_user_whole = user_whole[1:]
		while new_user_whole.isdigit():
			print('Great!', user_whole, 'is a whole number!')
			print()
			user_whole = input('Enter another one or press space to quit: ')

	elif user_whole.isdigit():
			print('Great!', user_whole, 'is a whole number!') #maybe the indentation here is wrong
			print()
			user_whole = input('Enter another one or press space to quit: ')

	elif user_whole == ' ':
		print('See you next time!')

	else:
		print('Oops', user_whole, 'is not a whole number.')
		user_whole = input('Pleanse try again: ')

# The above only loop once
# --------

def safeWholeNumber():
    user_whole = input('Please enter a whole number: ')

    while user_whole != '' and not user_whole.isdigit():
        if user_whole.startswith('-') and user_whole[1:].isdigit():
            print('Great!', user_whole, 'is a whole number.')
            user_whole = input('Enter another one or press enter to quit: ')
        else:
            print('Oops!', user_whole, 'is NOT a whole number')
            user_whole = input('Please try again: ')

    while user_whole.isdigit():
        print('Great!', user_whole, 'is a whole number!')
        user_whole = input('Enter another one or press enter to quit: ')

    if user_whole == '':
        print('See you next time!')

# -------------------------------------

def safeWholeNumbertest():
	user_whole = input('Please enter a whole number: ')
	while not user_whole[1:].isdigit():
		print('Oops!', user_whole, 'is not a whole number.')
		user_whole = input('Please try again: ')

	while user_whole[1:].isdigit():
		if user_whole.startswith('-'):
			print('Great!', user_whole, 'is a whole number.')
			user_whole = input('Enter another one or press enter to quit: ')
		else:
			print('Great!', user_whole, 'is a whole number.')
			user_whole = input('Enter another one or press enter to quit: ')

	if user_whole == '':
		print('Thanks! See you! ^_^')

safeWholeNumbertest()



