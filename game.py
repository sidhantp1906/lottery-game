import random
from random import choices

print('=====================start=============================================')
max_entry = 5
name = input('enter your name: ')
command = f'''
welcome {name} to our site to become crorepati in a simple way 
open for only 5 members of your family 
'''
print(command)

lists = ['']
inp = ''
i = 0

print('=======================entries=========================================')
if i == max_entry:
  print('list is full')
else:
  while i != max_entry+1:
    inp = input("""type buy to buy lottery 'or'
      type view to view lottery prizes and enrollment:
        'and' exit to leave: """)
    if inp == 'buy':
        name2 = input(f'confirm member{i+1} name: ')
        print(f'congratulations!member {i+1}: {name2}  for buying lottery')
        lists.append(name2)
    elif inp == 'view':
      cmd = '''
      prize1:car🚗
      prize2:bike🏍
      prize3:$150🎁
      '''
      print(cmd)
      print(lists)
    elif inp == 'exit':
      print('leaving the site..') 
      break 
    else:
      print('please type buy or view') 
    i = i+1 

print('=========================list==========================================')
print(f'final entry list: {lists}')

print('================================result=================================')

winner = choices(lists)
if winner == ['']:
  print('better luck next time!')
else:  
  print(f'place 1: {winner} congo! u win car')

winner1 = choices(lists)
if winner1 == ['']:
  print('better luck next time!')
elif winner1 == winner:
  print('cannot generate')  
else:  
  print(f'place 2: {winner1} congo! u win bike ')

winner2 = choices(lists)
if winner2 == ['']:
  print('better luck next time!')
elif winner2 == winner or winner2 == winner1:
    print('cannot generate')
else:  
  print(f'place 3: {winner2} congo! u win $150')

print('=================thankyou=============================================')
print('=====================copyright @sidhantp==============================') 
