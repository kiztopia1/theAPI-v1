
from django.urls import path
from .apiViews import ItemCreate, ReteriveUpdateDestroy, SoldItemCreate,soldItemsList

urlpatterns = [
    path('', ItemCreate.as_view()),
    path('<int:key>', ReteriveUpdateDestroy.as_view()),
    path('sold/', soldItemsList.as_view()),
    path('sold/add', SoldItemCreate.as_view()),
]
