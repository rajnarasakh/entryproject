from django.test import TestCase
from employeeapp.models import Employee


class TestModel(TestCase):
    def testModelEmployee(self):
        emp = Employee.objects.create(nam='zzz')
        print(emp)
        self.assertIsInstance(emp,Employee)