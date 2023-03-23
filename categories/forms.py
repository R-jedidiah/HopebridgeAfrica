from django.forms import ModelForm
from .models import Donor




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