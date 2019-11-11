# 3.3.3.4. Strange Sequence Exercise
# jumpSeq.py

print('Hi there! Let\'s play a game.')

def jumpSeq(n):
	while n != 1:
		if n % 2 == 0:
			n = n//2
		else:
			n = n * 3 + 1
	return n


# jumSeqLengths.py

def jumpSeq(n):
	listJumps = list()
	listJumps.append(n)
	while n != 1:
		if n % 2 == 0:
			n = n//2
			listJumps.append(n)
		else:
			n = n * 3 + 1
			listJumps.append(n)
	# return listJumps
	print('Starting from {}, jump sequence length {}.'.format(listJumps[0], len(listJumps)))
	# print(len(listJumps)) # this will not work since 'return' means the end of the function

def main():
	lowest_n = int(input('Enter lowest start: '))
	highest_n = int(input('Enter hightest start: '))
	for n in range(lowest_n, highest_n+1):
		jumpSeq(n)

