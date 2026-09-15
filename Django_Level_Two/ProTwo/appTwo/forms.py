from django import forms
from appTwo.models import User

class NewUser(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    class Meta:
        model = User
        fields = '__all__'