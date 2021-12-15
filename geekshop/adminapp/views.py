from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
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
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('adminapp:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    context = {
        'object_list': ProductCategotry.objects.all()
    }
    return render(request, 'adminapp/categories_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'Создание категории'

    if request.method == 'POST':
        cat_form = ProductCategoryEditForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        cat_form = ProductCategoryEditForm()

    content = {'title': title, 'cat_form': cat_form}

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'Редактирование категории'

    edit_cat = get_object_or_404(ProductCategotry, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, instance=edit_cat)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_cat.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_cat)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'Удаление категории'

    _cat = get_object_or_404(ProductCategotry, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        _cat.is_active = False
        _cat.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    content = {'title': title, 'category_to_delete': _cat}

    return render(request, 'adminapp/category_delete.html', content)


def products(request, pk):
    context = {
        'object_list': Product.objects.filter(category__pk=pk)
    }
    return render(request, 'adminapp/product_list.html', context)


def product_create(request):
    title = 'Создание продукта'

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('adminapp:products'))
    else:
        product_form = ProductEditForm()

    content = {'title': title, 'product_form': product_form}

    return render(request, 'adminapp/product_update.html', content)


def product_update(request, pk):
    title = 'Редактирование продукта'

    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'edit_form': edit_form, 'category': edit_product.category}

    return render(request, 'adminapp/product_update.html', content)


def product_delete(request, pk):
    title = 'Удаление продукта'

    product_to_delete = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        product_to_delete.is_active = False
        product_to_delete.save()
        return HttpResponseRedirect(reverse('adminapp:products', args=[product_to_delete.category.pk]))

    content = {'title': title, 'product_to_delete': product_to_delete}

    return render(request, 'adminapp/product_delete.html', content)


def product_read(request, pk):
    title = 'продукт/подробнее'
    product = get_object_or_404(Product, pk=pk)
    content = {'title': title, 'object': product}

    return render(request, 'adminapp/product_read.html', content)
