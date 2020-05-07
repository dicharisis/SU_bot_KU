dictOfNames = {
   7 : 'sam',
   8: 'john',
   9: 'mathew',
   10: 'riti',
   11 : 'aadi',
   12 : 'sachin'
}

newDict = dict(filter(lambda elem: elem[0] % 2 == 0, dictOfNames.items()))
print('Filtered Dictionary : ')
print(newDict)