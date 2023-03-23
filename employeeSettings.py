# Starting a BLUEPRINT(aka CLASS) for an Employee
class EmployeeProfile:
    # to initialize and identify what should go in an employee file, we need "self"
    # it would take the value assigned (aka OBJECT) to it when we call this method afterwards
    # Add with the self what other class variables (aka ATTRIBUTES) are required to make an employee in my program
    def __init__(self, f_name, l_name, salary, date_of_birth, hired_since, shift):
        """Specify the name, the salary upon hiring, DOB and first day of work."""
        # self.name means the name of the new object (aka new employee when we use the class Employee in practice)
        # will be defined by the name we will associate with it
        # the new object will be required to have name, salary, date_of_birth, hired_since when created
        self._f_name = f_name
        self._l_name = l_name
        self.salary = salary
        self.date_of_birth = date_of_birth
        self.hired_since = hired_since
        self.shift = shift

    # Since we are using this method now to access the full name of the employee in reports
    # It's not necessary to access f_name & l_name for the user
    # Specify it once then the program will do the formating through this method
    # To specify that it's "hidden" we put _ before the attribute
    def name_display(self):
        return f"{self._f_name} {self._l_name}"

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


# If we put the job_title in the EmployeeProfile class, that would make me do double the work
# Because I would have to type "Clerk" 3 times for example if I have 3 clerks
# Because if the title "Clerk" changes in the future, I would have to change it 3 times
# Manager as a role will be a subclass of EmployeeProfile
# Since all the manager will have all the information in EmployeeProfile, but not all EmployeeProfile will be "Manager"
class TeamManager(EmployeeProfile):
    job_title = "Team Manager"
    # Here we will add all the info or tools required for the role "Manager"
    # it applies to all the manager subsequently


class Clerk(EmployeeProfile):
    job_title = "Clerk"


class Pharmacist(EmployeeProfile):
    job_title = "Pharmacist"


class CustomJobTitle(EmployeeProfile):
    def addJobTitle(self, title):
        self.job_title = title