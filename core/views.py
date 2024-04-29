from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import JustSending, Coupon, Variant, ModelProductModel
from .serializers import JustSendingSerializer, OrderItemSerializer, CouponSerizlier, VariantSerizlier, ModelProductModelSeriaziler
from rest_framework.response import Response

@api_view(['GET'])
def getSomething(request):
    allHere = JustSending.objects.all()
    serizalierData = JustSendingSerializer(allHere, many=True)
    return Response(serizalierData.data)

@api_view(['GET'])
def getTheModelProduct(request):
    allHere = ModelProductModel.objects.all()
    serizalierData = ModelProductModelSeriaziler(allHere, many=True)
    return Response(serizalierData.data)


@api_view(['GET'])
def getSingleProduct(request, pk):
    # product = JustSending.objects.get(id=pk)
    # products = JustSendingSerializer(product, many=False)
    # variant = VariantSerizlier(product, many=True)
    # serizalierData = {
    #     'product': products.data,
    #     'variants': variant.data
    # }
    # # serizalierData = JustSendingSerializer(product, many=False)
    # return Response(serizalierData)
    try:
        product = JustSending.objects.get(slug=pk)
    except JustSending.DoesNotExist:
        return Response(status=404)

    # Serialize the product data
    product_serializer = JustSendingSerializer(product)

    # Serialize the variant data
    variants = Variant.objects.filter(product=product)
    variant_serializer = VariantSerizlier(variants, many=True)

    # Combine the product and variant data
    serialized_data = {
        'product': product_serializer.data,
        'variants': variant_serializer.data
    }

    return Response(serialized_data)

@api_view(['GET'])
def getCouponForProduct(request):
    coupon = Coupon.objects.all()
    print(coupon)
    seriazlizedCoupon = CouponSerizlier(coupon, many=True)
    print(seriazlizedCoupon.data)
    return Response(seriazlizedCoupon.data)

# @api_view(['POST'])
# def postOrderItem(request):
#     if request.data:
#         products_data  = request.data.get('product')

#         order_data = {
#             'product': products_data,
#             'size': request.data.get('size', 0),
#             'subtotal': request.data.get('subtotal', 0),
#             'firstName': request.data.get('formSendingData', {}).get('firstName'),
#             'lastName': request.data.get('formSendingData', {}).get('lastName'),
#             'phoneNumber': request.data.get('formSendingData', {}).get('phoneNumber'),
#             'email': request.data.get('formSendingData', {}).get('email'),
#             'fullName': request.data.get('formSendingData', {}).get('fullName'),
#             'country': request.data.get('formSendingData', {}).get('country'),
#             'city': request.data.get('formSendingData', {}).get('city'),
#             'address': request.data.get('formSendingData', {}).get('address'),
#             'address2': request.data.get('formSendingData', {}).get('address2'),
#             'state': request.data.get('formSendingData', {}).get('state'),
#             'pinCode': request.data.get('formSendingData', {}).get('pinCode'),
#             'phoneNumber2': request.data.get('formSendingData', {}).get('phoneNumber2'),
#             'textNote': request.data.get('formSendingData', {}).get('textNote'),
#         }

#         print(order_data, 'this is order data')
#         print(products_data, 'this is product data')

#         serializer = OrderItemSerializer(data=order_data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('Order submitted successfully')
#         else:
#             return Response(serializer.errors)
#     else:
#         return Response('No data provided')



# @api_view(['POST'])
# def postOrderItem(request):
#     if request.data:
#         products_data  = request.data.get('product')
#         size_data = request.data.get('size', [])
#         quantity_data = request.data.get('quantity', [])
# # Check if size_data is a list
#         if isinstance(size_data, list):
#     # Convert list to string with sizes separated by commas
#             size_str = ", ".join(["'{}'".format(size[0]) for size in size_data])
#             print("[{}]".format(size_str))
#         else:
#             print("size_data is not a list")

#         if isinstance(quantity_data, list):
#     # Convert list to string with sizes separated by commas
#             quantity_str = ", ".join(["'{}'".format(quantity[0]) for quantity in quantity_data])
#             print("[{}]".format(quantity_str))
#         else:
#             print("size_data is not a list")    

#         form_sending_data_address2 = request.data.get('formSendingData', {}).get('address2') 
#         if not form_sending_data_address2:
#             form_sending_data_address2 = 'null'


#         form_sending_data_phoneNumber2 = request.data.get('formSendingData', {}).get('phoneNumber2') 
#         if not form_sending_data_phoneNumber2:
#             form_sending_data_phoneNumber2 = 0

#         form_sending_data_textNote = request.data.get('formSendingData', {}).get('textNote') 
#         if not form_sending_data_textNote:
#             form_sending_data_textNote = 'null'
              

#         order_data = {
#             'product': products_data,
#             'size': size_str,
#             'quantity': quantity_str,
#             'subtotal': request.data.get('subtotal', 0),
#             'firstName': request.data.get('formSendingData', {}).get('firstName'),
#             'lastName': request.data.get('formSendingData', {}).get('lastName'),
#             'phoneNumber': request.data.get('formSendingData', {}).get('phoneNumber'),
#             'email': request.data.get('formSendingData', {}).get('email'),
#             'fullName': request.data.get('formSendingData', {}).get('fullName'),
#             'country': request.data.get('formSendingData', {}).get('country'),
#             'city': request.data.get('formSendingData', {}).get('city'),
#             'address': request.data.get('formSendingData', {}).get('address'),
#             'address2': form_sending_data_address2,
#             'state': request.data.get('formSendingData', {}).get('state'),
#             'pinCode': request.data.get('formSendingData', {}).get('pinCode'),
#             'phoneNumber2': form_sending_data_phoneNumber2,
#             'textNote': form_sending_data_textNote,
#         }

#         print(order_data, 'this is order data')
#         print(products_data, 'this is product data')

#         serializer = OrderItemSerializer(data=order_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('Order submitted successfully')
#         else:
#             return Response(serializer.errors)
#     else:
#         return Response('No data provided')



@api_view(['POST'])
def postOrderItem(request):
    if request.data:
        # Extract data from request
        form_sending_data = request.data.get('formSendingData', {}) 

        form_sending_data_address2 = request.data.get('formSendingData', {}).get('address2') 
        if not form_sending_data_address2:
            form_sending_data_address2 = 'null'


        form_sending_data_phoneNumber2 = request.data.get('formSendingData', {}).get('phoneNumber2') 
        if not form_sending_data_phoneNumber2:
            form_sending_data_phoneNumber2 = 0

        form_sending_data_textNote = request.data.get('formSendingData', {}).get('textNote') 
        if not form_sending_data_textNote:
            form_sending_data_textNote = 'null'

        # Create the order data dictionary
        order_data = {
            'firstName': form_sending_data.get('firstName'),
            'lastName': form_sending_data.get('lastName'),
            'phoneNumber': form_sending_data.get('phoneNumber'),
            'email': form_sending_data.get('email'),
            'fullName': form_sending_data.get('fullName'),
            'country': form_sending_data.get('country'),
            'city': form_sending_data.get('city'),
            'address': form_sending_data.get('address'),
            'address2': form_sending_data_address2,
            'state': form_sending_data.get('state'),
            'pinCode': form_sending_data.get('pinCode'),
            'phoneNumber2': form_sending_data_phoneNumber2,
            'textNote': form_sending_data_textNote,
            'subtotal': request.data.get('subtotal', 0),
            'order_items': []  # We will populate this with OrderItemProduct data
        }

        # Extract product, size, and quantity data
        products_data = request.data.get('product', [])
        size_data = request.data.get('size', [])
        quantity_data = request.data.get('quantity', [])

        # Loop through products to create OrderItemProduct data
        for idx, product_id in enumerate(products_data):
            if idx < len(size_data) and idx < len(quantity_data):
                order_item_product = {
                    'product': product_id,
                    'size': size_data[idx],
                    'quantity': quantity_data[idx]
                }
                order_data['order_items'].append(order_item_product)

        print("Order Data:")
        print(order_data)

        # Create serializer with order_data
        serializer = OrderItemSerializer(data=order_data)
        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
            return Response('Order submitted successfully')
        else:
            print("Serializer errors:")
            print(serializer.errors)
            return Response(serializer.errors)
    else:
        return Response('No data provided')