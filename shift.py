# Composition: Each employee will have a shift and a shift will be assigned to an employee
# Instead of creating one shift for each employee, we generalize and create them separately
# Just like we did for the name display
import datetime


class Shift:
    # this method doesn't need inputs bc each shift will have a different time for start and end
    def get_shift(self):
        return f"{self.start_time:%H:%M} to {self.end_time:%H:%M}"


class MorningShift(Shift):
    start_time = datetime.time(7, 30)
    end_time = datetime.time(18, 00)


class NightShift(Shift):
    start_time = datetime.time(18, 00)
    end_time = datetime.time(7, 30)


class CustomShift(Shift):
    start_time = input("What time does the employee starts working? HH:MM ")
    end_time = input("What time does the employee finishes work? HH:MM ")