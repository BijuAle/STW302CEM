from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.views.generic import ListView, DetailView
from django.utils import timezone

from store.models import Product, OrderItem, Cart
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

# Replaced by CakeListView()
def listAllCakes(request):
    if not request.user.is_authenticated:
        return redirect('index')
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/product_list.html', context)

# Replaced by CakeSingleView()
def showCake(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'store/product.html', context)

class CakeListView(ListView):
    model = Product
    template_name = 'store/product_list.html'

class CakeSingleView(DetailView):
    model = Product
    template_name = 'store/product.html'

def addToCart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Cart.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__pk=item.pk).exists():
            order_item.qty += 1
            order_item.save()
            messages.info(request, 'This item quantity was updated.')
            return redirect('showCake', pk=item.pk)
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart.')
            return redirect('showCake', pk=item.pk)

    else:
        ordered_date = timezone.now()
        order = Cart.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart.')
        return redirect('showCake', pk=item.pk)

def removeFromCart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Cart.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.qty > 1:
                order_item.qty -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect('showCake', pk=item.pk)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('showCake', pk=item.pk)
    else:
        messages.info(request, "You do not have an active order")
        return redirect('showCake', pk=item.pk)


def getCart(request):
    if not request.user.is_authenticated:
        return redirect('index')
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/product_list.html', context)