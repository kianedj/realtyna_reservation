# Generated by Django 4.1.7 on 2023-03-17 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0009_alter_room_hotel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HotelGuest',
        ),
        migrations.DeleteModel(
            name='ReservationList',
        ),
    ]
