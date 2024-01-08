from rest_framework import serializers

from payment.models import Order
from payment.services import get_session_for_order


class OrderSessionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения ссылки на оплату товара со скидкой
    """
    stripe_session_url = serializers.SerializerMethodField()

    def get_stripe_session_url(self, obj):
        session = get_session_for_order(pk_order=obj.pk)
        session_url = session['url']
        return session_url

    class Meta:
        model = Order
        fields = ('stripe_session_url',)
