from pprint import pprint


class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

        self.employees = set()

    def get_company_name(self):  # Returns the name of the company
        return self.company_name

    def get_employees(self):
        return self.employees


class Employee:
    def __init__(self, fn, ln, p):
        self.firstName = fn
        self.lastName = ln
        self.position = p


ToysOrBust = Company("ToysOrBust", "1jan2018")

# Create some employees
aaron = Employee("Aaron", "Brownlee", "Manager")
brandon = Employee("Brandon", "Tanay", "IT")
carrie = Employee("Carrie", "Lambert", "HR")

# Add the employees into the aggregate instance variable of the company
ToysOrBust.employees.add(aaron)
ToysOrBust.employees.add(brandon)
ToysOrBust.employees.add(carrie)

# print(ToysOrBust.__dict__)
pprint(vars(ToysOrBust))
