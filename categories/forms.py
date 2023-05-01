from django import forms
from .models import Donor, ChildrenHome

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'email', 'address', 'county']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'id': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'id': 'last_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address', 'id': 'address'}),
            'county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'County', 'id': 'county'}),
        }



class ChildrenHomeForm(forms.ModelForm):
    class Meta:
        model = ChildrenHome
        fields = ['name', 'category', 'location', 'county', 'email', 'phone', 'address', 'num_children', 'age_group', 'about_us', 'main_challenges', 'activities', 'image1', 'image2', 'image3', 'management_details', 'management_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Children Home'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location of Children Home'}),
            'county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter County of Children Home'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email of Children Home'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number of Children Home'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address of Children Home'}),
            'num_children': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Children'}),
            'age_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age Group of Children'}),
            'about_us': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter About Us information'}),
            'main_challenges': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Main Challenges faced by the Children Home'}),
            'activities': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Activities offered by the Children Home'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'management_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Management Details of Children Home'}),
            'management_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)