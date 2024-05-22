from django.db import models
import random
import string

#Model for the vehicle image model and the fields of data to be saved to db
class VehicleImage(models.Model):
    # saves the image into the vehicle_image directory. Only the path of the image gets saved into the db
    # I chose to do it this way to reduce server processing time but mainly to save on Azure credits lol
    image = models.ImageField(upload_to='vehicle_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    vehicle_type = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=20, unique=True, editable=False)
    insurance_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    #Overrides default save method of parent class Model, creates a ref number if there is none and then calls on save() from Model
    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = self.generate_reference_number()
        super().save(*args, **kwargs)

#function to generate a ref number combining a string with a random 6 digit number
#made static as it doesn't need to be associated with a specific object when generating the ref
    @staticmethod
    def generate_reference_number():
        return 'TCI' + ''.join(random.choices(string.digits, k=6))

#defines a string representation of the VehicleImage object and return a formatted string with the ID, vehicle type, and reference number.
    def __str__(self):
        return f'VehicleImage {self.id} - {self.vehicle_type} - {self.reference_number}'
