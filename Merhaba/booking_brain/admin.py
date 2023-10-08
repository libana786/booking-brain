from django.contrib import admin
from .models import Passenger, Booking,Payment, Trash



# Register your models here.
admin.site.register(Passenger)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Trash)
