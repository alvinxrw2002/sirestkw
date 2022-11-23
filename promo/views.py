from django.shortcuts import render, redirect
from promo.models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from promo.forms import *

# Create your views here.
def buat_promo(request):
    return render(request, "buat-promo.html")

def buat_promo_hari_spesial(request):
    if request.method == 'POST':
        
        form = SpecialDayPromoForm(request.POST)

        if form.is_valid():
            nama_promo = form.cleaned_data['nama']
            diskon = form.cleaned_data['diskon']
            tanggal_berlaku = form.cleaned_data['tanggal']

            all_promo = Promo.objects.all()
            latest_promo = all_promo[len(all_promo) - 1]
            id = latest_promo.promo_id

            newer_id = "PRM-" + str(int(id.strip("PRM-")) + 1)
            new_promo = Promo(promo_id=newer_id, promo_type="Promo Hari Spesial", promo_name=nama_promo, discount=diskon)
            new_promo.save()

            new_sdp = SpecialDayPromo(promo_id = newer_id, promo_date = tanggal_berlaku)
            new_sdp.save()

            return redirect('/daftar-promo')

    else:
        form = SpecialDayPromoForm()

    return render(request, 'buat-promo-hari-spesial.html', {'form': form})

def buat_promo_minimum_transaksi(request):
    if request.method == 'POST':
        
        form = MinimumTransactionPromoForm(request.POST)

        if form.is_valid():
            nama_promo = form.cleaned_data['nama']
            diskon = form.cleaned_data['diskon']
            min_transaksi = form.cleaned_data['transaksi']

            newer_id = "PRM-1"
            all_promo = Promo.objects.all()
            promo_amt = len(all_promo)
            if promo_amt != 0:
                latest_promo = all_promo[promo_amt - 1]
                id = latest_promo.promo_id
                newer_id = "PRM-" + str(int(id.strip("PRM-")) + 1)
            
            new_promo = Promo(promo_id=newer_id, promo_type="Promo Minimum Transaksi", promo_name=nama_promo, discount=diskon)
            new_promo.save()

            new_mtp = MinimumTransactionPromo(promo_id = newer_id, minimum_transaction = min_transaksi)
            new_mtp.save()

            return redirect('/daftar-promo')

    else:
        form = MinimumTransactionPromoForm()

    return render(request, 'buat-promo-minimum-transaksi.html', {'form': form})

def daftar_promo(request):
    all_promo_data = Promo.objects.all()
    context = {
        'promos': all_promo_data
    }
    return render(request, "daftar-promo.html", context)

@csrf_exempt
def get_detail(request, promo_id):
    try:
        promo = SpecialDayPromo.objects.get(pk = promo_id)
        returns = promo.promo_date
    except SpecialDayPromo.DoesNotExist:
        promo = MinimumTransactionPromo.objects.get(pk = promo_id)
        returns = promo.minimum_transaction
    discount = Promo.objects.get(pk = promo_id).discount

    response_dict = {"discount": discount, "returns": returns}
    return JsonResponse(response_dict)

@csrf_exempt
def ubah_promo_hari_spesial(request, promo_id):
    promo_diubah = Promo.objects.get(pk = promo_id)
    promo_diubah.discount = request.POST["diskon"]
    promo_diubah.save()
    return HttpResponse("success")

@csrf_exempt
def ubah_promo_transaksi_minimum(request, promo_id):
    promo_diubah = Promo.objects.get(pk = promo_id)
    promo_hari_diubah = MinimumTransactionPromo.objects.get(pk = promo_id)

    promo_diubah.discount = request.POST["diskon"]
    promo_hari_diubah.minimum_transaction = request.POST["transaksi"]

    promo_diubah.save()
    promo_hari_diubah.save()

    return HttpResponse("success")

def delete(request, promo_id):
    promo_dihapus = Promo.objects.get(pk = promo_id)
    promo_dihapus.delete()
    return HttpResponse("success")