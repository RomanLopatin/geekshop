import json

from django.shortcuts import render, get_object_or_404

# Create your views here.
from basketapp.models import Basket
from mainapp import models
from mainapp.models import Product, ProductCategotry


def index(request):
    product_list = Product.objects.all()[:4]
    context = {
        'title': 'магазин',
        'products': product_list
    }
    return render(request, "mainapp/index.html", context)


def products(request, pk=None):
    links_menu = ProductCategotry.objects.all()
    title = 'продукты'

    if pk is not None:
        if pk == 0:
            product_list = Product.objects.all()
            category_item = {'name': 'все'}
        else:
            category_item = get_object_or_404(ProductCategotry, pk=pk)
            product_list = Product.objects.filter(category__pk=pk)

        content = {
            'title': title,
            'links_menu': links_menu,
            'products': product_list,
            'category': category_item,
            'basket': Basket.objects.filter(user=request.user)
        }
        return render(request, 'mainapp/products_list.html', content)

    # same_products = Product.objects.all()[1:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': Product.objects.all().first,
        'same_products': Product.objects.all()[1:3],
        'basket': basket
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    with open("json/contact_info.json") as read_f:
        adresses = json.load(read_f)

    context = {
        'title': 'Контакты',
        'addresses': adresses
    }
    return render(request, "mainapp/contact.html", context)


def context(request):
    with open("json/my.json") as read_f:
        some_info = json.load(read_f)

    context = {
        'title': "Title",
        'header': "header",
        'username': "Джон",
        'products': [{'name': 'one', 'price': 1}, {'name': 'two', 'price': 10}, {'name': 'three', 'price': 15}]
    }
    return render(request, "mainapp/test_context.html", context)
