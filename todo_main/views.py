from django.http import render

def home(request):
    return request(request, 'home.html')