from django.contrib import admin

from .models import User, Profile, Donor, Recipient
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Donor)
admin.site.register(Recipient)