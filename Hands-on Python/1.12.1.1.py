# 1.12.1.1. Number Dictionary Exercise
def numDictadding():
	numDict = dict()
	numDict['one'] = 1
	numDict['two'] = 2
	numDict['three'] = 3
	numDict['four'] = 4
	numDict['five'] = 5
	numDict['six'] = 6
	return numDict

def test():
	thedict = numDictadding # Here, it should be equal to the function! Brakets missing!
	print(int(thedict['one']) + int(thedict['six']))

test()

# The above code will get an error:
'''
TypeError                                 Traceback (most recent call last)
<ipython-input-5-b756e06c69af> in <module>()
     13         print(int(thedict['one']) + int(thedict['six']))
     14 
---> 15 test()

<ipython-input-5-b756e06c69af> in test()
     11 def test():
     12         thedict = numDictadding
---> 13         print(int(thedict['one']) + int(thedict['six']))
     14 
     15 test()

TypeError: 'function' object is not subscriptable

'''
# line 13 above should be:
thedict = numDictadding() # pay attention to the brackets