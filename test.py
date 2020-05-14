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
from puzzle import CELL

mylist={1:{1:CELL(1),2:CELL(2),3:CELL(3)}}

value=4
for cell in mylist[1].values():

    print(cell.pos_nums)
   