from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import *
from . import forms
from django.contrib.auth import login, authenticate 


# Create your views here.
def Home_Page(requests):
    template = get_template("home_page.html")
    context = {
        "author":"Ajith H P"
    }
    return HttpResponse(template.render(context))


def User_Login(requests):
    form = forms.UsersForm()
    message = ""
    if requests.method == "POST":
        form = forms.UsersForm(requests.POST)
        if form.is_valid():
            user = authenticate(
                mail_address = form.cleaned_data['mail_address'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(requests, user)
                message = f"Hello {user.mail_address}! You have been logged in"
            else:
                message = "Login Failed!"
    return render(
        requests, 'user_login.html', context={'form':form, 'message':message}
    )
    # users = Users.objects.all().filter(mail_address=mail_address,password=password)
    
    # for user in users:
    #     if user.mail_address==mail_address and user.password==password:
    #         return render(requests, "home_page.html")
    #     else:
    #         return render(requests, "user_login.html")


def Service_Center_Login(requests):
    form = forms.ServiceCenterForm()
    message = ""
    if requests.method == "POST":
        form = forms.ServiceCenterForm(requests.POST)
        if form.is_valid():
            user = authenticate(
                mail_address = form.cleaned_data['mail_address'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(requests, user)
                message = f"Hello {user.mail_address}! You have been logged in"
            else:
                message = "Login Failed!"
    return render(
        requests, 'service_login.html', context={'form':form, 'message':message}
    )