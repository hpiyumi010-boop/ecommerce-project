from django.shortcuts import render
from .models import Product, Category

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})