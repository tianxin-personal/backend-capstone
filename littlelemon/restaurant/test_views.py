from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token  # Import Token model
from django.contrib.auth.models import User

from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a user and obtain an authentication token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Milk", price=3, inventory=100)
        Menu.objects.create(title="Chocolate", price=10, inventory=100)

    def test_get_all(self):
        # Create an instance of the APIClient
        client = APIClient()

        # Add the token to the client's Authorization header for authentication
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Issue a GET request to the view's URL
        url = '/restaurant/menu/'  # Replace this with the actual URL path for your view
        response = client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data contains the expected number of menu items
        self.assertEqual(len(response.data), 3)

        # Check that the response data contains the expected menu items
        expected_menu_titles = ["IceCream", "Milk", "Chocolate"]
        for menu_item, expected_title in zip(response.data, expected_menu_titles):
            self.assertEqual(menu_item['title'], expected_title)
