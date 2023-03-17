from django.contrib import admin
from . import models

admin.site.register(models.Guest)
admin.site.register(models.Hotel)
admin.site.register(models.Room)
admin.site.register(models.Reservation)
