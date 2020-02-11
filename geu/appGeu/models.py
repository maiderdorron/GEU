from django.db import models


class Bolsa(models.Model):
   nombre = models.CharField(max_length=40)
   precio = models.IntegerField()
   foto = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
   
   def __str__(self):
   	    return self.nombre

class Textil(models.Model):
   nombre = models.CharField(max_length=40)
   precio = models.IntegerField()
   foto = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')

   def __str__(self):
   	    return self.nombre

class Complemento(models.Model):
   nombre = models.CharField(max_length=40)
   precio = models.IntegerField()
   foto = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')

   def __str__(self):
   	    return self.nombre

# Create your models here.
