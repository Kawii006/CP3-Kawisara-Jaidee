username = input('Username : ')
password = input('Password : ')
if username == 'doda' and password == '0987':
   print('-'*30)
   print('Welcome to poppy Shop')
   print('-'*30)
   print(' 1.Omelette ',30 ,'THB')
   print(' 2.Noodles  ',35 ,'THB')
   print(' 3.Steak    ',59 ,'THB')
   Omelette = 30
   Noodles  = 35
   Steak    = 59
X = int(input("Choose a num :"))
if X ==1:
        amountInput = int(input('Amount = '))
        print('Total Food',Omelette*amountInput,'THB')
if X ==2:
        amountInput = int(input('Amount = '))
        print('Total Food',Noodles*amountInput,'THB')
if X ==3:
        amountInput = int(input('Amount = '))
        print('Total Food',Steak*amountInput,'THB')

else:
  print("-----Sorry-----")
