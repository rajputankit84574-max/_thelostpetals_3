from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")  

def services(request):
    return render(request, "services.html")

def collections(request):
    return render(request, "collections.html")

def contact(request):
    return render(request, "contact.html")

