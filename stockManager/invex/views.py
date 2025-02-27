from django.shortcuts import render,redirect,HttpResponse
import datetime
from . models import Product
import os
from . models import picfile
# Create your views here.
def addProduct(request):
    return render(request, 'addProduct.html')

def allProducts(request):
    products = Product.objects.all()
    return render(request, 'allProducts.html', {'products': products})

def editProduct(request):
    return render(request, 'editProduct.html')

def loginPage(request):
    return render(request, 'loginPage.html')

def productDetails(request):
    products = Product.objects.all()
    return render(request, 'productDetails.html',{'products': products})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            return redirect('productDetails')
    return render(request, 'loginPage.html')

def add(request):
    if request.method == 'POST' and request.FILES.get('image'):
        name = request.POST.get('product_name')
        sku = request.POST.get('sku')
        price = request.POST.get('price')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        supplier = request.POST.get('supplier')
        date = datetime.date.today()

        file = request.FILES['image']
        filename = file.name
        upload_dir = 'invex/static/upload/'

        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, filename)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image_url = f"upload/{filename}" if file else ""
        if(checkExtension(filename)):
            pic = picfile(fname=filename, furl=image_url)
            pic.save()
            product = Product(
            name=name, sku=sku, price=price, category=category,
            quantity=quantity, status=status, supplier=supplier, date=date,
            image_url=image_url
            )
            product.save()
        else:
            return HttpResponse("""
            <script>
            alert('Invalid File Format. Please upload only images (jpg, jpeg, png, gif)');
            window.location.href = 'addProduct';
        </script>
        """)
        return redirect('productDetails')
    return render(request, 'addProduct.html')


def checkExtension(filename):
    ext = filename.split('.')[-1]
    if ext.lower() in ['jpg', 'jpeg', 'png', 'gif']:
        return True
    return False

def hide(request,id):
    product = Product.objects.get(id=id)
    product.isVisible = False
    product.save()
    return redirect('productDetails')

def show(request,id):
    product = Product.objects.get(id=id)
    product.isVisible = True
    product.save()
    return redirect('productDetails')


def handle_uploaded_file(file, file_path):
    upload_dir = 'store/static/upload/'
    
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)