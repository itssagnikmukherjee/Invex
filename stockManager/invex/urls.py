from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.allProducts, name='allProducts'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('allProducts', views.allProducts, name='allProducts'),
    path('editProduct', views.editProduct, name='editProduct'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('productDetails', views.productDetails, name='productDetails'),
    path('login', views.login, name='login'), 
    path('add',views.add, name='add'),
    path('hide/<int:id>/', views.hide, name='hide'),
    path('show/<int:id>/', views.show, name='show'),
]