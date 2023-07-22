from django.test import TestCase

# Create your tests here.
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream",price=80,inventory=100)
        self.assertEqual(f'{item.title} : {item.price}',"IceCream : 80")

        