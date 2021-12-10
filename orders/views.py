from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import UserProfile
from .models import Order
from gigs.models import CompleteGig

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        active_orders = Order.objects.filter(user=user_profile, active=True)
        cancelled_orders = Order.objects.filter(
            user=user_profile, cancelled=True)
        delivered_orders = Order.objects.filter(
            user=user_profile, delivered=True, active=False)
        completed_orders = Order.objects.filter(
            user=user_profile, delivered=True, cancelled=False)
        all_orders = Order.objects.all()
        context = {
            'user_profile': user_profile,
            'active_orders': active_orders,
            'cancelled_orders': cancelled_orders,
            'delivered_orders': delivered_orders,
            'completed_orders': completed_orders,
            'all_orders': all_orders
        }
        return render(request, 'orders/order.html', context=context)


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        gig = CompleteGig.objects.get(id=id)
        service_fee = (gig.pricing.price / 100) * 5
        total = gig.pricing.price + service_fee
        context = {
            'gig': gig,
            'service_fee': round(service_fee, 2),
            'total': total
        }
        return render(request, 'orders/order-detail.html', context=context)


class OrderPaymentView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        gig = CompleteGig.objects.get(id=id)
        service_fee = (gig.pricing.price / 100) * 5
        total = gig.pricing.price + service_fee
        context = {
            'gig': gig,
            'service_fee': round(service_fee, 2),
            'total': total
        }
        return render(request, 'orders/order-pay.html', context=context)

    def post(self, request, id, *args, **kwargs):
        gig = CompleteGig.objects.get(id=id)
        service_fee = (gig.pricing.price / 100) * 5
        total = gig.pricing.price + service_fee

        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 10000,
                        'product_data': {
                            'name': gig.over_view.title,
                            # 'images': gig.media.main_image.url,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": gig.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        # return JsonResponse({
        #     'id': checkout_session.id
        # })

        # YOUR_DOMAIN = "http://127.0.0.1:8000"
        # checkout_session = stripe.checkout.Session.create(
        #     line_items=[
        #         {
        #             'price': '100',
        #             'quantity': 1,
        #         },
        #     ],
        #     payment_method_types=[
        #         'card',
        #     ],
        #     mode='payment',
        #     success_url=YOUR_DOMAIN + '/success/',
        #     cancel_url=YOUR_DOMAIN + '/success/',
        # )
        return redirect(checkout_session.url, code=303)


class PaymentSuccessView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('ok')
