from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")
class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField(label='Your email')
    message = forms.CharField(label='Your message', widget=forms.Textarea)
    #Botcatcher field to prevent spam bots from submitting the form. This field is hidden and should be left empty by human users.
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
    def clean_botcatcher(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")
    
