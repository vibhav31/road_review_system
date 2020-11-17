from django.contrib import admin
from .models import UserProfile
from .models import GuestEmail
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(GuestEmail)