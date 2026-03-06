from django import forms
from .models import Item

class CreateNewList(forms.Form):
    model = Item
    fields = ["name", "description"]
