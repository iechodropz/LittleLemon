from django.shortcuts import render
from rest_framework import generics


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    pass


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    pass
