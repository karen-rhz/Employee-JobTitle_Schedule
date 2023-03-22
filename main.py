# Since "Team Manager" "Clerk" and stuff are using the EmployeeProfile as a base
# We don't have to import the EmployeeProfile to main
# EmployeeProfile becomes a superclass or an ABSTRACT BASE CLASS
from employeeSettings import TeamManager, Clerk, Pharmacist, CustomJobTitle
from reports import AccountingReport, StaffingReport, ScheduleReport
from shift import MorningShift, NightShift, CustomShift

# employee_1 is an object
# employee_1 is using the blueprint from class EmployeeProfile to be used
employee_1 = TeamManager("Karen", "Raha", 31, "29-08-1996", "01-05-2018", MorningShift())
# Always specify what attribute in the file you want to print
# Can't just say print(employee_1) if I want all info about the new employee
# Must be employee_1.name to retrieve name from EmployeeProfile class even if we did specify them earlier
# print(f"New employee name :\n{employee_1.name}, Salary:{employee_1.salary}$/h,"
#       f"\nDOB: {employee_1.date_of_birth}, \nDOH: {employee_1.hired_since}")

# Populating my employee list with more employees
# each of them is an object, but they don't need a specific name like "employee_1"
# they can be used as is as long as the required values are given
employee_list = [
    Pharmacist("Lauren", "Raha", 30, "24-08-1998", "01-01-2023", MorningShift()),
    Clerk("Marshall", "Rabe", 25, "29-08-2003", "01-05-2020", NightShift()),
    Pharmacist("Lionel", "Andria", 31, "29-08-1999", "01-05-2016", MorningShift()),
    employee_1,
]


def get_all_employees():
    """To print all the employees and their information."""
    # looping in my employee list to print the employee information
    for employee in employee_list:
        print(f"Employee name :\n{employee.name_display()},\nSalary:{employee.salary}$/h,"
              f"\nDOB: {employee.date_of_birth}, \nDOH: {employee.hired_since}"
              f"\nRole: {employee.job_title}\n")


# get_all_employees()

get_quarterly_reports = [
    AccountingReport(employee_list),
    StaffingReport(employee_list),
    ScheduleReport(employee_list)
]


# Since the report specifics are in different class and have their own parameters
# It's much easier to loop through the report by changing the method and giving them the same name
# Then when we call that print report, we cleaned our for loop to be much easier without changing much 🤯
# Now if the report need some modification, we can just go in the subclass in reports and twik individually
# It's called polymorphism
for report in get_quarterly_reports:
    report.print_report()


f_name = input("Enter employee first name(s) : ")
l_name = input("Enter employee last name(s) : ")
salary = input("Enter employee hourly rate : $")
date_of_birth = input("Enter employee birthdate : ")
hired_since = input("Enter employee first day of work : ")

# Should be CustomJobTitle from input
job_title = input("Please specify the title of the employee: ")
# CustomJobTitle(f_name, l_name, salary, date_of_birth, hired_since, shift)
shift = CustomShift()

