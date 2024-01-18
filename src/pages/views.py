from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): 
    return render(request, "contact.html", {})
    #return HttpResponse("<h1>Contact Page</h1>")

def about_view(request, *args, **kwargs): 
    return render(request, "about.html", {})
    #return HttpResponse("<h1>About Page</h1>")

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {}) 
    #return HttpResponse("<h1>Social Page</h1>")