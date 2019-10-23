from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from store.models import Product


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})
