from django.urls import path

from product.apps import ProductConfig
from product import views

app_name = ProductConfig.name

urlpatterns = [
    path('buy/<int:pk>/', views.ItemSessionIdRetrieveAPIView.as_view(), name='get_session_id'),
    path('item/<int:pk>/', views.ItemBuyUrlDetailView.as_view(), name='get_session_url'),
    path('item_buy/<int:pk>/', views.ItemBuyDetailView.as_view(), name='get_site'),
]