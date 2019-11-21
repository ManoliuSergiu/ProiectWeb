from django.urls import path
from products.views.product import ItemView
from products.views.search import SearchView
from products.views.add import AddView


urlpatterns = [
    path('item/<int:pk>', ItemView.as_view(), name = 'Item'),
    path('search', SearchView.as_view(), name = 'Search'),
    path('add', AddView.as_view(), name='Add' ), 
]