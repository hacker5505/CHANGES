from django.contrib import admin
from .models import Media, OverView, Pricing, Description, Media, CompleteGig

# Register your models here.
admin.site.register(OverView)
admin.site.register(Pricing)
admin.site.register(Description)
admin.site.register(CompleteGig)
admin.site.register(Media)
