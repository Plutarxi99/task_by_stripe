from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from payment.models import Order
from payment.serializers import OrderSessionSerializer


class OrderRetrieveAPIView(RetrieveAPIView):
    """
    Получение ссылки на покупку выбранных продуктов
    """
    queryset = Order.objects.all()
    serializer_class = OrderSessionSerializer
