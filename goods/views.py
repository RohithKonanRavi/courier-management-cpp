from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db import connection, IntegrityError
from django.contrib import messages
from .models import goods  # Ensure this is correctly pointing to your Goods model
from django.shortcuts import render, redirect
from .models import generate_uuid
import uuid

from .models import goods


# Create your views here.
def index(request):
    return render(request, 'login.html')

def goodslisting(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM goods_goods")  # Assuming your table name is correct
    goodslist = dictfetchall(cursor)

    context = {
        "goodslist": goodslist,
        "heading": "All couriers Record"
    }
    return render(request, 'goods-record.html', context)

def getData(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM goods_goods WHERE goods_id = %s", [id])  # Safe parameter passing
    dataList = dictfetchall(cursor)
    return dataList[0] if dataList else {}

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def update(request, goodsId):
    goods_details = getData(goodsId)
    context = {
        "fn": "update",
        "goodsdetails": goods_details,
        "heading": 'Goods Update',
        "goods_types": goods.GOODS_TYPES,  # Assuming your Goods model correctly defines GOODS_TYPES
    }
    if request.method == "POST":
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE goods_goods
            SET goods_name=%s, goods_type=%s, goods_sender_name=%s, goods_sender_mobile=%s, goods_sender_email=%s, goods_sender_address=%s, goods_receiver_name=%s, goods_receiver_mobile=%s, goods_receiver_email=%s, goods_receiver_address=%s, goods_cost=%s, goods_description=%s
            WHERE goods_id=%s
        """, (
            request.POST['goods_name'],
            request.POST['goods_type'],
            request.POST['goods_sender_name'],
            request.POST['goods_sender_mobile'],
            request.POST['goods_sender_email'],
            request.POST['goods_sender_address'],
            request.POST['goods_receiver_name'],
            request.POST['goods_receiver_mobile'],
            request.POST['goods_receiver_email'],
            request.POST['goods_receiver_address'],
            request.POST['goods_cost'],
            request.POST['goods_description'],
            goodsId
        ))
        messages.add_message(request, messages.INFO, "Courier updated successfully !!!")
        return redirect('goodslisting')
    else:
        return render(request, 'goods-add.html', context)


def add(request):
    context = {
        "fn": "add",
        "heading": 'Add Goods',
        "goods_types": goods.GOODS_TYPES,  # Include this to populate the 'goods_type' dropdown
    }
    if request.method == "POST":
        new_goods = goods(
            goods_name=request.POST['goods_name'],
            goods_type=request.POST['goods_type'],
            goods_sender_name=request.POST['goods_sender_name'],
            goods_sender_mobile=request.POST['goods_sender_mobile'],
            goods_sender_email=request.POST['goods_sender_email'],
            goods_sender_address=request.POST['goods_sender_address'],
            goods_receiver_name=request.POST['goods_receiver_name'],
            goods_receiver_mobile=request.POST['goods_receiver_mobile'],
            goods_receiver_email=request.POST['goods_receiver_email'],
            goods_receiver_address=request.POST['goods_receiver_address'],
            goods_cost=request.POST['goods_cost'],
            goods_description=request.POST['goods_description']
        )
        new_goods.save()
        messages.add_message(request, messages.INFO, "Courier added successfully !!!")
        return redirect('goodslisting')
    else:
        return render(request, 'goods-add.html', context)
    
    
from django.shortcuts import get_object_or_404
from .models import goods

def delete_goods(request, goods_id):
    goods_item = get_object_or_404(goods, goods_id=goods_id)
    goods_item.delete()
    return redirect('goodslisting')