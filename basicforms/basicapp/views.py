from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_page(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something with the form data
            print("Validation successful")
            # CLeaned_data is a dictionary of validated form input fields
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Message: " + form.cleaned_data['message'])
            
    return render(request, 'form.html', {'form': form})