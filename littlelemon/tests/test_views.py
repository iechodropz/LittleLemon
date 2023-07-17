from django.test import TestCase, Client
from django.contrib.auth.models import User
from restaurant.models import Menu
from django.core.serializers import serialize
import json


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Burger", price=120, inventory=50)
        Menu.objects.create(title="Pizza", price=200, inventory=30)

        self.create_authenticated_user(username="testuser", password="testpass")

    def test_getall(self):
        menu_data = Menu.objects.all()
        menu_data_serialized = serialize("json", menu_data)
        menu_data_deserialized = json.loads(menu_data_serialized)
        fields_values = [
            {"id": item["pk"], **item["fields"]} for item in menu_data_deserialized
        ]

        response = self.client.get("/restaurant/menu/")
        response_deserialized = json.loads(response.content.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_deserialized, fields_values)

    def create_authenticated_user(self, username, password):
        User.objects.create_user(username=username, password=password)
        self.client = Client()
        self.client.login(username=username, password=password)
