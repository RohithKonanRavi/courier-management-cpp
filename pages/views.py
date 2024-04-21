from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')	
	
def listing(request, goodsId):
    try:
        goodslist =  goods.objects.filter(Q(goods_level=goodsId))
    except Exception as e:
        return HttpResponse('Something went wrong. Error Message : '+ str(e))

    context = {
        "showmsg": True,
        "message": "User Updated Successfully",
        "goodslist": goodslist
    }	
	    # Message according Users Role #
    if(goodsId == "1"):
        context['heading'] = "Goods Report";
    return render(request,'goods-report.html',context)
	