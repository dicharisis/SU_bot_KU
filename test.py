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

combinations = 10
combo=1023

binary=[int(i) for i in  bin(combo)[2:]]
print(binary)

result=[0 for i in range((combinations+1)-len(binary))] 
print(result)


result[-1:]=binary

print(result)
