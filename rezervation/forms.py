from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class Add_form(forms.Form):
    nazwa = forms.CharField()
    pojemnosc_sali = forms.CharField(max_length=4)
    rzutnik = forms.BooleanField(required=False)

class Delete_form(forms.Form):
    Usuwam = forms.BooleanField(required=False)

class DateRangeForm(forms.Form):
    Rezerwuje = forms.DateField()
    Uwagi = forms.CharField(max_length=500, required=False)

class SearchName(forms.Form):
    Nazwa = forms.CharField(max_length=200, required=False)

class SearchDate(forms.Form):
    Data = forms.DateField(required=False)

class SearchCapacity(forms.Form):
    cap = forms.CharField(label='Pojemność',max_length=4, required=False)

class SearchProjector(forms.Form):
    Rzutnik = forms.BooleanField(required=False)

