from .models import Product, Category
from .forms import ContactForm
from cart.forms import CartAddProductForm
from django.conf import settings
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


class Home(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = Product.objects.all()[:5]
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bakery'
        context['home_active'] = 'active'
        context['images'] = ['images/cake-item1.jpg', 'images/postImg1.jpg', 'images/cake-item4.jpg', 'images/blackforest.jpg', 'images/sprinkleddonuts.jpg', 'images/macarons.jpg']
        return context


class Shop(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        context['title'] = 'Shop'
        context['shop_active'] = 'active'
        return context


class CategoryView(ListView):
    model = Product
    template_name = 'shop/shop.html'  
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['category_id'])  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories    
        context['title'] = 'Shop'
        context['shop_active'] = 'active'
        return context


class ViewProduct(DetailView):
    model = Product
    template_name = 'shop/single_product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product']
        context['cart_product_form'] = CartAddProductForm()
        return context


class Contact(View):
    template_name = 'shop/contact.html'

    def get(self, request):
        form = ContactForm()
        context = {'title': 'Contact us', 'contact_active': 'active', 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            if message and from_email:
                message = f'Name: {name}\nFrom e-mail: {from_email}\n\n{message}'
                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('contact_done')

        context = {'title': 'Contact us', 'contact_active': 'active', 'form': form}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact us'
        context['contact_active'] = 'active'
        return context


def contact_done(request):
    context = {'title': 'Contact us', 'contact_active': 'active'}
    return render(request, 'shop/contact_done.html', context)


def about(request):
    context = {'title': 'About us', 'pages_active': 'active'}
    return render(request, 'shop/about.html', context)


def blog(request):
    context = {'title': 'Blog', 'blog_active': 'active'}
    return render(request, 'shop/blog.html', context)


def single_post(request):
    context = {'title': 'Post', 'pages_active': 'active'}
    return render(request, 'shop/single_post.html', context)


def error_404_view(request, exception):
    return render(request, 'shop/404.html')
