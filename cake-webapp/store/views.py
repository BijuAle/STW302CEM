from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from store.models import Product, ShoppingCart
from store.forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list-products')
    else:
        form = RegistrationForm()
    return render(request, 'store/register.html', {'form': form})

def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/product_list.html', context)

def show(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'store/product.html', context)


def cart(request):
    context = {
        'items': [],
        'subtotal': 1.0,
        'tax_rate': int(ShoppingCart.TAX_RATE * 100.0),
        'tax_total': 2.0,
        'total': 3.0,
    }
    return render(request, 'store/cart.html', context)
