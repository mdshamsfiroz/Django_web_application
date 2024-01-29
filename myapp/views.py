# myapp/views.py
from django.shortcuts import render
from .models import Item

def index(request):

    #Item.objects.create(name='Item 1', description='Description for Item 1')
    #Item.objects.create(name='Item 2', description='Description for Item 2')
    items = Item.objects.all()
    return render(request, 'myapp/index.html', {'items': items})
