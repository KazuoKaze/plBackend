from rest_framework.serializers import ModelSerializer
from .models import JustSending, OrderItem, Coupon, Variant, ModelProductModel, OrderItemProduct

class JustSendingSerializer(ModelSerializer):
    class Meta:
        model = JustSending
        fields = '__all__'

class ModelProductModelSeriaziler(ModelSerializer):
    class Meta:
        model = ModelProductModel
        fields = '__all__'


# class OrderItemSerializer(ModelSerializer):
#     product = JustSendingSerializer(many=True)

#     class Meta:
#         model = OrderItem
#         fields = '__all__'

#     def create(self, validated_data):
#         product_data = validated_data.pop('product')
#         size_data = validated_data.pop('size', []) 

#         # If size_data is a list, join the values into a string
#         if isinstance(size_data, list):
#             size_str = ', '.join(size_data)
#         else:
#             size_str = size_data

#         order_item = OrderItem.objects.create(size=size_str, **validated_data)
#         order_item.product.set(product_data)
#         return order_item
        
class OrderItemProductSerializer(ModelSerializer):
    class Meta:
        model = OrderItemProduct
        fields = ['product', 'size', 'quantity']

class OrderItemSerializer(ModelSerializer):
    order_items = OrderItemProductSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = ['firstName', 'lastName', 'phoneNumber', 'email', 'fullName', 'country',
                  'city', 'address', 'address2', 'state', 'pinCode', 'phoneNumber2', 'textNote', 'subtotal', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order_item = OrderItem.objects.create(**validated_data)
        for order_item_data in order_items_data:
            OrderItemProduct.objects.create(order_item=order_item, **order_item_data)
        return order_item





# class OrderItemSerializer(ModelSerializer):

#     class Meta:
#         model = OrderItem
#         fields = '__all__'

#     def create(self, validated_data):
#         product_data = validated_data.pop('product')
#         order_item = OrderItem.objects.create(**validated_data)
#         order_item.product.set(product_data)
#         return order_item
        


    

class CouponSerizlier(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class VariantSerizlier(ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'
        

# class CartSerizalizer(ModelSerializer):
#     class Meta:
#         model = CartHere
#         fields = ['product', 'quantity']

