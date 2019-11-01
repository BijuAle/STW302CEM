from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from store.models import Product, ShoppingCart
from store.forms import RegistrationForm, LoginForm


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('listAllCakes')
            else:
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'store/index.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('listAllCakes')
    form = RegistrationForm()
    return render(request, 'store/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('index')


def listAllCakes(request):
    if not request.user.is_authenticated:
        return redirect('index')
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/product_list.html', context)


def showCake(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'store/product.html', context)


def cart(request):
    if not request.user.is_authenticated:
        return redirect('index')
    context = {
        'items': [],
        'subtotal': 1.0,
        'tax_rate': int(ShoppingCart.TAX_RATE * 100.0),
        'tax_total': 2.0,
        'total': 3.0,
    }
    return render(request, 'store/cart.html', context)
