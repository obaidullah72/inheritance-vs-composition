# from employees import TemporarySecretary
import json
from hr import calculate_payroll, LTDPolicy
from productivity import track
from employees import employee_database
from contacts import Address

address = Address('55 Main St.', 'Concord', 'NH', '03301')
print(address)

# print(TemporarySecretary.__mro__)
# import hr
#
# salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])

# In program.py
#
# import hr
# import disgruntled
#
# salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# disgruntled_employee = disgruntled.DisgruntledEmployee(20000, 'Anonymous')
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee,
#     disgruntled_employee
# ])

# In program.py

# import hr
# import employees
#
# salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = employees.HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = employees.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])

# import hr
# import employees
# import productivity
#
# manager = employees.Manager(1, 'Mary Poppins', 3000)
# secretary = employees.Secretary(2, 'John Smith', 1500)
# sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
# factory_worker = employees.FactoryWorker(4, 'Jane Doe', 40, 15)
# temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)
# company_employees = [
#     manager,
#     secretary,
#     sales_guy,
#     factory_worker,
#     temporary_secretary,
# ]
# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(company_employees, 40)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(company_employees)


# In program.py
#
# import hr
# import employees
# import productivity
# import contacts
#
# manager = employees.Manager(1, 'Mary Poppins', 3000)
# manager.address = contacts.Address(
#     '121 Admin Rd',
#     'Concord',
#     'NH',
#     '03301'
# )
# secretary = employees.Secretary(2, 'John Smith', 1500)
# secretary.address = contacts.Address(
#     '67 Paperwork Ave.',
#     'Manchester',
#     'NH',
#     '03101'
# )
# sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
# factory_worker = employees.FactoryWorker(4, 'Jane Doe', 40, 15)
# temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)
# employees = [
#     manager,
#     secretary,
#     sales_guy,
#     factory_worker,
#     temporary_secretary,
# ]
# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(employees, 40)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees)

# In program.py

# from hr import PayrollSystem
# from productivity import ProductivitySystem
# from employees import EmployeeDatabase
#
# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees
# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)

#
# from hr import PayrollSystem, HourlyPolicy
# from productivity import ProductivitySystem
# from employees import EmployeeDatabase
#
# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees
# manager = employees[0]
# manager.payroll = HourlyPolicy(55)
#
# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)

# import json
# from employees import EmployeeDatabase
#
#
# def print_dict(d):
#     print(json.dumps(d, indent=2))
#
#
# for employee in EmployeeDatabase().employees:
#     print_dict(employee.to_dict())
# In program.py

# employees = employee_database.employees
#
# sales_employee = employees[2]
# ltd_policy = LTDPolicy()
# sales_employee.apply_payroll_policy(ltd_policy)
#
# track(employees, 40)
# calculate_payroll(employees)
from hr import calculate_payroll, LTDPolicy
from productivity import track
from employees import employee_database

employees = employee_database.employees

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)