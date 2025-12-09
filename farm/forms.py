from django import forms
from django.forms import ModelForm
from .models import Livestock

#Create a Livestock Form
class LivestockForm(ModelForm):
    class Meta: #allows you to define things in django
        model = Livestock
        fields = ('category', 'tagId', 'breed', 'age', 'healthStatus', 'location', 'owner')
