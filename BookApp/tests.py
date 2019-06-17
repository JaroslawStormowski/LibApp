from django.test import TestCase
from .scripts import Script
# Create your tests here.


class test_Script(TestCase):

    def test_transfer_data(self):

        result = Script.transfer_data()
        print(result)

