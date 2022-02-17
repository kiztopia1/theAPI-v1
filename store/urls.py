
from django.urls import path
from .apiViews import ProductsList, ProductReterive
from .views import index, add_new_product
urlpatterns = [
    path('', index , name='index'),
    path('add_new_product', add_new_product, name='products_list'),
    path('add_new_product', add_new_product, name='add_new_product'),


    # # add new item
    # path('api/v1/item/add', ItemCreate.as_view()),
    # # list of items
    path('api/v1/products/', ProductsList.as_view()),
    path('api/v1/products/<int:id>', ProductReterive.as_view()),
    # # items edit delete update
    # path('api/v1/item/<int:key>', ReteriveUpdateDestroy.as_view()),
    # #list of sold items
    # path('api/v1/sold-items/', soldItemsList.as_view()),
    # # add new sold Item
    # path('api/v1/pos/add', SoldItemCreate.as_view()),
]
