# Generated by Django 5.0.6 on 2024-05-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_Identifier_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleimage',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicleimage',
            name='city',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicleimage',
            name='insurance_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='vehicleimage',
            name='reference_number',
            field=models.CharField(default=0, editable=False, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]