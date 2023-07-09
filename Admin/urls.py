
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('Homepage',views.Homepage),
    path('dashboard',views.dashboard),
    path('category',views.category),
    path('Adminapp/Addcategory',views.Addcategory),
    path('Removecat',views.Removecat),
    path('product',views.product),
    path('editproduct',views.editproduct),
    path('modifyproduct',views.modifyproduct),
    path('Removepro',views.Removepro),
    path('user',views.user),
    path('Removeuser',views.Removeuser),
    path('orders',views.orders)
]
