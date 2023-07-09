
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path('ShowCakes/<id>',views.ShowCakes),
    path('login',views.login),
    path('signup',views.signup),
    path('signout',views.signout),
    path('ViewDetails/<id>',views.viewDetails),
    path('profile/',views.profile),
    path('addToCart', views.addToCart),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('removeItem', views.removeItem),
    path('Search',views.Search),
    path('MakePayment', views.MakePayment),
    path('AddAddress',views.AddAddress),
    path('addremove',views.addremove),
    path('myorders',views.myorders),
    path('passwordchange',views.passwordchange),
    
]
