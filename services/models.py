from django.db import models
from categories.models import Category

# Create your models here.
class Service(models.Model):
    name= models.CharField(max_length=256,unique=True)
    description=models.TextField(max_length=256,blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    categories=models.ManyToManyField(Category,related_name='service') 
    def _str_(self):
        return self.name

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'


class Image(models.Model):
    image=models.ImageField(upload_to='uploads/')
    service=models.ForeignKey(Service,on_delete=models.CASCADE,related_name='images')
    def _str_(self):
        return self.image.name
    
    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'

    def __str__(self):
        return f'{str(self.image)}'