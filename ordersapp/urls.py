from django.urls import path, re_path

import ordersapp.views as ordersapp
from ordersapp import views

app_name = 'ordersapp'


urlpatterns = [
    path('', views.OrderList.as_view(), name='orders_list'),
    path('create/', views.OrderItemCreate.as_view(), name='order_create'),
    path('read/<pk>/', views.OrderItemsRead.as_view(), name='order_read'),
    path('update/<pk>/', views.OrderItemUpdate.as_view(), name='order_update'),
    path('delete/<pk>/', views.OrderItemsDelete.as_view(), name='order_delete'),
    path('forming/complete/<pk>/', views.order_forming_complete, name='order_forming_complete'),

    path('product/<pk>/price/', ordersapp.product_price),
]