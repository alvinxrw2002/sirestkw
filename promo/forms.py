from django.forms import *

class DateInput(DateInput):
    input_type = 'date'

class SpecialDayPromoForm(Form):
    nama = CharField(max_length=25, label="Nama Promo", widget=TextInput(attrs={'class': 'form-control'}))
    diskon = IntegerField(min_value=0, max_value=100, label="Diskon", widget=NumberInput(attrs={'class': 'form-control'}))
    tanggal = DateField(label="Tanggal Berlangsung", widget=DateInput(attrs={'class': 'form-control'}))

class MinimumTransactionPromoForm(Form):
    nama = CharField(max_length=25, label="Nama Promo", widget=TextInput(attrs={'class': 'form-control'}))
    diskon = IntegerField(min_value=0, max_value=100, label="Diskon", widget=NumberInput(attrs={'class': 'form-control'}))
    transaksi = IntegerField(min_value=0, label="Minimum Transaksi", widget=NumberInput(attrs={'class': 'form-control'}))