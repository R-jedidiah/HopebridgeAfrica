from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('type', 'image')


@admin.register(ChildrenHome)
class ChildrenHomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'phone', 'address', 'county', 'category')




@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address', 'county')


@admin.register(Donations)
class DonationsAdmin(admin.ModelAdmin):
    list_display = ('donation_type', 'message', 'donation_amount')



