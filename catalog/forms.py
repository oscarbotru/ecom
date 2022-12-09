from django import forms

from catalog.models import Product


class ProductFormAdmin(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'count', 'is_deleted')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'count')
