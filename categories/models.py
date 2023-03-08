from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=256)
    description=models.TextField(max_length=256,blank=True)

    def _str_(self):
        return self.name
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'