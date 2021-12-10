from django.urls import path
from .views import OrderView, OrderDetailView, OrderPaymentView, PaymentSuccessView

urlpatterns = [
    path('order-view/', OrderView.as_view(),
         name='order_view'),
    path('order-detail/<int:id>', OrderDetailView.as_view(),
         name='order_detail'),
    path('order-payment/<int:id>', OrderPaymentView.as_view(),
         name='order_payment'),
    path('success/', PaymentSuccessView.as_view(),
         name='success'),
]
