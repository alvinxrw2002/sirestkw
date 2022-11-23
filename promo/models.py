from django.db import models

# Create your models here.
class Promo(models.Model):
    promo_id = models.CharField(max_length=25, primary_key=True)
    promo_type = models.CharField(max_length=50)
    promo_name = models.CharField(max_length=25)
    discount = models.IntegerField()

class MinimumTransactionPromo(models.Model):
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE, primary_key=True)
    minimum_transaction = models.IntegerField()

class SpecialDayPromo(models.Model):
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE, primary_key=True)
    promo_date = models.DateField()