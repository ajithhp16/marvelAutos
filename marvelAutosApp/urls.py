from django.urls import include,path
from .views import Home_Page

urlpatterns = [
    path("", Home_Page, name="Home_Page"),
    path('accounts/', include("django.contrib.auth.urls"))
]
