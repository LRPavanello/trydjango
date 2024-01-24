from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_contextC = {
        "my_textc": " This is Contact View ",
        "this_is_truec": True,
        "my_numberc": 2790,
        "my_listc": [123],
        "titlec":" Contact It ",
        "textc": " All of that content is in upper case ",
        "my_htmlc":"<h3>Python and Django WebFramework</h3>",
    }
    return render(request, "contact.html", my_contextC)
    #return HttpResponse("<h1>Contact Page</h1>")

def about_view(request, *args, **kwargs): 
    my_contextA = {
        "my_text": " This is About View ",
        "this_is_true": True,
        "my_number": 2790,
        "my_list": [123, 4235, 312, 5465467, "abc"],
        "title": " About That ",
        "text": " All of that content is in upper case ",
        "my_html":"<h3>Python and Django WebFramework</h3>",
    }
    return render(request, "about.html", my_contextA)
    #return HttpResponse("<h1>About Page</h1>")

def social_view(request, *args, **kwargs):
    my_contextS = {
        "my_text": " This is Contat us",
        "this_is_true": True,
        "my_number": 2790,
        "my_list": [123, 4235, 312, 5465467, "abc"],
        "title": " Contact Us",
        "text": " All of that content is in upper case ",
        "my_html":"<h3>Python and Django WebFramework</h3>"
    }
    return render(request, "social.html", my_contextS) 
    #return HttpResponse("<h1>Social Page</h1>")