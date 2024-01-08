from django.conf import settings
from rest_framework.generics import RetrieveAPIView

from product.serializers import ItemSessionSerializer, ItemUrlSerializer

from django.views.generic import DetailView

from product.models import Item


class ItemSessionIdRetrieveAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSessionSerializer


class ItemBuyUrlDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemUrlSerializer


class ItemBuyDetailView(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        """
        Для передачи в HTML страницу ключа для перехода к оплате товара
        @param kwargs:
        @return: возвращает публичный ключ
        """
        context = super(ItemBuyDetailView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
