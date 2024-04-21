from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    path('goods-record', views.goodslisting, name="goodslisting"),
    path('goods-add', views.add, name="add"),
    re_path(r'^update/(?P<goodsId>[0-9a-f-]{36})/$', views.update, name='update'),
    # re_path(r'^delete/(?P<goods_id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.delete_goods, name="delete_goods"),
    re_path(r'^delete/(?P<goods_id>[0-9a-f-]{36})/$', views.delete_goods, name="delete_goods"),
]   