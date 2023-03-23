# To test on Terminal by myself
# Type : python3 -m unittest
# Then this followong code will run

import unittest
from employeeSettings import EmployeeProfile, CustomJobTitle



# Each test class need to begin by "Test"
# First value of attribute needs to inherit from unittest.TestCase to be able to work
# Plenty of assert methods are available
# Since we only want to test the name display, we don't need the other values, so we mark None and 0 instead
class TestEmployee(unittest.TestCase):
    def test_name_display(self):
        employee = EmployeeProfile("Mirana", "Ravao", 0, None, None, None)
        self.assertEqual(employee.name_display(), "Mirana Ravao")

    # # Testing if a raise salary fucntion works
    # def test_raise_salary(self):
    #     employee = EmployeeProfile("", "", 2000, None, None, None)
    #     employee.raise_salary(300)
    #     self.assertEqual(employee.salary, 2300)

class TestCustomJobTitleEmployee(unittest.TestCase):
    def test_Custom_Job_Title(self):
        employee = CustomJobTitle(None, None, 0, None, None, None)
        employee.addJobTitle("Consultant")
        self.assertEqual(employee.job_title, "Consultant")

    def test_Failed_Custom_Job_Title(self):
        employee = CustomJobTitle(None, None, 0, None, None, None)
        employee.addJobTitle("Assistant Manager")
        self.assertNotEqual(employee.job_title, "Manager")

unittest.main()