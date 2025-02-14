import tkinter as tk
from tkinter import messagebox, simpledialog
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
class employees_manager:
#class prop
    employees=[]
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    def __init__(self, first_name, last_name, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.salary = salary
        employees_manager.employees.append(self)
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    def new_employee():
        first_name = input("Enter the employee first name: ").upper()
        last_name = input("Enter the employee last name: ").upper()
        department = input("Enter employee department: ").upper()
        salary = float(input("Enter employee salary: "))
        employees_manager(first_name, last_name, department, salary)
        print("The new employee has been added to the database.")
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    #class method
    @classmethod
    def search_employee(cls):
        if len(cls.employees) == 0:
            return "There are no employees in the database."
        else:
            matching_employees = []
            search_category = input("By what category do you want to search?\n1. First name and last name\n2. Department\n3. Salary\nEnter your choice (1 or 2 or 3): ")

            if search_category == "1":
                search_first_name = input("Please enter the first name of the employee you want to search for: ").upper()
                search_last_name = input("Please enter the last name of the employee you want to search for: ").upper()

                for employee in cls.employees:
                    if employee.first_name == search_first_name and employee.last_name == search_last_name:
                        matching_employees.append(employee)
                
            elif search_category == "2":

                search_department = input("Please enter the department of the employee you want to search for: ").upper()

                for employee in cls.employees:
                    if employee.department == search_department:
                        matching_employees.append(employee)
        
            elif search_category == "3":

                search_salary = float(input("Please enter the range of salary of the employee you want to search for: "))

                for employee in cls.employees:
                    if employee.salary <= search_salary:
                        matching_employees.append(employee)
                            
            if not matching_employees:
                if search_category == "1":
                    return f"No matching employees found for the employee {search_first_name} {search_last_name} that you entered."
                elif search_category == "2":
                    return f"No matching employees found for the department {search_department} that you entered."
                elif search_category == "3":
                    return f"No matching employees found for the salary range {search_salary} that you entered."

            return matching_employees
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def delete_employee(cls):
        if len(cls.employees) == 0:
            return "There are no employees in the database."

        deleted_employees = []
        search_category = input("By what category do you want to search for the employee to delete?\n1. First name and last name\n2. Department\n3. Salary\nEnter your choice (1/2/3): ")

        if search_category == "1":
            delete_employee_first_name = input("Please enter the first name of the employee you want to delete: ").upper()
            delete_employee_last_name = input("Please enter the last name of the employee you want to delete: ").upper()
            loop_counter = 0
            while loop_counter < len(cls.employees):
                employee = cls.employees[loop_counter]
                if employee.first_name == delete_employee_first_name and employee.last_name == delete_employee_last_name:
                    print(employee)
                    answer = input("Is this the employee you want to delete? [ Please enter { yes or no } or { y or n } ]: ").upper()
                    if answer == "YES" or answer == "Y":
                        deleted_employees.append(cls.employees.pop(loop_counter))
                        print("The employee has been deleted from the database.")
                    elif answer == "NO" or answer == "N":
                        print("The employee has not been deleted from the database.")
                        loop_counter += 1
                    else:
                        print("Invalid input. Please try again.")
                else:
                    loop_counter += 1

        elif search_category == "2":
            delete_department = input("Please enter the department of the employee(s) you want to delete: ").upper()
            loop_counter = 0
            while loop_counter < len(cls.employees):
                employee = cls.employees[loop_counter]
                if employee.department == delete_department:
                    print(employee)
                    answer = input("Is this the employee you want to delete? [ Please enter { yes or no } or { y or n } ]: ").upper()
                    if answer == "YES" or answer == "Y":
                        deleted_employees.append(cls.employees.pop(loop_counter))
                        print("The employee has been deleted from the database.")
                    elif answer == "NO" or answer == "N":
                        print("The employee has not been deleted from the database.")
                        loop_counter += 1
                    else:
                        print("Invalid input. Please try again.")
                else:
                    loop_counter += 1

        elif search_category == "3":
            try:
                delete_salary = float(input("Please enter the salary range of the employee(s) you want to delete: "))
                
                loop_counter = 0
                while loop_counter < len(cls.employees):
                    employee = cls.employees[loop_counter]
                    if employee.salary <= delete_salary:
                        print(employee)
                        answer = input("Is this the employee you want to delete? [ Please enter { yes or no } or { y or n } ]: ").upper()
                        if answer == "YES" or answer == "Y":
                            deleted_employees.append(cls.employees.pop(loop_counter))
                            print("The employee has been deleted from the database.")
                        elif answer == "NO" or answer == "N":
                            print("The employee has not been deleted from the database.")
                            loop_counter += 1
                        else:
                            print("Invalid input. Please try again.")
                    else:
                        loop_counter += 1
            except ValueError:
                return "Invalid salary input. Please enter a valid number."

        else:
            return "Invalid search category selected. Please choose 1, 2, or 3."

        if not deleted_employees:
            return "No employees were deleted."

        return deleted_employees
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def update_employee(cls):
        if len(cls.employees) == 0:
            return "There are no employees in the database."

        updated_employees = []
        search_category = input("By what category do you want to search for the employee to update?\n1. First name and last name\n2. Department\n3. Salary\nEnter your choice (1/2/3): ")

        if search_category == "1":
            update_employee_first_name = input("Please enter the first name of the employee you want to update: ").upper()
            update_employee_last_name = input("Please enter the last name of the employee you want to update: ").upper()
            
            loop_counter = 0
            while loop_counter < len(cls.employees):
                employee = cls.employees[loop_counter]
                if employee.first_name == update_employee_first_name and employee.last_name == update_employee_last_name:
                    print(employee)
                    answer = input("Is this the employee you want to update? [ Please enter { yes or no } or { y or n } ]: ").upper()
                    if answer == "YES" or answer == "Y":
                        print("Enter the new details for the employee:")
                        new_first_name = input("New first name: ").upper()
                        new_last_name = input("New last name: ").upper()
                        new_department = input("New department: ").upper()
                        
                        while True:
                            try:
                                new_salary = float(input("New salary: "))
                                break
                            except ValueError:
                                print("Invalid salary input. Please enter a valid number.")
                        
                        employee.first_name = new_first_name
                        employee.last_name = new_last_name
                        employee.department = new_department
                        employee.salary = new_salary
                        
                        updated_employees.append(employee)
                        print("The employee has been updated.")
                    elif answer == "NO" or answer == "N":
                        print("The employee has not been updated.")
                        loop_counter += 1
                    else:
                        print("Invalid input. Please try again.")
                else:
                    loop_counter += 1

        elif search_category == "2":
            update_department = input("Please enter the department of the employee(s) you want to update: ").upper()
            
            loop_counter = 0
            while loop_counter < len(cls.employees):
                employee = cls.employees[loop_counter]
                if employee.department == update_department:
                    print(employee)
                    answer = input("Is this the employee you want to update? [ Please enter { yes or no } or { y or n } ]: ").upper()
                    if answer == "YES" or answer == "Y":
                        print("Enter the new details for the employee:")
                        new_first_name = input("New first name: ").upper()
                        new_last_name = input("New last name: ").upper()
                        new_department = input("New department: ").upper()
                        
                        while True:
                            try:
                                new_salary = float(input("New salary: "))
                                break
                            except ValueError:
                                print("Invalid salary input. Please enter a valid number.")
                        
                        employee.first_name = new_first_name
                        employee.last_name = new_last_name
                        employee.department = new_department
                        employee.salary = new_salary
                        
                        updated_employees.append(employee)
                        print("The employee has been updated.")
                    elif answer == "NO" or answer == "N":
                        print("The employee has not been updated.")
                        loop_counter += 1
                    else:
                        print("Invalid input. Please try again.")
                else:
                    loop_counter += 1

        elif search_category == "3":
            while True:
                try:
                    update_salary = float(input("Please enter the salary range of the employee(s) you want to update: "))
                    break
                except ValueError:
                    print("Invalid salary input. Please enter a valid number.")
            
            loop_counter = 0
            while loop_counter < len(cls.employees):
                employee = cls.employees[loop_counter]
                if employee.salary <= update_salary:
                    print(employee)
                    answer = input("Is this the employee you want to update? [ Please enter { yes or no } or { y or n } ]: ").upper()
                    if answer == "YES" or answer == "Y":
                        print("Enter the new details for the employee:")
                        new_first_name = input("New first name: ").upper()
                        new_last_name = input("New last name: ").upper()
                        new_department = input("New department: ").upper()
                        
                        
                        while True:
                            try:
                                new_salary = float(input("New salary: "))
                                break
                            except ValueError:
                                print("Invalid salary input. Please enter a valid number.")
                        
                        employee.first_name = new_first_name
                        employee.last_name = new_last_name
                        employee.department = new_department
                        employee.salary = new_salary
                        
                        updated_employees.append(employee)
                        print("The employee has been updated.")
                    elif answer == "NO" or answer == "N":
                        print("The employee has not been updated.")
                        loop_counter += 1
                    else:
                        print("Invalid input. Please try again.")
                else:
                    loop_counter += 1

        else:
            return "Invalid search category selected. Please choose 1, 2, or 3."

        if not updated_employees:
            return "No employees were updated."

        return updated_employees
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    def all_employee_information(cls):
        if len(employees_manager.employees) == 0:
            print("There are no employees in the database.")
        else:
            for employee in cls.employees:
                print(employee)
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name} Department: {self.department} Salary: {self.salary}"
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
class accounts_manager:
    accounts = []
    account_number=20250101
#class prop
    def __init__(self, account_holder_first_name, account_holder_last_name, amount, account_number=0):
        self.account_holder_first_name = account_holder_first_name
        self.account_holder_last_name = account_holder_last_name
        self.amount = amount
        self.account_number = accounts_manager.account_number
        accounts_manager.accounts.append(self)
        accounts_manager.accout_number += 1
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    def __str__(self):
            return f"The name of the account holder is {self.account_holder_first_name} {self.account_holder_last_name} , amount is {self.amount} , and account number is {self.account_number}"
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def deposit(cls):
        if len(cls.accounts) == 0:
            return "There are no accounts in the database."
        
        else:
            account = cls.find_account()
            if isinstance(account,str):
                return account
            
            else:
                while True:
                    try:
                        deposit_amount = float(input("Enter the amount to deposit: "))
                        if deposit_amount <= 0:
                            print("Deposit amount must be greater than 0.")
                        else:
                            break
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")

                print(f"Depositing ${deposit_amount} into account {account.account_number}.")
                confirm = input("Confirm deposit? [yes/no]: ").upper()
                if confirm == "YES" or confirm == "Y":

                    account.amount += deposit_amount
                    print("Deposit successful.")
                    print(f"Updated account balance: ${account.amount}")
                else:
                    print("Deposit canceled.")

                return
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def withdraw(cls):
        if len(cls.accounts) == 0:
            return "There are no accounts in the database."

        else:
            account = cls.find_account()
            if isinstance(account,str):
                return account
            
            else:
                while True:
                    try:
                        withdraw_amount = float(input("Enter the amount to withdraw: "))
                        if withdraw_amount <= 0:
                            print("Withdrawal amount must be greater than 0.")
                        elif withdraw_amount > account.amount:
                            print("Insufficient funds in the account.")
                        else:
                            break
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")

                print(f"Withdrawing ${withdraw_amount} from account {account.account_number}.")
                confirm = input("Confirm withdrawal? [yes/no]: ").upper()
                if confirm == "YES" or confirm == "Y":

                    account.amount -= withdraw_amount
                    print("Withdrawal successful.")
                    print(f"Updated account balance: ${account.amount}")

                else:
                    print("Withdrawal canceled.")

                return
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    def transfer():
        pass
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def all_account_information(cls):
        if len(accounts_manager.accounts) == 0:
            print("There are no accounts in the database.")
        else:
            for account in cls.accounts:
                print(account)
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def delete_account(cls):
        if len(cls.accounts) == 0:
            return "There are no accounts in the database."

        deleted_accounts = []
        search_category = input("By what category do you want to search for the account to delete?\n1. Account holder first name and last name\n2. Account number\n3. Amount\nEnter your choice (1 or 2 or 3): ")

        if search_category == "1":
            search_first_name = input("Please enter the first name of the account holder you want to delete: ").upper()
            search_last_name = input("Please enter the last name of the account holder you want to delete: ").upper()

            loop_counter = 0
            while loop_counter < len(cls.accounts):
                account = cls.accounts[loop_counter]
                if account.account_holder_first_name.upper() == search_first_name and account.account_holder_last_name.upper() == search_last_name:
                    print(account)
                    answer = input("Is this the account you want to delete? [ Please enter { yes or no } or { y or n } ]: ").upper()
                    if answer == "YES" or answer == "Y":
                        deleted_accounts.append(cls.accounts.pop(loop_counter))
                        print("The account has been deleted from the database.")
                    elif answer == "NO" or answer == "N":
                        print("The account has not been deleted from the database.")
                        loop_counter += 1
                    else:
                        print("Invalid input. Please try again.")
                else:
                    loop_counter += 1

        elif search_category == "2":
            try:
                search_account_number = int(input("Please enter the account number of the account you want to delete: "))
                
                loop_counter = 0
                while loop_counter < len(cls.accounts):
                    account = cls.accounts[loop_counter]
                    if account.account_number == search_account_number:
                        print(account)
                        answer = input("Is this the account you want to delete? [ Please enter { yes or no } or { y or n } ]: ").upper()
                        if answer == "YES" or answer == "Y":
                            deleted_accounts.append(cls.accounts.pop(loop_counter))
                            print("The account has been deleted from the database.")
                        elif answer == "NO" or answer == "N":
                            print("The account has not been deleted from the database.")
                            loop_counter += 1
                        else:
                            print("Invalid input. Please try again.")
                    else:
                        loop_counter += 1
            except ValueError:
                return "Invalid account number. Please enter a valid number."

        elif search_category == "3":
            try:
                search_amount = float(input("Please enter the amount range of the account(s) you want to delete: "))
                
                loop_counter = 0
                while loop_counter < len(cls.accounts):
                    account = cls.accounts[loop_counter]
                    if account.amount <= search_amount:
                        print(account)
                        answer = input("Is this the account you want to delete? [ Please enter { yes or no } or { y or n } ]: ").upper()
                        if answer == "YES" or answer == "Y":
                            deleted_accounts.append(cls.accounts.pop(loop_counter))
                            print("The account has been deleted from the database.")
                        elif answer == "NO" or answer == "N":
                            print("The account has not been deleted from the database.")
                            loop_counter += 1
                        else:
                            print("Invalid input. Please try again.")
                    else:
                        loop_counter += 1
            except ValueError:
                return "Invalid amount input. Please enter a valid number."

        else:
            return "Invalid search category selected. Please choose 1, 2, or 3."

        if not deleted_accounts:
            return "No accounts were deleted."

        return deleted_accounts
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def search_account(cls):
        if len(cls.accounts) == 0:
            return "There are no accounts in the database."
        else:
            matching_accounts = []
            search_category = input("By what category do you want to search?\n1. Account holder first name and last name\n2. Account number\n3. Amount\nEnter your choice (1 or 2 or 3): ")

            if search_category == "1":
                search_first_name = input("Please enter the first name of the account holder you want to search for: ").upper()
                search_last_name = input("Please enter the last name of the account holder you want to search for: ").upper()

                for account in cls.accounts:
                    if account.account_holder_first_name == search_first_name and account.account_holder_last_name == search_last_name:
                        matching_accounts.append(account)
                    
            elif search_category == "2":
                try:
                    search_account_number = int(input("Please enter the account number of the account you want to search for: "))
                    
                    for account in cls.accounts:
                        if account.account_number == search_account_number:
                            matching_accounts.append(account)
                except ValueError:
                    return "Invalid account number. Please enter a valid number."

            elif search_category == "3":
                try:
                    search_amount = float(input("Please enter the amount range of the account you want to search for: "))
                    
                    for account in cls.accounts:
                        if account.amount <= search_amount:
                            matching_accounts.append(account)
                except ValueError:
                    return "Invalid amount input. Please enter a valid number."
                                
            if not matching_accounts:
                if search_category == "1":
                    return f"No matching accounts found for the account holder {search_first_name} {search_last_name} that you entered."
                elif search_category == "2":
                    return f"No matching accounts found for the account number {search_account_number} that you entered."
                elif search_category == "3":
                    return f"No matching accounts found for the amount range {search_amount} that you entered."

            return matching_accounts
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    def new_account():
        account_holder_first_name = input("Enter the first name of the account holder: ").upper()
        account_holder_last_name = input("Enter the last name of the account holder: ").upper()
        amount = float(input("Enter the amount: "))
        accounts_manager(account_holder_first_name, account_holder_last_name, amount)
        print("The new account has been added to the database.")
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def update_account(cls):
        if len(cls.accounts) == 0:
            return "There are no accounts in the database."

        updated_accounts = []
        search_category = input("By what category do you want to search for the account to update?\n1. Account holder first name and last name\n2. Account number\n3. Amount\nEnter your choice (1 or 2 or 3): ")

        if search_category == "1":
            search_first_name = input("Please enter the first name of the account holder you want to update: ").upper()
            search_last_name = input("Please enter the last name of the account holder you want to update: ").upper()

            loop_counter = 0
            while loop_counter < len(cls.accounts):
                account = cls.accounts[loop_counter]
                if account.account_holder_first_name == search_first_name and account.account_holder_last_name == search_last_name:
                    print(account)
                    answer = input("Is this the account you want to update? [ Please enter { yes or no } or { y or n } ]: ").upper()
                    if answer == "YES" or answer == "Y":
                        print("Enter the new details for the account:")
                        new_first_name = input("New first name: ").upper()
                        new_last_name = input("New last name: ").upper()
                        
                        while True:
                            try:
                                new_amount = float(input("New amount: "))
                                break
                            except ValueError:
                                print("Invalid amount input. Please enter a valid number.")
                        
                        account.account_holder_first_name = new_first_name
                        account.account_holder_last_name = new_last_name
                        account.amount = new_amount
                        
                        updated_accounts.append(account)
                        print("The account has been updated.")
                    elif answer == "NO" or answer == "N":
                        print("The account has not been updated.")
                        loop_counter += 1
                    else:
                        print("Invalid input. Please try again.")
                else:
                    loop_counter += 1

        elif search_category == "2":
            try:
                search_account_number = int(input("Please enter the account number of the account you want to update: "))
                
                loop_counter = 0
                while loop_counter < len(cls.accounts):
                    account = cls.accounts[loop_counter]
                    if account.account_number == search_account_number:
                        print(account)
                        answer = input("Is this the account you want to update? [ Please enter { yes or no } or { y or n } ]: ").upper()
                        if answer == "YES" or answer == "Y":
                            print("Enter the new details for the account:")
                            new_first_name = input("New first name: ").upper()
                            new_last_name = input("New last name: ").upper()

                            while True:
                                try:
                                    new_amount = float(input("New amount: "))
                                    break
                                except ValueError:
                                    print("Invalid amount input. Please enter a valid number.")
                            
                            account.account_holder_first_name = new_first_name
                            account.account_holder_last_name = new_last_name
                            account.amount = new_amount
                            
                            updated_accounts.append(account)
                            print("The account has been updated.")
                        elif answer == "NO" or answer == "N":
                            print("The account has not been updated.")
                            loop_counter += 1
                        else:
                            print("Invalid input. Please try again.")
                    else:
                        loop_counter += 1
            except ValueError:
                return "Invalid account number. Please enter a valid number."

        elif search_category == "3":
            try:
                search_amount = float(input("Please enter the amount range of the account(s) you want to update: "))
                
                loop_counter = 0
                while loop_counter < len(cls.accounts):
                    account = cls.accounts[loop_counter]
                    if account.amount <= search_amount:
                        print(account)
                        answer = input("Is this the account you want to update? [ Please enter { yes or no } or { y or n } ]: ").upper()
                        if answer == "YES" or answer == "Y":
                            print("Enter the new details for the account:")
                            new_first_name = input("New first name: ").upper()
                            new_last_name = input("New last name: ").upper()

                            while True:
                                try:
                                    new_amount = float(input("New amount: "))
                                    break
                                except ValueError:
                                    print("Invalid amount input. Please enter a valid number.")
                            
                            account.account_holder_first_name = new_first_name
                            account.account_holder_last_name = new_last_name
                            account.amount = new_amount
                            
                            updated_accounts.append(account)
                            print("The account has been updated.")
                        elif answer == "NO" or answer == "N":
                            print("The account has not been updated.")
                            loop_counter += 1
                        else:
                            print("Invalid input. Please try again.")
                    else:
                        loop_counter += 1
            except ValueError:
                return "Invalid amount input. Please enter a valid number."

        else:
            return "Invalid search category selected. Please choose 1, 2, or 3."

        if not updated_accounts:
            return "No accounts were updated."

        return updated_accounts
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def transfer(cls):
        if len(cls.accounts) == 0:
            return "There are no accounts in the database."

        else:
            print("Enter details for the source account (from which funds will be transferred):")
            source_account = cls._find_account()
            if isinstance(source_account,str):
                return source_account

            else:
                print("Enter details for the destination account (to which funds will be transferred):")
                destination_account = cls._find_account()
                if isinstance(source_account,str):
                    return source_account
                
                else:
                    if source_account.account_number == destination_account.account_number:
                        return "Source and destination accounts cannot be the same."

                    while True:
                        try:
                            transfer_amount = float(input("Enter the amount to transfer: "))
                            if transfer_amount <= 0:
                                print("Transfer amount must be greater than 0.")
                            elif transfer_amount > source_account.amount:
                                print("Insufficient funds in the source account.")
                            else:
                                break
                        except ValueError:
                            print("Invalid amount. Please enter a valid number.")

                    print(f"Transferring ${transfer_amount} from account {source_account.account_number} to account {destination_account.account_number}.")
                    confirm = input("Confirm transfer? [yes/no]: ").upper()
                    if confirm == "YES" or confirm == "Y":

                        source_account.amount -= transfer_amount
                        destination_account.amount += transfer_amount
                        print("Transfer successful.")
                        print(f"Updated source account balance: ${source_account.amount}")
                        print(f"Updated destination account balance: ${destination_account.amount}")

                    elif confirm == "NO" or confirm == "N":
                        print("Transfer canceled.")

                    else:
                        print("Invalid input. Transfer canceled.")

                    return
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>
    @classmethod
    def find_account(cls):
        if len(cls.accounts) == 0:
            return "There are no accounts in the database."
        else:
            while True:
                try:
                    account_number = int(input("Enter the account number: "))
                    for account in cls.accounts:
                        if account.account_number == account_number:
                            return account
                    print("Account not found. Please try again.")
                except ValueError:
                    print("Invalid account number. Please enter a valid number.")
#<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>