# Generated by Django 3.0.7 on 2021-01-26 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='body_style',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(default=None, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo_1',
            field=models.ImageField(blank=True, default=None, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo_2',
            field=models.ImageField(blank=True, default=None, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo_3',
            field=models.ImageField(blank=True, default=None, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, default=None, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_title',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='city',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='condition',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4')], default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='features',
            field=models.CharField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Wind Deflector', 'Wind Deflector')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='interior',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='milage',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='car',
            name='miles',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='no_of_owners',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('AL', 'Albania'), ('NY', 'NewYork'), ('SL', 'Srinlanka')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='vin_no',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=None, verbose_name='year'),
        ),
    ]
