from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.
class Car(models.Model):

    def __str__(self):
        return self.car_title

    state_choice = (
        ('AL', 'Albania'),
        ('NY', 'NewYork'),
        ('SL', 'Srinlanka'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choice = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Wind Deflector', 'Wind Deflector'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    car_title = models.CharField(max_length=255, default=None)
    state = models.CharField(choices=state_choice, max_length=100, default=None)
    city = models.CharField(max_length=255, default=None)
    color = models.CharField(max_length=255, default=None)
    model = models.CharField(max_length=100, default=None)
    year = models.IntegerField(('year'), choices=year_choice, default=None)
    condition = models.CharField(max_length=255, default=None)
    price = models.IntegerField(default=None)
    description = RichTextField(default=None)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None)
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default=None)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default=None)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default=None)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default=None)
    features = MultiSelectField(choices=features_choice)
    body_style = models.CharField(max_length=255, default=None)
    engine = models.CharField(max_length=255, default=None)
    transmission = models.CharField(max_length=255, default=None)
    interior = models.CharField(max_length=255, default=None)
    miles = models.IntegerField(default=None)
    doors = models.CharField(choices=door_choices, max_length=10, default=None)
    passengers = models.IntegerField(default=None)
    vin_no = models.CharField(max_length=255, default=None)
    milage = models.IntegerField(default=None)
    fuel_type = models.CharField(max_length=50, default=None)
    no_of_owners = models.CharField(max_length=255, default=None)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)





