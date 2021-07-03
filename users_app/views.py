from django.shortcuts import redirect, render, HttpResponse
from .models import User

# Create your views here.

def index(request):
    context = {
    "users" : User.objects.all(),
    "all_fields" : User._meta.get_fields()
        }
    return render(request, 'index.html', context)

def add_user(request):
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email_address = request.POST['email'], age = request.POST['age'])
    return redirect('/')
