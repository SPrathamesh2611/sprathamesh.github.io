from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image1', 'image2', 'image3', 'image4', 'video', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the 'required' attribute to False for optional fields
        self.fields['image2'].required = False
        self.fields['image3'].required = False
        self.fields['image4'].required = False
        self.fields['video'].required = False

# class ContactForm(forms.Form):
#     class Meta:
#         model = Project
#         fields = ['name', 'email', 'subject', 'message']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)