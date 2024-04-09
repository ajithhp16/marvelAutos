from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def Home_Page(requests):
    template = get_template("home_page.html")
    context = {
        "author":"Ajith H P"
    }
    return HttpResponse(template.render(context))