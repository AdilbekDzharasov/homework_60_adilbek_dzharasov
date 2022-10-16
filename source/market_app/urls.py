from django.urls import path



from market_app.views.products_add import add_view
from market_app.views.products_delete import delete_view
from market_app.views.products_update import update_view

from market_app.views.base import HomeView
from market_app.views.products_detail import TaskDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>', TaskDetailView.as_view(), name='product_detail'),
    path('products/add/', add_view, name='product_add'),
    path('products/delete/<int:pk>', delete_view, name='product_delete'),
    path('products/update/<int:pk>', update_view, name='product_update')
]

