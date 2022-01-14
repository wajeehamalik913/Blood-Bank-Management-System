from django.shortcuts import render
from BBMSAPP.models import User
from django.contrib.auth.hashers import make_password


# Create your views here.
def hello(request):
    return render(request, 'BBMSAPP/signup.html')

def signup(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    password = make_password(password)
    user = User.objects.create(username=name, email=email, password=password)
    if user:
        return render(request, 'BBMSAPP/dashboard.html')

def signin(request):
    email = request.POST['email']
    # password = request.POST['password']
    user = User.objects.filter(email=email).first()
    if user:
        return render(request, 'BBMSAPP/dashboard.html')
    else:
        return render(request, 'BBMSAPP/signin.html')

def dashboard(request):
    return render(request, 'BBMSAPP/dashboard.html')
