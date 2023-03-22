# Since main will not be used for printing reports, we moved them here

class ReportFormat:
    # Since the employee list used for reporting is on another page,
    # I need a way to import that list
    # from main import employee_list is good for now but might complicate things in the future
    # This reporting file will be too dependent on the main if we do that
    # It will make the code rigid in the long run
    # Therefore, using the __init__ method then add a required attibute, which is a mandatory list
    # This is called dependency injection to prevent coupling (miantehatra be @ main)
    def __init__(self, emp_list):
        # To make this report, we need a list
        # Adding the list in the init method will make it mandatory when we use this class
        self.emp_list = emp_list


class AccountingReport(ReportFormat):
    def print_report(self):
        """Gives a list of the employees and their respective salary."""
        print("Accounting report")
        print("===================")
        for employee in self.emp_list:
            print(f"{employee.name_display()} | {employee.salary}$/h\n")


class StaffingReport(ReportFormat):
    def print_report(self):
        """Gives a list of the employees and their respective roles."""
        print("Staffing report")
        print("===================")
        for employee in self.emp_list:
            print(f"{employee.name_display()} | {employee.job_title}\n")


class ScheduleReport(ReportFormat):
    def print_report(self):
        """Gives a list of the employees and their shedule."""
        print("Scheduling report")
        print("===================")
        for employee in self.emp_list:
            print(f"{employee.name_display()} | {employee.shift.get_shift()}\n")