from django.urls import path
from partners.views import (PartnerCreateView, PartnerDescriptionView,
                            PartnerDashboardView,
                            GigsDashboardView, EarningsDashboardView
                            )

urlpatterns = [
    path('parter_create/', PartnerCreateView.as_view(), name='partner_create'),
    path('parter_description/', PartnerDescriptionView.as_view(), name='description'),
    path('partner_dashboard/', PartnerDashboardView.as_view(),
         name='partner_dashboard'),
    path('partner_gigs/', GigsDashboardView.as_view(),
         name='partner_gigs'),
    path('partner_earnings/', EarningsDashboardView.as_view(),
         name='partner_earnings'),
]
