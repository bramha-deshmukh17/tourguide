from django import forms
from .models import *

class HotelForm(forms.ModelForm):
    class Meta:
        model = hotel
        fields = ['name', 'img', 'city', 'area', 'location', 'description']

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = restaurant
        fields = ['name', 'img', 'city', 'area', 'location', 'description']

class PlaceForm(forms.ModelForm):
    class Meta:
        model = place
        fields = ['name', 'img', 'city', 'area', 'location', 'description']

class GuidePhoto(forms.ModelForm):
    class Meta:
        model = TourGuide
        fields = ['img']

class PlacePhoto(forms.ModelForm):
    class Meta:
        model = place
        fields = ['img']

class RestaurantPhoto(forms.ModelForm):
    class Meta:
        model = restaurant
        fields = ['img']

class HotelPhoto(forms.ModelForm):
    class Meta:
        model = hotel
        fields = ['img']

