def safeWholeNumber():
    wholeNum = input('Please enter a whole number: ')
    if wholeNum.startswith('-'):
        result = wholeNum.replace('-', '')
        print(f'{wholeNum} is a whole number: ', result.isdigit())

    else:
        print(f'{wholeNum} is a whole number: ', wholeNum.isdigit())

# --------
for i in range(4):
    safeWholeNumber()