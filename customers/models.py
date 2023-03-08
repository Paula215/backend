from django.db import models

class Customer(models.Model):
    first_name= models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    gender=models.CharField(max_length=4)
    age=models.CharField(max_length=4)
    phone=models.CharField(max_length=9,blank=True)
    email=models.EmailField(unique=True,blank=True)
    address=models.CharField(max_length=256,blank=True)
    dni=models.CharField(max_length=8,blank=True)
    birth_date=models.CharField(max_length=20,blank=True)

    def _str_(self):
        return self.name
    
    class Meta:
        verbose_name='Customer'
        verbose_name_plural='Customers'