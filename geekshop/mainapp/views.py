import json

from django.shortcuts import render

# Create your views here.
from mainapp import models
from mainapp.models import Product, ProductCategotry


def index(request):
    product_list = Product.objects.all()[:4]
    context = {
        'title': 'магазин',
        'products': product_list
    }
    return render(request, "mainapp/index.html", context)


# links_menu = [
#     # {'link_name': "", 'name': 'все'},
#     {'link_name': "home", 'name': 'дом'},
#     {'link_name': "office", 'name': 'офис'},
#     {'link_name': "modern", 'name': 'модерн'},
#     {'link_name': "classic", 'name': 'классика'}
# ]

links_menu = ProductCategotry.objects.all()[:3]


def products(request, name=None):
    # if name is not None:
    #     pass

    context = {
        'title': 'каталог',
        'links_menu': links_menu
    }
    return render(request, "mainapp/products.html", context)


# def products_home(request):
#     context = {
#         'title': 'каталог',
#         'links_menu': links_menu
#     }
#     return render(request, "mainapp/products.html", context)
#
#
# def products_office(request):
#     context = {
#         'title': 'каталог',
#         'links_menu': links_menu
#     }
#     return render(request, "mainapp/products.html", context)
#
#
# def products_modern(request):
#     context = {
#         'title': 'каталог',
#         'links_menu': links_menu
#     }
#     return render(request, "mainapp/products.html", context)
#
#
# def products_classic(request):
#     context = {
#         'title': 'каталог',
#         'links_menu': links_menu
#     }
#     return render(request, "mainapp/products.html", context)


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
