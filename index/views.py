from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {'message': 'Welcome to the Django Project'})
