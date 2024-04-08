
from django.contrib import admin
from django.urls import path, re_path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/customers/$', views.customers_list),
    re_path(r'^api/customers/(?P<pk>[0-9]+)$', views.customer_details),
    re_path(r'^api/products/$', views.products_list),
    re_path(r'^api/products/(?P<pk>[0-9]+)$', views.product_details),
]
