from django.urls import path
from products.views.product import ItemView
from products.views.search import SearchView
from products.views.add import ProductCreateView, detailFormView


urlpatterns = [
    path('item/<int:pk>', ItemView.as_view(), name = 'Item'),
    path('search', SearchView.as_view(), name = 'Search'),
    path('add', ProductCreateView.as_view(), name='Add' ), 
    # path('edit/<int:pk>',ProductUpdateView.as_view() , name='Edit'), 
    path('detailform',detailFormView,name='Detail Form'),

]