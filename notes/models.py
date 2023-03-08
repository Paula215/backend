from django.db import models
from customers.models import Customer

# Create your models here.
class Note(models.Model):
    type=models.CharField(max_length=256)
    name= models.CharField(max_length=256)
    description=models.TextField(max_length=256)
    customer=models.ForeignKey(
        Customer,on_delete=models.CASCADE,
        related_name='notes')

    def _str_(self):
        return self.name
    
    class Meta:
        verbose_name='Note'
        verbose_name_plural='Notes'