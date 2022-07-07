from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=150)
    town_or_city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, default=True)
    postcode = models.CharField(max_length=20)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.street_address}, {self.town_or_city}, {self.county}, {self.postcode}"

    class Meta:
        verbose_name_plural = 'Addresses'


class FormatVariation(models.Model):
    format_name = models.CharField(max_length=20)

    def __str__(self):
        return self.format_name


class Product(models.Model):
    artist_name = models.CharField(max_length=150, null=False)
    album_title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_images')
    image_2 = models.ImageField(upload_to='product_images')
    spotify_link = models.URLField(max_length=150)
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    available_formats = models.ManyToManyField(FormatVariation)
    primary_genre = models.ForeignKey(
        Genre, related_name='primary_genre_products', on_delete=models.CASCADE)
    secondary_genre = models.ManyToManyField(Genre, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.artist_name

    def get_absolute_url(self):
        return reverse("cart:product-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("staff:product-update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("staff:product-delete", kwargs={"pk": self.pk})

    def get_price(self):
        return "{:.2f}".format(self.price)

    @property
    def in_stock(self):
        return self.stock > 0


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    vinyl_format = models.ForeignKey(
        FormatVariation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.artist_name} / {self.product.album_title} - {self.quantity}x"

    def get_raw_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_item_price(self):
        price = self.get_raw_total_item_price()
        return "{:.2f}".format(price)


class Order(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)

    billing_address = models.ForeignKey(
        Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"
    
    

    def get_raw_subtotal(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_raw_total_item_price()
        return total

    def get_subtotal(self):
        subtotal = self.get_raw_subtotal()
        return "{:.2f}".format(subtotal)

    def get_raw_total(self):
        subtotal = self.get_raw_subtotal()
        # total = subtotal - delivery
        return subtotal

    def get_total(self):
        total = self.get_raw_total()
        return "{:.2f}".format(total)


class Payment(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=(
        ('PayPal', 'PayPal'),
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"PAYMENT-{self.order}-{self.pk}"


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.album_title)


pre_save.connect(pre_save_product_receiver, sender=Product)
