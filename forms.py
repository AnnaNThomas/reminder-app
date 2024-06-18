from django import forms
from .models import register,dt
 
class registerform(forms.ModelForm):
    class Meta:
        model=register
        fields=('firstname','lastname','email','mobile','gender','dob','password')
        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

# class dtform(forms.ModelForm):
#     class Meta:
#         model=dt
#         fields=('date','time','image')
#         widgets={
#             'date':forms.TextInput(attrs={'class':'form-control'}),
#             'time':forms.TextInput(attrs={'class':'form-control'}),
#             'image':forms.FileInput(attrs={'class':'form-control'}),
#         }