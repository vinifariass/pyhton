from django.shortcuts import render
from appTwo.models import User
# Create your views here.
from appTwo.forms import NewUser

def index(request):
    return render(request, 'appTwo/index.html')

def users(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
    
    return render(request, 'appTwo/users.html', {'form': form})