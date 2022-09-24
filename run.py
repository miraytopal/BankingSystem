
from employee import Employee
from customer import Customer

# to run the banking system
while True:
    user_type = int(input(
        ''' Hello... Welcome to TrustBank System!\n 
            Please enter your user type:
                1. Customer
                2. Employee
                3. Exit the Banking System
          '''))

    if user_type == 1:
        ID = int(input('Please enter your ID: '))
        name = input('Please enter your name: ')
        surname = input('Please enter your surname: ')
        Customer(ID, name, surname)

    elif user_type == 2:
        ID = int(input('Please enter your ID: '))
        name = input('Please enter your name: ')
        surname = input('Please enter your surname: ')
        Employee(ID, name, surname)

    elif user_type == 3:
        break

    else:
        print('Please enter a valid user type')