from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    # Other URL patterns of your project
    path('homepage/', views.homepage, name='homepage'),
    # Other URL patterns of your project
]
