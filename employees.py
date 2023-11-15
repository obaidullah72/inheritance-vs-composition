# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super().__init__(id, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate
#
#
# class CommissionEmployee(SalaryEmployee):
#     def __init__(self, id, name, weekly_salary, commission):
#         super().__init__(id, name, weekly_salary)
#         self.commission = commission
#
#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return fixed + self.commission
#
#
# class Manager(SalaryEmployee):
#     def work(self, hours):
#         print(f'{self.name} screams and yells for {hours} hours.')
#
#
# class Secretary(SalaryEmployee):
#     def work(self, hours):
#         print(f'{self.name} expends {hours} hours doing office paperwork.')
#
#
# class SalesPerson(CommissionEmployee):
#     def work(self, hours):
#         print(f'{self.name} expends {hours} hours on the phone.')
#
#
# class FactoryWorker(HourlyEmployee):
#     def work(self, hours):
#         print(f'{self.name} manufactures gadgets for {hours} hours.')
#
#
# class TemporarySecretary(Secretary, HourlyEmployee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
#
#     def calculate_payroll(self):
#         return HourlyEmployee.calculate_payroll(self)

######################
# from hr import (
#     SalaryPolicy,
#     CommissionPolicy,
#     HourlyPolicy
# )
# from productivity import (
#     ManagerRole,
#     SecretaryRole,
#     SalesRole,
#     FactoryRole
# )
#
#
# # In employees.py
#
# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.address = None
#
#
# class Manager(Employee, ManagerRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id, name)
#
#
# class Secretary(Employee, SecretaryRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id, name)
#
#
# class SalesPerson(Employee, SalesRole, CommissionPolicy):
#     def __init__(self, id, name, weekly_salary, commission):
#         CommissionPolicy.__init__(self, weekly_salary, commission)
#         super().__init__(id, name)
#
#
# class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id, name)
#
#
# class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id, name)


# In employees.py
# from productivity import ProductivitySystem
# from hr import PayrollSystem
# from contacts import AddressBook
# from representations import AsDictionaryMixin
#
#
# class Employee(AsDictionaryMixin):
#     def __init__(self, id, name, address, role, payroll):
#         self.id = id
#         self.name = name
#         self.address = address
#         self.role = role
#         self.payroll = payroll
#
#     def work(self, hours):
#         duties = self.role.perform_duties(hours)
#         print(f'Employee {self.id} - {self.name}:')
#         print(f'- {duties}')
#         print('')
#         self.payroll.track_work(hours)
#
#     def calculate_payroll(self):
#         return self.payroll.calculate_payroll()
#
#
# class EmployeeDatabase:
#     def __init__(self):
#         self._employees = [
#             {
#                 'id': 1,
#                 'name': 'Mary Poppins',
#                 'role': 'manager'
#             },
#             {
#                 'id': 2,
#                 'name': 'John Smith',
#                 'role': 'secretary'
#             },
#             {
#                 'id': 3,
#                 'name': 'Kevin Bacon',
#                 'role': 'sales'
#             },
#             {
#                 'id': 4,
#                 'name': 'Jane Doe',
#                 'role': 'factory'
#             },
#             {
#                 'id': 5,
#                 'name': 'Robin Williams',
#                 'role': 'secretary'
#             },
#         ]
#         self.productivity = ProductivitySystem()
#         self.payroll = PayrollSystem()
#         self.employee_addresses = AddressBook()
#
#     @property
#     def employees(self):
#         return [self._create_employee(**data) for data in self._employees]
#
#     def _create_employee(self, id, name, role):
#         address = self.employee_addresses.get_employee_address(id)
#         employee_role = self.productivity.get_role(role)
#         payroll_policy = self.payroll.get_policy(id)
#         return Employee(id, name, address, employee_role, payroll_policy)

# In employees.py

from productivity import get_role
from hr import get_policy
from contacts import get_employee_address
from representations import AsDictionaryMixin


class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            2: {
                'name': 'John Smith',
                'role': 'secretary'
            },
            3: {
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            4: {
                'name': 'Jane Doe',
                'role': 'factory'
            },
            5: {
                'name': 'Robin Williams',
                'role': 'secretary'
            }
        }

    @property
    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError(employee_id)
        return info


class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get('name')
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get('role'))
        self._payroll = get_policy(self.id)

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy


employee_database = _EmployeeDatabase()
