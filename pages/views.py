from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):

    return HttpResponse ("Helloworld")
def about_page_view(request):
     context = {"name": "Shagustha" }
     return render(request,"about.html", context) 
