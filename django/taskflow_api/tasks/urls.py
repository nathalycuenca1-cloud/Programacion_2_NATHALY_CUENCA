from django.urls import path
from . import views

app_name = "tasks" 

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("sobre-nosotros/", views.sobre_nosotros, name="sobre_nosotros"),
    path("greeting/<str:nombre>/", views.greeting, name="greeting"),
    path("destination/<str:titulo>/<str:nombre>/<str:cargo>", views.destination, name="destination"),
    path("area/<int:base>/<int:altura>", views.area, name="area"),
    path("leads-like", views.leads_like, name="leads_like"),
    ]
