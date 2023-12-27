from django.db import models

# Create your models here.

class product_table(models.Model):
    product_name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='static/img/')
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name

class carousels(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='static/img/corusels/')

    def __str__(self):
        return self.title
    
class fixed_images(models.Model):
    photo = models.ImageField(upload_to='static/img/fixed/')
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.photo
    
class about_us(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name