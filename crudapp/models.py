from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=200)
    details=models.TextField(default='')

    def __str__(self):
        return self.name
        return self.details

"""class Details(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE) 
    text=models.TextField()   

    class Meta:
        verbose_name_plural='Details'

    def __str__(self):
        return self.text"""