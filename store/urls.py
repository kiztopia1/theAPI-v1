
from django.urls import path
from .apiViews import ItemCreate, ReteriveUpdateDestroy, SoldItemCreate,soldItemsList,ItemsList

urlpatterns = [
    # add new item
    path('item/add', ItemCreate.as_view()),
    # list of items
    path('items/', ItemsList.as_view()),
    # items edit delete update
    path('item/<int:key>', ReteriveUpdateDestroy.as_view()),
    #list of sold items
    path('sold-items/', soldItemsList.as_view()),
    # add new sold Item
    path('sold/add', SoldItemCreate.as_view()),
]
