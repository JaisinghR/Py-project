# Python Banking program

def show_balance(balance):
    print(f"Your Balance is {balance:,.2f} INR")

def deposit():
    amount = int(input("Enter Your Amount to be Deposited: "))

    if amount < 0:
        print("That's not valid!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = int(input("Enter Your Amount to be Withdrawn: "))

    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("That's not valid!")
        return 0
    else:
        return amount
 
def main():
    balance = 0
    is_running = True
    while is_running:
        print("****************************")
        print("      Banking Porgram       ")
        print("****************************")
        print("      1. Show Balance")
        print("      2. Deposit")
        print("      3. Withdraw")
        print("      4. Exit")
        print("****************************")
        choice = input("Enter your choice(1 - 4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not valid!")
    print("****************************")
    print("Thank You! Have A Nice Day!")
    print("****************************")

if __name__ == '__main__':
    main()