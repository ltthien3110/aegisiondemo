def show_menu():
    print('ATM MENU')
    print('1.Check Balance')
    print('2.Deposit Money')
    print('3.Withdraw Money')
    print('4.Exit')
def withdraw(balance, amount):
    if balance <= 0:
        print('Negative')
    else :
        balance = balance - amount
        print('Balance:',balance)
    return balance
balance = 1000
while True:
    try:
        show_menu()
        option = int(input('Choose an option: '))
        if option == 1:
            print('Check balance: ', balance)
        elif option == 2:
            deposit_amount = float(input('Enter deposit amount: '))
            if deposit_amount > 0:
                balance = balance + deposit_amount
                print('Balance ', balance)
            else:
                print('Deposit amount must be > 0')
        elif option == 3:
            withdraw_amount = float(input('Enter withdraw amount: '))
            withdraw(balance = 1000, amount = withdraw_amount)
            balance = balance - withdraw_amount
        elif option == 4:
            print('Goodbye')
            break
        else:
            print('Invalid choice!')
    except ValueError:
        print('Please enter a valid number')
    break
                                    
                                    
            
        
        
    