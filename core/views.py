from django.shortcuts import render

def index(request):
    return render(request,'core/index.html')

def about(request):
    return render(request,'core/about.html')

def services(request):
    return render(request,'core/services.html')

def contact(request):
    return render(request,'core/contact.html')

def store(request):
    return render(request,'core/store.html')