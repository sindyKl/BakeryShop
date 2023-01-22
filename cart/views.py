from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm


def cart(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart.html', {'cart': cart, 'title': 'Shopping Cart'})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(product=product, quantity=cleaned_data['quantity'])
    return redirect('cart')


def cart_update(request, product_id, sign):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, sign=sign)
    return redirect('cart')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart')
    