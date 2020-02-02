from django.forms import ModelForm, TextInput, DateTimeInput, DateTimeField, CharField
from .models import City, Weather, HistoryFilter

import datetime
 
# timenow =  lambda: datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %I:%M %p').replace(' ', 'T')


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={
                'class' : "form-control  mx-sm-3 mb-2", 
                'aria-label'  : "Large",
                'aria-describedby' : "inputGroup-sizing-sm",
                'placeholder': 'City...',
                'name' : 'city',
                'value' : '',
                'id' : 'cities'
                }
        )}


class HistoryFilterForm(ModelForm):
    name = CharField(required=False)
    date_from = DateTimeField(required=False)
    date_to = DateTimeField(initial=datetime.date.today, required=False)

    name.widget = TextInput(attrs={
                    'class' : "form-control col-5 mx-sm-3 mb-2", 
                    'aria-label'  : "Large",
                    'aria-describedby' : "inputGroup-sizing-sm",
                    'placeholder': 'City...',
                    'name' : 'city',
                })

    date_from.widget = DateTimeInput(attrs={
                    'class' : "form-control col-5 mx-sm-3 mb-2", 
                    'name' : 'date_from',
                    'type' : "datetime-local",
                    'value' : '2000-01-01T01:01'
                })

    date_to.widget = DateTimeInput(attrs={
                    'class' : "form-control col-5 mx-sm-3 mb-2", 
                    'name' : 'date_to',
                    'type' : "datetime-local",
                    # 'value' : lambda: datetime.date.today().__str__().replace(' ', 'T')
                })

    class Meta:
        model = HistoryFilter
        fields = ['name', 'date_from', 'date_to']
