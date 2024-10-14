from module4 import Bank
import datetime
class Menu:
    def __init__(self):
        self.bank = Bank()
    
    def main_menu(self):
        print("!!! *** WELCOME TO THE BANK *** !!!")
        print("1. Existing User")
        print("2. New User")
        return int(input("Select User Type: "))  
    
    def existing_user_menu(self):
        print("Service Provided:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Fixed Deposit")
        print("4. Transaction Details")
        print("5. Check Credit Card Eligibility")
        print("6. Loan Availability")
        print("7. Exit")
        return int(input("Select Service: "))  
    
    def if_existing_user(self):
        service_choice = self.existing_user_menu()
        
        if service_choice == 1:
            self.deposit_menu()
        elif service_choice == 2:
            self.withdraw_menu()
        elif service_choice == 3:
            self.fixed_deposit_menu()
        elif service_choice == 4:
            self.transaction_details_user()
        elif service_choice == 5:
            self.credit_card_eligibility_user()
        elif service_choice == 6:
            self.loan()
        elif service_choice == 7:
            return False  
        else:
            print("Invalid choice")
        return True
    
    def deposit_menu(self):
        accno = int(input("Enter Accno: "))  
        depamt = int(input("Enter Deposit amt: "))
        if depamt > 50000:
            pan = input("Enter Pan No.: ")
            if len(pan) != 5:
                print("Invalid PAN")
                return
        self.bank.deposit(accno, depamt)

    def withdraw_menu(self):
        accno = int(input("Enter Accno: "))  
        witamt = int(input("Enter Withdraw amt: "))
        if witamt > 50000:
            pan = input("Enter Pan No.: ")
            if len(pan) != 5:
                print("Invalid PAN")
                return
        self.bank.withdraw(accno, witamt)

    def fixed_deposit_menu(self):
        accno = int(input("Enter Accno: "))  
        fdamt = int(input("Enter FD amt: "))
        yrs = int(input("Enter years: "))
        self.bank.fd(accno, fdamt, yrs)

    def transaction_details_user(self):
        accno = int(input("Enter Accno: "))  
        self.bank.transaction(accno)

    def credit_card_eligibility_user(self):
        accno = int(input("Enter Accno: "))  
        self.bank.credit_card(accno)

    def loan(self):
        print("*** LOAN TYPE ***")
        print("1. Vehicle Loan")
        print("2. Home Loan")
        print("3. Personal Loan")
        print("4. Education Loan")
        loan_choice = int(input("Select Loan Type: "))
        
        if loan_choice == 1:
            self.vehicle_loan()  
        elif loan_choice == 2:
            self.home_loan()  
        elif loan_choice == 3:
            self.personal_loan()  
        elif loan_choice == 4:
            self.education_loan()  
        else:
            print("Invalid Option")

    def vehicle_loan(self):
        print("Select Vehicle Type")
        print("1. Bike")
        print("2. Car")
        vehicle_choice = int(input("Select Vehicle Type: "))  

        if vehicle_choice == 1:
            accno = int(input("Enter Your AccNo: "))
            bike_value = int(input("Enter Bike Value: "))
            model_year = int(input("Enter Model Year: "))
            if model_year > current_year:
                print(f"{model_year} is yet to be launched.")
            else:
                self.bank.bike(accno, bike_value, model_year)
        elif vehicle_choice == 2:
            accno = int(input("Enter Your AccNo: "))
            car_value = int(input("Enter Car Value: "))
            model_year = int(input("Enter Model Year: "))
            current_year = datetime.datetime.now().year
            if model_year > current_year:
                print(f"{model_year} is yet to be launched.")
            else:
                self.bank.car(accno, car_value, model_year)
        else:
            print("Invalid Option")

    def home_loan(self):
        print("Select Home Loan Type")
        print("1. Home Loan for Purchase of Land")
        print("2. Home Purchase Loan")
        print("3. Home Construction Loan")
        print("4. Home Extension Loan")
        print("5. Home Improvement Loan (Renovation)")
        homeloan_type = int(input("Select Home Loan Type: "))

        if homeloan_type == 1:
            accno = int(input("Enter Your AccNo: "))  
            loan_amt = int(input("Enter Loan Amount: "))
            loan_term = int(input("Enter Loan Tenure in Months: "))
            self.bank.loan_purchase_of_land(accno, loan_amt, loan_term)
        elif homeloan_type == 2:
            accno = int(input("Enter Your AccNo: "))  
            loan_amt = int(input("Enter Loan Amount: "))
            loan_term = int(input("Enter Loan Tenure in Months: "))
            self.bank.loan_home_purchase(accno, loan_amt, loan_term)
        elif homeloan_type == 3:
            accno = int(input("Enter Your AccNo: "))  
            loan_amt = int(input("Enter Loan Amount: "))
            loan_term = int(input("Enter Loan Tenure in Months: "))
            self.bank.loan_home_construction(accno, loan_amt, loan_term)
        elif homeloan_type == 4:
            accno = int(input("Enter Your AccNo: "))  
            loan_amt = int(input("Enter Loan Amount: "))
            loan_term = int(input("Enter Loan Tenure in Months: "))
            self.bank.loan_home_extension(accno, loan_amt, loan_term)
        elif homeloan_type == 5:
            accno = int(input("Enter Your AccNo: "))  
            loan_amt = int(input("Enter Loan Amount: "))
            loan_term = int(input("Enter Loan Tenure in Months: "))
            self.bank.loan_home_improvement(accno, loan_amt, loan_term)
        else:
            print("Invalid Option")

    def personal_loan(self):
        accno = int(input("Enter Your AccNo: "))  
        loan_amt = int(input("Enter Loan Amount: "))
        loan_term = int(input("Enter Loan Tenure in Months: "))
        self.bank.loan_personal(accno, loan_amt, loan_term)

    def education_loan(self):
        accno = int(input("Enter Your AccNo: "))  
        loan_amt = int(input("Enter Loan Amount: "))
        loan_term = int(input("Enter Loan Tenure in Months: "))
        self.bank.loan_education(accno, loan_amt, loan_term)

    def if_new_user(self):
        print("New ACCOUNT CREATION")
        name = input("Enter Name: ")
        depamt = int(input("Enter Deposit Amt: "))
        fdamt = int(input("Enter FD Amt: "))
        self.bank.create(name, depamt, fdamt)

    def run(self):
        while True:
            user_choice = self.main_menu()  

            if user_choice == 1:  
                if not self.if_existing_user():
                    break  
            elif user_choice == 2:  
                self.if_new_user()
            else:
                print("Invalid choice")


if __name__ == "__main__":
    app = Menu()
    app.run()
