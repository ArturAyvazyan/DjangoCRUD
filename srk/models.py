from django.db import models
from datetime import datetime, date

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    position_choice = (
        ('Техник','Техник'),
        ('Бухгалтер','Бухгалтер'),
        ('Программист','Программист'),
    )
    age = models.IntegerField(max_length=100)
    position = models.CharField(max_length=100, blank = True, null = True, choices=position_choice)
    udalenka = models.BooleanField(default=False)
    gorod = models.CharField(max_length=100)
    ulitsa = models.CharField(max_length=100)
    dom = models.IntegerField(max_length=100)
    kvartira = models.IntegerField(max_length=100)
    cover = models.ImageField(upload_to='bows/', null = True, blank = True)
    

    def __str__(self): #Что значит такая записть стр
        return self.title
    
    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args,**kwargs)