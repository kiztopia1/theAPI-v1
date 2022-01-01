from rest_framework import response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import ValidationError 
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from store.models import Item, SoldItem
from store.serializers import ItemSerializer, SoldItemSerializer

# item getway
class ItemCreate(CreateAPIView):
    serializer_class = ItemSerializer

    def create(self, request, *args,  **kwargs):
        try: 
            price = request.data.get('price') 
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'price': "A valid number is required"})
        return super().create(request, *args, **kwargs )

# items list class
class ItemsList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields =  ('name','amount')

class ReteriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    lookup_field = 'key'
    serializer_class = ItemSerializer

    def delete(self, request, *args, **kwargs):
        item_id = request.data.get('key')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            cache.delete('item_data_{}'.format(item_id))
        return response
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            item = response.data
            cache.set('item_data_{}'.format(item['key']), {
                'name': item['name'],
                'price': item['price'],
                'amount': item['amount']
            })
        return response

class soldItemsList(ListAPIView):
    queryset = SoldItem.objects.all()
    serializer_class = SoldItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields =  ('date',)

#sold item 
class SoldItemCreate(CreateAPIView):
    serializer_class = SoldItemSerializer

    def create(self, request, *args,  **kwargs):
        try: 
            price = request.data.get('price') 
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'price': "A valid number is required"})
        return super().create(request, *args, **kwargs )
