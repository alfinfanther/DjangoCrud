from django import forms
from django.db.models import Q
from django.core.validators import RegexValidator

TYPE_CHOICES = (
    ('One Of Novel', 'One Of Novel'),
    ('Documentation', 'Documentation'),
    ('Others', 'Others')
)

class BookForm(forms.Form):
    """docstring for ClassName"""

    title = forms.CharField(
        label="Title",
        initial='',
        widget=forms.TextInput(attrs={
            'id': 'title',
            'class': 'form-control',
            'data-parsley-required': 'true',
        }),
        required=True)

    author = forms.CharField(
        label="Author",
        initial='',
        widget=forms.TextInput(attrs={
            'id': 'author',
            'class': 'form-control',
            'data-parsley-required': 'true'
        }),
        required=True)

    data_published = forms.DateField(
        label="data_published",
        initial='',
        widget=forms.DateInput(attrs={
            'id': 'date_published',
            'class': 'form-control',
            'data-parsley-required': 'true',
            'type': 'date'
        })
    )

    number_of_page = forms.IntegerField(
        label="Number Of Page",
        initial='',
        widget=forms.TextInput(attrs={
            'id': 'number_of_page',
            'class': 'form-control',
            'data-parsley-required': 'true',
            'type': 'number'
        })
    )

    type_of_book = forms.ChoiceField(
        choices=TYPE_CHOICES,
        label="Type Of Book",
        initial='',
        widget=forms.Select(attrs={
            'id': 'type_of_book',
            'class': 'form-control',
            'data-parsley-required': 'true'
        })
    )
