from django.urls import include,path
from . import views

urlpatterns = [
    path("", views.Home_Page, name="Home_Page"),
    path("user_login/", views.User_Login, name="users_login"),
    path("service_center_login/", views.Service_Center_Login, name="service_login")
]
