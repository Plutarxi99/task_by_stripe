from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from rest_framework import serializers

from product import services
from product.models import Item


class ItemSessionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения stripe_session_id
    """
    stripe_session_id = serializers.SerializerMethodField()

    def get_stripe_session_id(self, obj):
        session_stripe = services.CreateSessionStripe(
            name=obj.name,
            description='obj.description',
            unit_amount=obj.price,
            currency=obj.currency,
            quantity=1
        )
        session_dict_id = session_stripe.create_session()
        session_id = session_dict_id['id']
        return session_id

    class Meta:
        model = Item
        fields = ('stripe_session_id',)


class ItemUrlSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения простейшей HTML страницы
    """
    url_for_buy = serializers.SerializerMethodField()

    def get_url_for_buy(self, obj):
        url = reverse('product:get_site', args=[obj.id, ])
        return url

    class Meta:
        model = Item
        fields = ('url_for_buy',)
