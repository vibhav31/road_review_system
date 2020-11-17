from django.db import models
import random
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext  = os.path.splitext(base_name)
    return name,ext

def upload_roadimage(instance,filename):
    new_filename  =random.randint(1,999999999)
    name,ext      =get_filename_ext(filename)
    final_filename=f"{new_filename},{ext}"
    return 'roadimage/'+f"{new_filename}/{final_filename}"

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=80)
    category_image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=20,unique=True)
    subcategory_image=models.ImageField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.category_name.category_name+ " - " +self.subcategory_name

class Type(models.Model):
    type_name =models.CharField(max_length=80)
    type_image =models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.type_name

class Road(models.Model):
    title           =models.TextField(max_length = 60)
    type_name       =models.ForeignKey(Type, on_delete=models.CASCADE)
    subcategory_name=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description     =models.TextField(max_length=100)
    image           =models.ImageField(unique=True, upload_to=upload_roadimage)
    slug            =models.SlugField(max_length = 40,blank=True,null=True)
    active          =models.BooleanField(default=True)
    tender_amount   =models.DecimalField(max_digits=15,decimal_places=2)
    quality         =models.CharField(max_length=10)

    def __str__(self):
        return self.title
class Review(models.Model):
    reviewedby = models.EmailField(max_length=50)
    roadid  = models.IntegerField()
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['reviewedby' ,'roadid'],name='ReviewedConstraint')]

    def __str__(self):
        return self.reviewedby
