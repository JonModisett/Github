#Non-OOP
#Bank version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print('Press b to get the balance \n'+
          'Press d to make a deposit \n'+
          'Press w to make a withdrawal \n'+
          'Press s to show the account \n'+
          'Press q to quit\n')
    action = input('What do you want to do? ')
    action = action.lower()[0]

#Quit Action
    if action == 'q':
        break

#Balance Action
    elif action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        if userPassword == accountPassword:
            print('Your balnce is: ', accountBalance, '\n')
        else:
            print('Incorrect Password!')

#Depoit Action
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = int(input('Please enter amount to Deposit: '))
        userPassword = input('Plase enter the password: ')
        if userDepositAmount < 0:
            print('You cannot deposit a negative amount!')
        elif userPassword == accountPassword:
            accountBalance = accountBalance + userDepositAmount
            print('Your new Balance is: ', accountBalance, '\n')
        else:
            print('Incorrect password or other problem')

#Withdrawal Action
    elif action == 'w':
        print('Withdrawal:')
        userWithdrawAmount = int(input('Please enter the amount to withdraw: '))
        userPassword = input('Please enter the password: ')

        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount')
        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')
        elif userPassword == accountPassword:
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is: ', accountBalance, '\n')
        else:
            print('Incorrect password or other problem')

#Show Action
    elif action == 's':
        print('Show Account Information:\n',
              '\tName ', accountName, '\n'
              '\tBalance: ', accountBalance, '\n')
print('Done')
        
