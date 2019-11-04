from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.views
import store.api_views


# default: "Django Administration"
admin.site.site_header = 'Cake WebStore'
# default: "Site administration"
admin.site.index_title = 'Features area'
# default: "Django site admin"
admin.site.site_title = 'HTML title from adminsitration'


urlpatterns = [

    # Show index page / login
    path(r'', store.views.index, name='index'),

    #logout
    path(r'logout', store.views.logout, name='logout'),

    # Show page: User Registration
    path(r'register', store.views.register, name='register'),

    # Add to Cart
    path(r'add_to_cart/<pk>/', store.views.addToCart, name='addToCart'),

    # Add to Cart (from view - Order Summary)
    path(r'addToCart_os/<pk>/', store.views.addToCart_OS, name='addToCart_OS'),

    # Remove from Cart
    path(r'remove_from_cart/<pk>/', store.views.removeFromCart, name='removeFromCart'),

    # Remove from Cart (from view - Order Summary)
    path(r'remove_from_cart_os/<pk>/', store.views.removeFromCart_OS, name='removeFromCart_OS'),

    # Show Order Summary - Cart
    path(r'order_summary/', store.views.getCart, name='order_summary'),

    # Show all cakes
    path(r'list', store.views.CakeListView.as_view(), name='listAllCakes'),
    
    # Show individual cake
    path('products/<pk>/', store.views.CakeSingleView.as_view(), name='showCake'),

    # Stats
    path('api/v1/products/<int:id>/stats', store.api_views.ProductStats.as_view()),

    # Retrieve all cakes
    path('api/v1/products/', store.api_views.ProductList.as_view()),

    # Create a cake
    path('api/v1/products/new', store.api_views.ProductCreate.as_view()),

    # Retrieve, update, and destroy a cake
    path('api/v1/products/<int:id>/', store.api_views.ProductRetrieveUpdateDestroy.as_view()),

    # Admin dashboard for cake CRUD
    path('admin/', admin.site.urls)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
