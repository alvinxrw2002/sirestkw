from django.contrib import admin
from promo.models import *

# Register your models here.
admin.site.register(Promo)
admin.site.register(MinimumTransactionPromo)
admin.site.register(SpecialDayPromo)