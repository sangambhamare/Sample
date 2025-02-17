# Install necessary packages
# pip install django gunicorn

# views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi")

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
