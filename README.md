**Django_web_application**

**Step 1: Set Up Django Project and App**
Open a terminal in the directory where you want to create your project.

Run the following commands:


Copy code
_django-admin startproject myproject
cd myproject
python manage.py startapp myapp_

**Step 2: Define Model**
In myapp/models.py, define your model. For example:

python
Copy code
# myapp/models.py
_from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name_
Run migrations:
_
python manage.py makemigrations
python manage.py migrate
_
**Step 3: Create Views**
In myapp/views.py, create a view to fetch data from the database:

# myapp/views.py
_from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all()
    return render(request, 'myapp/index.html', {'items': items})_
**Step 4: Templates**
Create a templates folder inside the myapp folder.

Inside myapp/templates/myapp, create index.html:


<!-- myapp/templates/myapp/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Items List</title>
    <style>
        body {
            background-image: url('/static/background.jpg');
            background-size: cover;
        }
    </style>
</head>
<body>
    <h1>Items</h1>
    <ul>
        {% for item in items %}
            <li>{{ item.name }} - {{ item.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>
**Step 5: URL Configuration**
In myapp/urls.py, define a URL pattern:


# myapp/urls.py
_from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]_
Include this URL configuration in the main project's urls.py:


# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
**Step 6: Serve Static Files (for the background image)**
Create a static folder inside the myapp folder.
Place your background image (e.g., background.jpg) in the static folder.
**Step 7: Run Development Server**
Run the development server:


python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to see the webpage with your data and background image.
