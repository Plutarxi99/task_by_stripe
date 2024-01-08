from django.urls import path
from payment.apps import PaymentConfig
from payment.views import OrderRetrieveAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('order_buy/<int:pk>/', OrderRetrieveAPIView.as_view(), name='order-buy')
]