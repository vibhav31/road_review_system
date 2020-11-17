from django.contrib import admin
from .models import Road , Type , Category , SubCategory,Review

# Register your models here.
admin.site.register(Road)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Review)

