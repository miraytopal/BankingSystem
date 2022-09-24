from customer import Customer
import person

class Employee(person.Person):
    # employee informations and authorization status list
    employee_list = [(741, 'Ricky', 'Morty', True), (954, 'George', 'Jetson', False), (475, 'Papa', 'Smurf', True)]

    def __init__(self, emp_id, emp_name, emp_surname):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_surname = emp_surname
        self.employee_control()

    # checking the employee's authorization status for transactions
    def employee_control(self):
        check = True
        for idx, emp in enumerate(self.employee_list):
            if self.emp_id == emp[0] and emp[3] == True:
                check = False
                self.__add_customer()
            elif self.emp_id == emp[0] and emp[3] == False:
                print('Sorry, you are not allowed to perform the transaction...')
        if check:
            print('The employee was not found in the list of bank employees.')

    # add a customer to bank system
    def __add_customer(self):
        customer = Customer(
            ID=int(input('Please enter customer\'s ID: ')),
            name=input('Please enter your customer\'s name: '),
            surname=input('Please enter your customer\'s surname: '),
            authority_check=True
        )
