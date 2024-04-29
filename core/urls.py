from django.urls import path
from .views import getSomething, getSingleProduct, postOrderItem, getCouponForProduct, getTheModelProduct

urlpatterns = [
    path('just/', getSomething, name='getSomething'),
    path('model/', getTheModelProduct, name='getTheModelProduct'),
    path('just/<str:pk>/', getSingleProduct, name='getSingleProduct'),
    path('postOrderItem/', postOrderItem, name='postOrderItem'),
    path('getCouponForProduct/', getCouponForProduct, name='getCouponForProduct'),
]