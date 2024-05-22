from django import forms
from .models import VehicleImage

#creating the form for the user to upload the image of a vehicle from the VehicleImage model
class VehicleImageForm(forms.ModelForm):
    class Meta:
        model = VehicleImage
        fields = ['image', 'age', 'city']
