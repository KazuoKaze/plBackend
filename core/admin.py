from django.contrib import admin
from .models import JustSending, OrderItem, Coupon, Variant, ModelProductModel, OrderItemProduct
from unfold.admin import ModelAdmin



class OrderItemProductAdmin(ModelAdmin):
    list_display = ['product', 'size', 'quantity', 'order_item_first_name', 'order_item_last_name', 'order_item_email']
    list_select_related = ['order_item']
    # inlines = [OrderItemInline]

    def order_item_first_name(self, obj):
        return obj.order_item.firstName

    def order_item_last_name(self, obj):
        return obj.order_item.lastName

    def order_item_email(self, obj):
        return obj.order_item.email

    order_item_first_name.short_description = 'First Name'
    order_item_last_name.short_description = 'Last Name'
    order_item_email.short_description = 'Email'

# Register each model with its respective admin
@admin.register(JustSending)
class JustSendingAdmin(ModelAdmin):
    pass

@admin.register(Variant)
class VariantAdmin(ModelAdmin):
    pass

@admin.register(Coupon)
class CouponAdmin(ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    pass

# Register the custom admin for OrderItemProduct
@admin.register(OrderItemProduct)
class CustomOrderItemProductAdmin(OrderItemProductAdmin):
    pass


