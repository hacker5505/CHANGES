from django.contrib import admin
from .models import Category, SubCategory


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 1
    # show_change_link = True


@admin.register(Category)
class ListingAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]
