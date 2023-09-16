from django.shortcuts import render

# Create your views here.
def home(request):
    """The home page for seaq"""
    return render(request, 'pages/home.html')

def violations(request):
    return render(request, 'pages/violations.html')

def purifier(request):
    return render(request, 'pages/purifier.html')

def events(request):
    return render(request, 'pages/events.html')