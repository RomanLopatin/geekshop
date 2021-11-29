from django.urls import path

from mainapp import views as mainapp

app_name = 'products'

urlpatterns = [
    path('', mainapp.products, name="products"),
    path('home/', mainapp.products_home, name="products_home"),
    path('office/', mainapp.products_office, name="products_office"),
    path('modern/', mainapp.products_modern, name="products_modern"),
    path('classic/', mainapp.products_classic, name="products_classic"),
]
