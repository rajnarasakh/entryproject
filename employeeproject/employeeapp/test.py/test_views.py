from django.test import SimpleTestCase, Client
from django.urls import reverse,resolve
from employeeapp.models import Employee

class TestViews(TestCase):
    def testviewshome(self):
        client=Client()
        response=client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')