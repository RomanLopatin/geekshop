from django.urls import path

from mainapp import views as mainapp

app_name = 'products'

urlpatterns = [
    path('', mainapp.products, name="products"),
    path('<name>', mainapp.products, name="product_category"),
]
