from django.forms import ModelForm
from .models import Donor, ChildrenHome




class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = [
            "first_name",
            "last_name",
            "email",
            "address",
            "county",
        ]

class ChildrenHomeForm(ModelForm):
    class Meta:
        model = ChildrenHome
        fields = '__all__'