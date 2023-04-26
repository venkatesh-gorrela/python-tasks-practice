amount=int(input("enter the amount: "))
option=input("enter the option: ")

def credit(amount):
    return amount

def debit(amount):
    cash = int(input("enter the cash: "))
    if amount > cash:
        return amount - cash
    if amount < cash:
        return 'invalid cash'
    
if option == '+':
    print(credit(amount))
if option == '-':
    print(debit(amount))    











