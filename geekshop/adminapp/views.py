from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from authapp.models import ShopUser
from mainapp.models import ProductCategotry, Product


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    context = {
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/users_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    context = {
        'object_list': ProductCategotry.objects.all()
    }
    return render(request, 'adminapp/categories_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    pass


def products(request, pk):
    context = {
        'object_list': Product.objects.filter(category__pk=pk)
    }
    return render(request, 'adminapp/product_list.html', context)


def product_create(request):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass


def product_read(request, pk):
    pass
