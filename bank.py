from colorama import init, Fore
init()
class BankSystem:
    def __init__(self, user, bal1, bal2, acctype1, acctype2):
        self.user = user
        self.bal1 = bal1
        self.bal2 = bal2
        self.acctype1 = acctype1
        self.acctype2 = acctype2

    def viewbal(self):
        choice = int(input(f"\nWhich Balance would you like to view? \n1. {self.acctype1} \n2. {self.acctype2}: "))
        if choice == 1:
            print(f"{self.acctype1} {Fore.GREEN}balance: {self.bal1}{Fore.RESET}")
            self.accoptions()
        elif choice == 2:
            print(f"{self.acctype2} balance: {self.bal2}")
            self.accoptions()
        else:
            print("Please enter 1 or 2...")
            self.viewbal()
    
    def accoptions(self):
        print("**********************************************************")
        choice = int(input("\nWould you like to do any of the following?\n1. Deposit \n2. Withdraw\n3. Exit\n"))
        if choice == 1:
            self.deposit()
        if choice == 2:
            self.withdraw()
        if choice == 3:
            accountuser()

    def deposit(self):
        amount = float(input(f"Your current balance is {self.bal1} in {self.acctype1} and {self.bal2} in {self.acctype2}\n How much would you like to Deposit?"))
        selection = int(input(f"\nWhich account would you like to deposit this into? \n1. {self.acctype1} \n2. {self.acctype2}"))

        if selection == 1:
            self.bal1 += amount
            print(f"Successfully deposited {Fore.GREEN}£{amount}{Fore.RESET} into {self.acctype1} \nYour new balance is {Fore.GREEN}{self.bal1}{Fore.RESET}")            
            filename = f"D:/Generation/top/{self.user}.txt"
            with open(filename, 'r') as file:
                lines = file.readlines()
            lines[1] = f"{self.bal1}\n"
            with open(filename, 'w') as file:
                file.writelines(lines)

        if selection == 2:
            self.bal2 += amount
            print(f"Successfully deposited {Fore.GREEN}£{amount}{Fore.RESET} into {self.acctype2} \nYour new balance is {Fore.GREEN}{self.bal2}{Fore.RESET}")            
            filename = f"D:/Generation/top/{self.user}.txt"
            with open(filename, 'r') as file:
                lines = file.readlines()
            lines[2] = f"{self.bal2}\n"
            with open(filename, 'w') as file:
                file.writelines(lines)

    def withdraw(self):
        amount = float(input(f"Your current balance is {self.bal1} in {self.acctype1} and {self.bal2} in {self.acctype2}\n How much would you like to Withdraw?"))
        selection = int(input(f"\nWhich account would you like to withdraw from? \n1. {self.acctype1} \n2. {self.acctype2}"))

        if selection == 1:
            self.bal1 -= amount
            print(F"Successfully withdrawed {Fore.GREEN}£{amount}{Fore.RESET} from {self.acctype1} \nYour new balance is {Fore.GREEN}£{self.bal1}{Fore.RESET}")

            

            filename = f"D:/Generation/top/{self.user}.txt"
            with open(filename, 'r') as file:
                lines = file.readlines()
            lines[1] = f"{self.bal1}\n"
            with open(filename, 'w') as file:
                file.writelines(lines)

def data_loading(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
        return BankSystem(user = lines[0], bal1 = float(lines[1]), bal2 = float(lines[2]), acctype1 = lines[3], acctype2 = lines[4])

def accountuser():
        userentry = input(f"\n{Fore.GREEN}**********************************************************{Fore.RESET}\nWelcome to Atef's Amazing Zero Interest Bank \nPlease enter your Username to view your account!:\n ")
        if userentry.lower() == "atef":
            atef.viewbal()
        elif userentry.lower() == "antony":
            antony.viewbal()
        elif userentry.lower() == "curtis":
            curtis.viewbal()

atef = data_loading('D:/Generation/top/atef.txt')
antony = data_loading('D:/Generation/top/antony.txt')
curtis = data_loading('D:/Generation/top/curtis.txt')


accountuser()