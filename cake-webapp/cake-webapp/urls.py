from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

import store.views
import store.api_views


admin.site.site_header = 'My project'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration'  # default: "Django site admin"


urlpatterns = [
    #User signup
    url(r'^signup/$', store.views.signup, name='signup'),
        
    #Retrieve all cakes
    path('api/v1/products/', store.api_views.ProductList.as_view()),

    #Create a cake
    path('api/v1/products/new', store.api_views.ProductCreate.as_view()),

    #Retrieve, update, and destroy a cake
    path('api/v1/products/<int:id>/', store.api_views.ProductRetrieveUpdateDestroy.as_view()),

    #Stats
    path('api/v1/products/<int:id>/stats', store.api_views.ProductStats.as_view()),

    #Admin dashboard for cake CRUD
    path('admin/', admin.site.urls),
    
    #Show individual cake
    path('products/<int:id>/', store.views.show, name='show-product'),

    #Show cart
    path('cart/', store.views.cart, name='shopping-cart'),

    #Show all cakes
    path('', store.views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
