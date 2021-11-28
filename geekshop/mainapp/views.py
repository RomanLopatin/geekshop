import json

from django.shortcuts import render


# Create your views here.


def index(request):
    context = {'title': 'магазин'}
    return render(request, "mainapp/index.html", context)


links_menu = [
    {'href': "products", 'name': 'все'},
    {'href': "products_home", 'name': 'дом'},
    {'href': "products_office", 'name': 'офис'},
    {'href': "products_modern", 'name': 'модерн'},
    {'href': "products_classic", 'name': 'классика'}
]


def products(request):
    context = {
        'title': 'каталог',
        'links_menu': links_menu
    }
    return render(request, "mainapp/products.html", context)


def products_home(request):
    context = {
        'title': 'каталог',
        'links_menu': links_menu
    }
    return render(request, "mainapp/products.html", context)


def products_office(request):
    context = {
        'title': 'каталог',
        'links_menu': links_menu
    }
    return render(request, "mainapp/products.html", context)


def products_modern(request):
    context = {
        'title': 'каталог',
        'links_menu': links_menu
    }
    return render(request, "mainapp/products.html", context)


def products_classic(request):
    context = {
        'title': 'каталог',
        'links_menu': links_menu
    }
    return render(request, "mainapp/products.html", context)


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
