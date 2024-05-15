from django.db import models

class Category(models.Model):
    catid=models.AutoField(primary_key=True)
    catname=models.CharField(max_length=50,unique=True)
    caticonname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.catname
    
    

class SubCategory(models.Model):
    subcatid=models.AutoField(primary_key=True)
    catname=models.CharField(max_length=50)
    subcatname=models.CharField(max_length=50,unique=True)
    subcaticonname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.subcatname
    
    
class Product(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_title=models.CharField(max_length=50)
    subcatname=models.CharField(max_length=50)
    p_description=models.CharField(max_length=100)
    p_bprice=models.IntegerField()
    p_iconname=models.CharField(max_length=100)    
    info=models.IntegerField()
    image = models.ImageField(upload_to="product_image/",default='default_image.jpg')
    
    def __str__(self):
        return self.p_iconname
    