# The following code creates a file the write the specifies sentence into it
# The file will be created under a certain path which is not shown here

outfile = open('sample.txt', 'w') # the file name is a string!
outfile.write('Python is fantastic')
outfile.close()

# create another file and write two lines into it
outfFile = open('sample2.txt', 'w')
outFile.write('My second output file!')
outFile.write('Write some more.')
outFile = close()

# A revised version of the file above
outFile = open('sample.txt', 'w')
outFile.write('A revised output file!\n')
outFile.write('Write some more.\n')
outFile.close()

# To read file with Python
inFile = open('sample3.txt', 'r') #open an already exsiting file, 'r' is optional
contents = inFile.read()  # read the content and add the content as the value to a var
print(contents) # print the var

# 2.5.2.1 PrintUpper Exercise
# a - PrintUpper.py
outFile = open('sample2.txt', 'r')
contents = outFile.read()
PrintUpper = str(contents).upper()
print(PrintUpper)

# b fileUpper.py
print('Hi there, please enter a name for your txt file: ')
filename = input('>') + '.txt'
print('Great! Your file has been named as: ', filename)
print('Now, please type in a line you would like to add into your file: ')
userline = input('>')
print('Wonderful! The following is your line in uppercase: ')

userfile = open(filename, 'w')
content = userfile.write(userline)
uppercon = content.upper()
userfile.close()
print(uppercon)

# c copyFileUpper.py
print('Hi there, please enter a name for your file: ')
filename = input('>') + '.txt'
print('Great! Your file has been named as: ', filename)
print('Now, please type in a line you would like to add into your file: ')
userline = input('>')
newfilename = 'UPPER' + filename
print('Wonderful! Now you will get a new file named: ', newfilename)

newuserfile = open(newfilename, 'r')
content = userfile.read()
uppercon = content.upper()
print(uppercon)
