# Controller
from django.shortcuts import render
# from .models import Products
from .models import Product
# Create your views here.
def index(request):
    product = Product.objects.all()
    print "*"*10
    print (product)
    print "*"*10
    Product.objects.create(name="tent",
    description="A 4 person tent perfect for backpacking",
    weight="20.00",
    price="2000.00",
    cost="1000.00")

    Product.objects.create(name="backpack",
    description="A compact backpack perfect for all your solo or group backpacking trips",
    weight="5.00",
    price="500.00",
    cost="200.00")

    Product.objects.create(name="canteen",
    description="Purfied water canteen insolated with BPA-free casing.",
    weight="3.00",
    price="100.00",
    cost="50.00")

    product = Product.objects.all()
    print "!"*50
    print (product)
    print "!"*50
    return render(request, 'myApp/index.html')
