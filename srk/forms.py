from django import forms
from django.forms import widgets  

from .models import Employee


MONTHS = {
    1:('Январь'), 2:('Февраль'), 3:('Март'), 4:('Апрель'),
    5:('Май'), 6:('Июнь'), 7:('Июль'), 8:('Август'),
    9:('Сентябрь'), 10:('Октябрь'), 11:('Ноябрь'), 12:('Декабрь')
}

class emplForm(forms.ModelForm):
  
    class Meta:
        model = Employee
        fields = ([
        'name', 
        'surname', 
        'birth', 
        'age', 
        'position', 
        'udalenka', 
        'gorod',
        'ulitsa',
        'dom',
        'kvartira',
        'cover',])

        widgets = {
        'birth': widgets.SelectDateWidget(
          years = range(1960, 2021),
          months = MONTHS
        ),
        'name' : forms.TextInput(attrs={'class':'input', 'size':'25', 'placeholder':'Имя'}),
        'surname' : forms.TextInput(attrs={'class':'input', 'size':'25', 'placeholder':'Фамилия'}),
        'gorod' : forms.TextInput(attrs={'class':'input', 'size':'25','placeholder':'Город'}),
        'ulitsa' : forms.TextInput(attrs={'class':'input', 'size':'25', 'placeholder':'Улица'}),
        'dom' : forms.NumberInput(attrs={'class':'input', 'size':'25', 'placeholder':'Дом'}),
        'kvartira' : forms.NumberInput(attrs={'class':'input', 'size':'25', 'placeholder':'Квартира'}),
        'age' : forms.NumberInput(attrs={'class':'input', 'size':'25', 'placeholder':'Возраст'}),
        
        }

         
        