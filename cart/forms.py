from django.contrib.auth import get_user_model
from django import forms
from .models import OrderItem, FormatVariation, Product, Address

User = get_user_model()


class AddToCartForm(forms.ModelForm):
    vinyl_format = forms.ModelChoiceField(
        queryset=FormatVariation.objects.none())
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = ['quantity', 'vinyl_format']

    def __init__(self, *args, **kwargs):
        self.product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=self.product_id)
        super().__init__(*args, **kwargs)

        self.fields['vinyl_format'].queryset = product.available_formats.all()

    def clean(self):
        product_id = self.product_id
        product = Product.objects.get(id=self.product_id)
        quantity = self.cleaned_data['quantity']
        if product.stock < quantity:
            raise forms.ValidationError(
                f"Sorry! We only have {product.stock} of these in the crate.")


class AddressForm(forms.Form):
    # saved_address = forms.ModelChoiceField(
    #     Address.objects.none(), required=False
    # )
    street_address = forms.CharField(required=False)
    town_or_city = forms.CharField(required=False)
    county = forms.CharField(required=False)
    postcode = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        # user = User.objects.get(id=user_id)

        saved_address_qs = Address.objects.filter(
            # user=user,
            address_type='S'
        )

        # self.fields['saved_address'].queryset = saved_address_qs

    def clean(self):
        data = self.cleaned_data

        # saved_address = data.get('saved_address', None)
        # if saved_address is None:
        if not data.get('street_address', None):
            self.add_error("street_address", "Please fill in this field")
        if not data.get('town_or_city', None):
            self.add_error("town_or_city", "Please fill in this field")
        if not data.get('county', None):
            self.add_error("county", "Please fill in this field")
        if not data.get('postcode', None):
            self.add_error("postcode", "Please fill in this field")
