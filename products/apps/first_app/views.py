from django.shortcuts import render
#look inside models.py for people class
from .models import Product
def index(request):
    Product.objects.create(productName="Mac Laptop", productDescription="Good condition Mac book pro must be sold", productWeight="5 lbs", productPrice="$2000", productCost="$1500", productCategory="Electrionics")
    product = Product.objects.all()
    for pro in product:
        print 'Product Name:', pro.productName,
        print 'Product Description:', pro.productDescription,
        print 'Product Weight:', pro.productWeight,
        print 'Product Price:', pro.productPrice,
        print 'Product Cost:', pro.productCost,
        print 'Product Category:', pro.productCategory
    return render(request,"first_app/index.html")