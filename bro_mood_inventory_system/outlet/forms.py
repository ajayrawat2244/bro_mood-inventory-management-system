from django import forms
from .models import Journal


class JournalFilterForm(forms.Form):
    CATEGORY_CHOICES = [(cat, cat) for cat in Journal.objects.values_list('category', flat=True).distinct()]
    SIZE_CHOICES = [(size, size) for size in Journal.objects.values_list('size', flat=True).distinct()]
    COLOR_CHOICES = [(color, color) for color in Journal.objects.values_list('color', flat=True).distinct()]

    category = forms.ChoiceField(choices=[('', 'All Categories')] + CATEGORY_CHOICES, required=False)
    size = forms.ChoiceField(choices=[('', 'All Sizes')] + SIZE_CHOICES, required=False)
    color = forms.ChoiceField(choices=[('', 'All Colors')] + COLOR_CHOICES, required=False)
