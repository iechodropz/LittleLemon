from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
