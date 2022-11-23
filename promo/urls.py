from django.urls import path
from promo.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', daftar_promo, name='daftar_promo'),
    path('/delete/<promo_id>', delete, name='delete'),
    path('/ubah-promo-hari-spesial/<promo_id>', ubah_promo_hari_spesial, name='ubah_promo_hari_spesial'),
    path('/ubah-promo-transaksi-minimum/<promo_id>', ubah_promo_transaksi_minimum, name='ubah_promo_transaksi_minimum'),
    path('/detail/<promo_id>', get_detail, name='get_detail'),
    path('/buat-promo', buat_promo, name="buat_promo"),
    path('/buat-promo-hari-spesial', buat_promo_hari_spesial, name="buat_promo_hari_spesial"),
    path('/buat-promo-minimum-transaksi', buat_promo_minimum_transaksi, name="buat_promo_minimum_transaksi"),
]