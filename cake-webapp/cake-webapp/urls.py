from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.views
import store.api_views


admin.site.site_header = 'My project'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration' # default: "Django site admin"


urlpatterns = [
    path('api/v1/products/', store.api_views.ProductList.as_view()),
    path('api/v1/products/new', store.api_views.ProductCreate.as_view()),
    path('api/v1/products/<int:id>/',
         store.api_views.ProductRetrieveUpdateDestroy.as_view()
         ),
    path('admin/', admin.site.urls),
    path('products/<int:id>/', store.views.show, name='show-product'),
    path('', store.views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
