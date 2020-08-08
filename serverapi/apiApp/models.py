# -*- coding: utf-8 -*-


from django.db import models


class Users(models.Model):
    first_name=models.CharField(max_length=100,default=None)
    last_name=models.CharField(max_length=100,default=None)
    email = models.EmailField(max_length=70, blank=True )
    password=models.CharField(max_length=50,blank=True)

class Store(models.Model):
    name=models.CharField(max_length=100,default=None)
    type = models.CharField(max_length=100,default=None)
    image = models.FileField(upload_to='images/banner',blank=True)

class Categories(models.Model):
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE,default=1)

class Brands(models.Model):
    name=models.CharField(max_length=100)
    banner=models.FileField(upload_to='images/productimages',blank=True)


class Product(models.Model):
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand_id=models.ForeignKey(Brands,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    serial_number=models.IntegerField(default=0)
    product_image = models.FileField(upload_to='images/productimages', blank=True)



class UserCart(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE)


class SoldItems(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    item_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    discount = models.FloatField(null=True, blank=True)

