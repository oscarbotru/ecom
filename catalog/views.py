from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from catalog.forms import ProductFormAdmin, ProductForm
from catalog.models import Product


class ProductList(ListView):
    model = Product  # catalog/product_list.html
    extra_context = {
        'page_title': 'Список активных товаров'
    }
    queryset = Product.objects.filter(is_deleted=False)


class ProductCreate(CreateView):
    model = Product  # catalog/product_form.html
    fields = ('title', 'price',)
    success_url = reverse_lazy('catalog:list')


class ProductUpdate(UpdateView):
    model = Product  # catalog/product_form.html
    fields = ('title', 'price',)
    success_url = reverse_lazy('catalog:list')


class ProductDetails(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        return context_data


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')

    def post(self, *args, **kwargs):
        product_item = self.model.objects.filter(pk=self.kwargs.get('pk')).first()
        if product_item:
            product_item.is_deleted = True
            product_item.save()

        return redirect(self.success_url)
