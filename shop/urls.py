from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('contact/done/', views.contact_done, name='contact_done'),
    path('about/', views.about, name='about'),
    path('shop/', views.Shop.as_view(), name='shop'),
    path('post/', views.single_post, name='post'),
    path('shop/<slug:slug>/', views.ViewProduct.as_view(), name='single_product'),
    path('category/<int:category_id>/', views.CategoryView.as_view(), name='category'),
]
