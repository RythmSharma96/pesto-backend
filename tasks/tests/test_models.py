from django.test import TestCase
from ..models import Task
from django.db import IntegrityError
# Create your tests here.

class ModelsTest(TestCase):
    # def setUpTestData(self):
    #     print("setUpTestData: Run once to set up non-modified data for all class methods.")
    #     pass


    def setUp(self):
        print("setUp: Run once for every test method to set up clean data.")
        pass


    def test_save_without_title(self):
        try:
            Task.objects.create(description='This is a test description')
        except IntegrityError as e:
            print("Integrity error")
            self.assertTrue(e, "NOT NULL constraint failed: tasks_task.title")