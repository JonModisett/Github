#Non-OOP
#Bank 4
#Single Account

'''Variable'''
accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

#Function to create an Account
def newAccount(name, balance, password):
    global accountNamseList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)

#Function to Show Account information
def getShow(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password == accountPasswordsList[accountNumber]:
        return print(f'\nAccount {accountNumber} \n\tName {accountNamesList[accountNumber]} \n\tBalance {accountBalancesList[accountNumber]} \n')
    else:
        return print("Sorry something is incorrect.")

#Function to get Balance
def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password == accountPasswordsList[accountNumber]:
        return print(f'\nYour balance is: {accountBalancesList[accountNumber]} \n')
    else:
        return print("\nSorry something is incorrect.\n")

#Function to get Withdrawl
def getWithdrawal(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    try:
        userWithdrawAmount = int(input('\nHow much would you like to withdrawal?\n'))
    except ValueError:
        return print("\nThe value must be an integer.\n")
    if password == accountPasswordsList[accountNumber]:
        if userWithdrawAmount < 0:
            return print('\nYou cannot withdraw a negative amount\n')
        elif userWithdrawAmount > accountBalancesList[accountNumber]:
            return print('\nYou cannot withdraw more than you have in your account\n')
        else:
            accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - userWithdrawAmount
            return print(f'\nYour new balance is: {accountBalancesList[accountNumber]} \n')
    else:
        return print("\nSorry something is incorrect.\n")

#Function to get Deposit
def getDeposit(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    try:
        userDepositAmount = int(input('How much would you like to deposit? '))
    except ValueError:
        return print("\nThe value must be an integer.\n")
    if password == accountPasswordsList[accountNumber]:
        if userDepositAmount < 0:
            return print('You cannot deposit a negative amount!')
        else:
            accountBalancesList[accountNumber] = accountBalancesList[accountNumber] + userDepositAmount
            return print(f'Your new balance is: {accountBalancesList[accountNumber]} \n')
    else:
        return print("\nSorry something is incorrect.\n")


#Create two sample accounts
print("Joe's account is account number: ", len(accountNamesList))
newAccount("Joe", 100, 'soup')
print("Mary's account is account number: ", len(accountNamesList), '\n')
newAccount("Mary", 12345, 'nuts')


#Prompts to user
while True:
    print('Press b to get the balance \n'+
          'Press d to make a deposit \n'+
          'Press w to make a withdrawal \n'+
          'Press s to show the account \n'+
          'Press q to quit\n')
    action = input('What do you want to do? ')
    action = action.lower()[0]

#User action transfer to funciton
#Quit Action
    if action == 'q':
        break

#Balance Action
    elif action == 'b':
        userAccountNumber = int(input('\nPlease enter your account number: '))
        userPassword = input('\nPlease enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print(theBalance)

#Depoit Action
    elif action == 'd':
        userAccountNumber = int(input('\nPlease enter your account number: '))
        userPassword = input('\nPlease enter the password: ')
        theDeposit = getDeposit(userAccountNumber, userPassword)
        if theDeposit is not None:
            print(theDeposit)

#Withdrawal Action
    elif action == 'w':
        userAccountNumber = int(input('\nPlease enter your account number: '))
        userPassword = input('\nPlease enter the password: ')
        theWithdrawal = getWithdrawal(userAccountNumber, userPassword)
        if theWithdrawal is not None:
            print(theWithdrawal)

#Show Action
    elif action == 's':
        userAccountNumber = int(input('\nPlease enter your account number: '))
        userPassword = input('\nPlease enter the password: ')
        theShow = getShow(userAccountNumber, userPassword)
        if theShow is not None:
            print(theShow)

print('Done')
    
