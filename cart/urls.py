from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('update/<int:product_id>/<str:sign>', views.cart_update, name='cart_update')
]