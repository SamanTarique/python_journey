import random


class Company:
    company_employees = []
    companies = []

    def __init__(self, company_name, address):
        self.company_id = random.randint(1, 100)
        self.company_name = company_name
        self.address = address
        self.set_comapany_data()

    def __str__(self):
        return (
            f"company_id: {self.company_id} "
            f"company_name: {self.company_name} "
            f"address: {self.address}"
        )

    def set_comapany_data(self):
        company_obj = {
                "company_id": self.company_id,
                "company_name": self.company_name,
                "address": self.address,
            }
        self.companies.append(company_obj)

    def get_company_employees(self, company_name):
        if company_name not in [i["company_name"] for i in self.companies]:
            return print(f"{company_name} doesnt exist")

        return [
                i
                for i in self.company_employees
                if self.company_name == company_name
                ]

    def get_companies(self):
        return self.companies


class Employee(Company):

    employees = []

    def __init__(
            self, company_name, emp_name, age, role, date_of_joining, team_lead
            ):
        self.company_name = company_name
        self.emp_id = random.randint(100, 10000)
        self.emp_name = emp_name
        self.age = age
        self.role = role
        self.date_of_joining = date_of_joining
        self.team_lead = team_lead
        self.emp_data = self.set_employee_data()
        Company.company_employees.append(self.emp_data)

    def __str__(self):
        return (
            f"company_name: {self.company_name}, "
            f"emp_id: {self.emp_id}, "
            f"emp_name: {self.emp_name}, "
            f"age: {self.age}, "
            f"role: {self.role}, "
            f"date_of_joining: {self.date_of_joining}, "
            f"team_lead: {self.team_lead}"
        )

    def set_employee_data(self):
        emp_record = {
            "company_name": self.company_name,
            "emp_id": self.emp_id,
            "emp_name": self.emp_name,
            "age": self.age,
            "role": self.role,
            "date_of_joining": self.date_of_joining,
            "team_lead": self.team_lead,
        }
        self.employees.append(emp_record)
        return emp_record

    # def get_company_employees(self, company_name):
    #     return [
    #         i for i in self.company_employees
    #         if i["company_name"] == company_name
    #     ]


company1 = Company("Bestpeers", "ELECTRONIC COMPLEX")
print(company1)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("company emps->", company1.get_company_employees("Bestpeers"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(company1.get_companies())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

emp1 = Employee(
    "Bestpeers", "Anurodh", 24,
    "Software Dev", "01/09/2025", "sagar jain"
    )
# print(emp1)
# emp2 = Employee(
#     "Oracle", "aman", 24,
#     "Software Dev", "01/09/2025", "harshit jain"
#     )
print("company emps->", company1.get_company_employees("Bestpeers"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("company emps->", company1.get_company_employees("Oracle"))
