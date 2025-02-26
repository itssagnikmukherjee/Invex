from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.allProducts),
    path('addProduct',views.addProduct),
    path('allProducts',views.allProducts),
    path('editProduct',views.editProduct),
    path('loginPage',views.loginPage),
    path('productDetails',views.productDetails),
]