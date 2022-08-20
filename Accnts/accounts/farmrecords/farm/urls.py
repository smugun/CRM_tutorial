from django.urls import path
from .views import addUSer, Home, records, register, table, image

urlpatterns = [
    path('/', Home, name='home'),
    path('', records, name='records'),
    path('register/', register, name='register'),
    path('table/', table, name='table'),
    path('image/', image, name='image'),
    path('addUser/', addUSer, name='addUser')
]
