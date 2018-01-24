from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'store/$', views.index, name='index'),
    url(r'store/buy', views.buy, name='buy'),
    url(r'store/checkout', views.checkout, name='checkout'),
    url(r'store/reset', views.reset, name='reset')
]