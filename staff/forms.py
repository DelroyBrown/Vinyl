from django import forms
from cart.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'artist_name',
            'album_title',
            'image',
            'image_2',
            'spotify_link',
            'price',
            'available_formats',
            'primary_genre',
            'secondary_genre',
            'stock',
        ]
        labels = {
            'artist_name' : ('Artist/Band Name'),
            'album_title' : ('Album Title'),
            'image' : ('Product List Image'),
            'image_2' : ('Product Display Image'),
            'spotify_link' : ('Link to Spotify'),
            'price' : ('Vinyl Retail Price'),
            'available_formats' : ('Available Formats'),
            'primary_genre' : ('Primary Genre'),
            'secondary_genre' : ('Secondary Genre'),
            'stock' : ('Stock Availability')
        }
       