from typing import overload
from django.urls import path
from .views import (OverViewGigView, PricingGigView, DescriptionGigView,
                    MediaGigView, EditGigView, DeleteGigView, ContinueGigView, GigsView, GigDetailView)


urlpatterns = [
    path('over_view/', OverViewGigView.as_view(), name='over_view'),
    path('pricing/', PricingGigView.as_view(), name='pricing'),
    path('description/', DescriptionGigView.as_view(), name='description'),
    path('media/', MediaGigView.as_view(), name='media'),
    path('<int:gig_id>/edit', EditGigView.as_view(), name='edit_gig'),
    path('<int:gig_id>/delete', DeleteGigView.as_view(), name='delete_gig'),
    path('<int:gig_id>/continue', ContinueGigView.as_view(), name='continue_gig'),
    path('gigs/', GigsView.as_view(), name='gigs'),
    path('<int:gig_id>/detail', GigDetailView.as_view(), name='gig_detail'),
]
