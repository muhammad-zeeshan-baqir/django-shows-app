from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    path('shop/', views.shop, name='shop'),
    path('form/', views.form, name='form')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
