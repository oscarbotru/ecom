from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductList, ProductCreate, ProductDetails, ProductDelete, ProductUpdate

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('create/', ProductCreate.as_view(), name='create'),
    path('<int:pk>/', ProductDetails.as_view(), name='details'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete'),
    path('edit/<int:pk>/', ProductUpdate.as_view(), name='update'),
]
