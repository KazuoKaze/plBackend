from django.db import models
from PIL import Image
from django.utils.text import slugify

# Create your models here.



class JustSending(models.Model):
    productTitle = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField(null=True, blank=True)
    productImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    productImage2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    productImage3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    productSmallImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    createdAT = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=255, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    isOnFrontPage = models.BooleanField(default=False)

    firstTitle = models.CharField(max_length=255, null=True, blank=True)
    secondModerTitle = models.CharField(max_length=255, null=True, blank=True)
    thirdModelTitle = models.CharField(max_length=255, null=True, blank=True)
    orThirdModeTitle = models.CharField(max_length=255, null=True, blank=True)
    productModelImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    secondsModerTitle = models.CharField(max_length=255, null=True, blank=True)
    thirdsModelTitle = models.CharField(max_length=255, null=True, blank=True)
    orsThirdModeTitle = models.CharField(max_length=255, null=True, blank=True)
    pTitleFirst = models.CharField(max_length=255, null=True, blank=True)
    pTitleSecond = models.CharField(max_length=255, null=True, blank=True)
    pThordTitle = models.CharField(max_length=255, null=True, blank=True)
    productModelSecondImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    bgColor = models.CharField(max_length=255, null=True, blank=True)
    textColor = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'justSending'
        ordering = ['createdAT']

    def __str__(self):
        return f"{self.id} - {self.productTitle}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.productTitle)
        super().save(*args, **kwargs)

class ModelProductModel(models.Model):
    firstTitle = models.CharField(max_length=255, null=True, blank=True)
    secondModerTitle = models.CharField(max_length=255, null=True, blank=True)
    thirdModelTitle = models.CharField(max_length=255, null=True, blank=True)
    orThirdModeTitle = models.CharField(max_length=255, null=True, blank=True)
    productModelImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    secondsModerTitle = models.CharField(max_length=255, null=True, blank=True)
    thirdsModelTitle = models.CharField(max_length=255, null=True, blank=True)
    orsThirdModeTitle = models.CharField(max_length=255, null=True, blank=True)
    pTitleFirst = models.CharField(max_length=255, null=True, blank=True)
    pTitleSecond = models.CharField(max_length=255, null=True, blank=True)
    pThordTitle = models.CharField(max_length=255, null=True, blank=True)
    productModelSecondImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    bgColor = models.CharField(max_length=255, null=True, blank=True)
    textColor = models.CharField(max_length=255, null=True, blank=True)
    createdAT = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'modelProductModel'
        ordering = ['createdAT']

    def __str__(self):
        return f"{self.id} - {self.secondModerTitle}"

    

# class OrderItem(models.Model):
#     product = models.ManyToManyField(JustSending, related_name='product')
#     size = models.CharField(max_length=255, null=True, blank=True)
#     quantity = models.CharField(max_length=255, null=True, blank=True)
#     subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     firstName = models.CharField(max_length=255, null=True, blank=True)
#     lastName = models.CharField(max_length=255, null=True, blank=True)
#     phoneNumber = models.IntegerField()
#     email = models.EmailField(max_length=255, null=True, blank=True)
#     fullName = models.CharField(max_length=255, null=True, blank=True)
#     country = models.CharField(max_length=255, null=True, blank=True)
#     city = models.CharField(max_length=255, null=True, blank=True)
#     address = models.CharField(max_length=255, null=True, blank=True)
#     address2 = models.CharField(max_length=255, null=True, blank=True)
#     state = models.CharField(max_length=255, null=True, blank=True)
#     pinCode = models.IntegerField()
#     phoneNumber2 = models.IntegerField()
#     textNote = models.CharField(max_length=955, null=True, blank=True)


#     class Meta:
#         verbose_name_plural = 'orderItem'

#     def __str__(self):
#         return f"{self.email}"
    
class OrderItem(models.Model):
    firstName = models.CharField(max_length=255, null=True, blank=True)
    lastName = models.CharField(max_length=255, null=True, blank=True)
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    fullName = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    pinCode = models.IntegerField()
    phoneNumber2 = models.IntegerField()
    textNote = models.CharField(max_length=955, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Order Details'

    def __str__(self):
        return f"{self.email}"
    
class OrderItemProduct(models.Model):
    order_item = models.ForeignKey(OrderItem, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(JustSending, related_name='products', on_delete=models.CASCADE)
    size = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f"{self.product.productTitle} - Size: {self.size} (Quantity: {self.quantity})"
    

class Coupon(models.Model):
    product = models.ManyToManyField(JustSending, related_name='coupon')
    coupon = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'coupon'

    def __str__(self):
        return f"{self.coupon}"
    

class Variant(models.Model):
    firstVariant = models.CharField(max_length=255, null=True, blank=True)
    secondVariant = models.CharField(max_length=255, null=True, blank=True)
    thirdVariant = models.CharField(max_length=255, null=True, blank=True)
    fourthVariant = models.CharField(max_length=255, null=True, blank=True)
    product = models.ManyToManyField(JustSending, related_name='variant')

    class Meta: 
        verbose_name_plural = 'variation'

    def __str__(self):
        return f"{self.firstVariant}"