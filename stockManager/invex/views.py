from django.shortcuts import render

# Create your views here.
def addProduct(request):
    return render(request, 'addProduct.html')

def allProducts(request):
    return render(request, 'allProducts.html')

def editProduct(request):
    return render(request, 'editProduct.html')

def loginPage(request):
    return render(request, 'loginPage.html')

def productDetails(request):
    return render(request, 'productDetails.html')
