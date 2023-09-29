from django.urls import path
from .views import *

urlpatterns = [
    path('create-category/', CreateCategory.as_view(), name="create-category"),
    path('create-product/', CreateProduct.as_view(), name="create-category")
]