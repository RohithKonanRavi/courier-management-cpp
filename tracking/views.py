from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from tracking.models import Tracking
from goods.models import goods
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

def ship_product(request, goods_id):
    goods_item = get_object_or_404(goods, pk=goods_id)
    tracking = Tracking(
        goods=goods_item,
        location="Shipping location",
        tracking_description="Product shipped",
    )
    tracking.save()

def update_tracking(request, id, new_location, new_description):
    tracking = get_object_or_404(Tracking, id=id)
    tracking.location = new_location
    tracking.tracking_description = new_description
    tracking.tracking_date = datetime.now()
    tracking.save()

def deliver_product(request, id):
    update_tracking(request, id, "Delivery location", "Product delivered")

def index(request):
    return render(request,'login.html')

def trackinglisting(request):
    try:
        trackinglist = Tracking.objects.select_related('goods').all()
    except Tracking.DoesNotExist:
        messages.add_message(request, messages.ERROR, "Database error: Tracking does not exist")
        trackinglist = []

    context = {
        "trackinglist": trackinglist,
        'heading': "All Tracking Record"
    }
    return render(request,'tracking-record.html', context)

def trackingsearch(request):
    context = {}
    if (request.method == "POST"):
        goods_id = request.POST['tracking_id']
        trackinglist = Tracking.objects.select_related('goods').filter(goods__goods_id=goods_id)

        context = {
            "trackinglist": trackinglist,
            'heading': "All Tracking Record"
        }
    return render(request,'tracking-search.html', context)

def update(request, id):
    context = {
        "fn": "update",
        "trackingdetails": Tracking.objects.get(id=id),
        "heading": 'Tracking Update',
    }
    if (request.method == "POST"):
        tracking_date_str = request.POST['tracking_date']
        tracking_date = datetime.strptime(tracking_date_str, '%m/%d/%Y %H:%M')
        tracking = Tracking.objects.get(id=id)
        tracking.tracking_date = tracking_date
        tracking.tracking_description = request.POST['tracking_description']
        tracking.location = request.POST['location']
        tracking.save()
        context["trackingdetails"] = tracking
        messages.add_message(request, messages.INFO, "Tracking updated succesfully !!!")
        return redirect('trackinglisting')
    else:
        return render(request, 'tracking-add.html', context)

def add(request, goodsId):
    context = {
        "fn": "add",
        "goodsId": goodsId,
        "heading": 'Add Tracking'
    }
    if (request.method == "POST"):
        tracking_date_str = request.POST['tracking_date']
        tracking_date = datetime.strptime(tracking_date_str, '%m/%d/%Y %H:%M')
        tracking = Tracking(
            goods_id=request.POST['goods_id'],
            tracking_date=tracking_date,
            tracking_description=request.POST['tracking_description'],
            location=request.POST['location'],
        )
        tracking.save()
        return redirect('trackinglisting')
    return render(request, 'tracking-add.html', context)

def delete(request, id):
    print(f"Deleting tracking record with ID: {id}")
    try:
        tracking = Tracking.objects.get(id=id)
        tracking.delete()
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, "Tracking record does not exist")
    return redirect('trackinglisting')