import person

class Customer(person.Person):
    customer_list = []

    # authority_check uses it to ensure that a customer account can only be created by a bank employee.
    def __init__(self, ID, name, surname, authority_check=False):
        super().__init__(ID, name, surname)
        self.authority_check = authority_check
        self.__addcustomer()

    # checking existing customer account and adding new customers
    def __addcustomer(self):
        if self.ID not in [id[0] for id in self.customer_list] and self.authority_check == True:
            self.customer_list.append([self.ID, self.name, self.surname, 0])
            self.Transaction()
            return self.customer_list
        elif self.ID in [id[0] for id in self.customer_list]:
            self.Transaction()
        else:
            print('You do not have permission to create a new customer account.')

    # choosing transaction
    def Transaction(self):
        while True:
            transaction = int(input(
                'Please enter a transcation :\n 1.Deposit Money\n 2.Withdraw Money\n 3.Transfer Money\n 4.Exit The Menu\n'))
            if transaction == 1:
                self.deposit_money(int(input('Please enter a deposit amount: ')))
            elif transaction == 2:
                self.withdraw_money(int(input('Please enter a withdraw amount: ')))
            elif transaction == 3:
                self.transfer_money(int(input('Please enter a transfer money amount: ')))
            elif transaction == 4:
                break
            else:
                print('Please enter a valid transaction.')

    # show customers info, employee can show all customers but a customer show just own account informations
    def show_info(self, customer):
        if self.authority_check:
            choice = int(input(
                """Please enter a process
                  1. I want to see current customer\'s infos
                  2. I want to see all customer\'s infos   
                """))
            if choice == 1:
                print(customer)
            elif choice == 2:
                print(self.customer_list)
            else:
                print('Invalid enter!')
        else:
            print(customer)

    # get a customer's information
    def get_info(self):
        for idx, cus in enumerate(self.customer_list):
            if self.ID == cus[0]:
                return self.customer_list[idx]

    def deposit_money(self, deposit_amount):
        customer = self.get_info()
        customer[3] += deposit_amount
        self.show_info(customer)
        return self.customer_list

    def withdraw_money(self, withdraw_amount):
        customer = self.get_info()
        if customer[3] >= withdraw_amount:
            customer[3] -= withdraw_amount
            self.show_info(customer)
            return self.customer_list
        else:
            print('You have not enough money for the transaction...')

    # transfer money to other customers
    def transfer_money(self, transfer_amount):
        customer = self.get_info()
        other_cus_id = int(input('Please enter the ID of the customer you want to transfer money to: '))
        if other_cus_id in [id[0] for id in self.customer_list] and other_cus_id != customer[0]:
            # Checking the customer in the list and getting customer information
            for idx, cus in enumerate(self.customer_list):
                if other_cus_id == cus[0]:
                    other_customer = self.customer_list[idx]
        elif other_cus_id == customer[0]:
            return print('You can\'t transfer money to yourself!')
        else:
            return print('The customer couldn\'t find the bank system...Please try again with different customer id.')

        if customer[3] >= transfer_amount:
            customer[3] -= transfer_amount
            other_customer[3] += transfer_amount
            self.show_info(customer)
            return self.customer_list
        else:
            print('You don\'t have enough money your account for the transfer.')
