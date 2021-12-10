import json
import random

from django.shortcuts import render, get_object_or_404

# Create your views here.
from basketapp.models import Basket
from mainapp import models
from mainapp.models import Product, ProductCategotry


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products_list = Product.objects.all()
    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    same_products_list = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)
    return same_products_list[:3]


def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    product_list = Product.objects.all()[:4]
    context = {
        'title': 'магазин',
        'products': product_list,
        'basket': basket
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

        basket = []
        if request.user.is_authenticated:
            basket = get_basket(request.user)

        content = {
            'title': title,
            'links_menu': links_menu,
            'products': product_list,
            'category': category_item,
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)

    # same_products = Product.objects.all()[1:3]
    # basket = []
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)
    hot_product = get_hot_product()
    basket = []
    if request.user.is_authenticated:
        basket = get_basket(request.user)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
        'basket': basket
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    with open("json/contact_info.json") as read_f:
        adresses = json.load(read_f)
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Контакты',
        'addresses': adresses,
        'basket': basket
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


def product(request, pk):
    title = 'продукты'
    basket = []
    if request.user.is_authenticated:
        basket = get_basket(request.user)

    content = {
        'title': title,
        'links_menu': ProductCategotry.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': basket,
    }

    return render(request, 'mainapp/product.html', content)
