from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import FarmUser, Livestock, Crop, Resource, VetRecord, FinancialRecord, MarketItem

# Register your models here.

admin.site.register(FarmUser)
admin.site.register(Livestock)
admin.site.register(Crop)
admin.site.register(Resource)
admin.site.register(VetRecord)
admin.site.register(FinancialRecord)
admin.site.register(MarketItem)

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     fieldsets = BaseUserAdmin.fieldsets + (
#     ('Role', {
#         'fields': ('role',)
#     }),
#     )
#     list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
#     list_filter = ('role', 'is_staff', 'is_active')
#
# @admin.register(Livestock)
# class LivestockAdmin(admin.ModelAdmin):
#     llist_display = ('tagId', 'category', 'breed', 'age', 'healthStatus', 'owner')
#     search_fields = ('tagId', 'breed', 'owner__username')
