from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.views
import store.api_views


# default: "Django Administration"
admin.site.site_header = 'My project'
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

    # Show cart
    path(r'cart/', store.views.cart, name='shopping-cart'),

    # Show all cakes
    path(r'list', store.views.listAllCakes, name='listAllCakes'),

    # Show individual cake
    path('products/<int:id>/', store.views.showCake, name='showCake'),

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
