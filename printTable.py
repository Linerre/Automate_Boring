# Practice Project
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(aList):
    '''Return the printed table of the list in
    a tidy way:
    >>> aList = [[A, D], [B, E], [C, F]]
    >>> printTable(aList)
    >>> A B C
        D E F
    '''
    repetition = len(aList) # set loop times
    widths = [[],[],[]]
    col_widths = []

    for i in range(repetition):
         for item in aList[i]: #already reach to each word in the list inside alist
             widths[i].append(len(item))
         col_widths.append(max(widths[i]))
         # if not a new blck, the loop will simply return every len() value

    n = 0
    for word_0, word_1, word_2 in aList[n], aList[n+1], aList[n+2]:
            print(word_0.rjust(col_widths[n]), end='')
            print(word_1.rijust(col_widths[n]+col_widths[n+1]), end='')
            print(word_2.rjust(sum(col_widths)), end='')

    #return col_widths

    #return widths

# -------
def printTable(aList):
    '''Return the printed table of the list in
    a tidy way:
    >>> aList = [[A, D], [B, E], [C, F]]
    >>> printTable(aList)
    >>> A B C
        D E F
    '''
    repetition = len(aList) # loop times set
    widths = [[],[],[]]
    col_widths = []
    #n = 0   not need anymore
    for i in range(repetition):
         for item in aList[i]: #already reach to each word in the list inside alist
             widths[i].append(len(item))
         col_widths.append(max(widths[i]))
         # if not a new blck, the loop will simply return every len() value

    #for i in range(repetition): #loop times set
        #for word in aList[i]:
            #print(word.rjust(col_widths[i]))
    for i in range(len(aList[0])):
        print(aList[0][i].rjust(col_widths[0]),
              aList[1][i].rjust(col_widths[1]),
              aList[2][i].rjust(col_widths[2]),)

printTable(tableData)
  apples
 oranges
cherries
  banana
Alice
  Bob
Carol
David
 dogs
 cats
moose
goose

# ----------
y = [['1', '2', '3', 'a'], ['3', '5', '9', 'b'], ['80', '56', '34','c']]
x = [[], [], [], []]
m = 0
for i in range(4):
    for n in range(len(y)):
        x[i].append(y[n][m])
    m += 1
print(x)
[['1', '3', '80'], ['2', '5', '56'], ['3', '9', '34'], ['a', 'b', 'c']]
