# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory
from multiupload.fields import MultiFileField

from bootstrap3.tests import TestForm


BU_CHOICES = (
    ('ebg', 'EBG'),
    ('ebg_bu1', 'EBG BU 1'),
    ('ebg_bu2', 'EBG BU 2'),
    ('ebg_bu3', 'EBG BU 3'),
    ('ebg_bu5', 'EBG BU 5'),
    ('ebg_bu6', 'EBG BU 6'),
    ('ebg_pc', 'EBG PRODUCT CENTER'),
    ('ebg_nidc', 'EBG NIDC'),
)

STATUS_CHOICES = (
    ('ready', 'READY'),
    ('stop', 'STOP'),
)

PRODUCT_TYPE_CHOICES = (
    ('Enterprise', (
        ('network', 'Network'),
        ('server', 'Server'),
	('storage', 'Storage'),
	('rack', 'Rack'),
	('eother', 'Enterprise Other'),
    )
    ),
    ('Personal', (
        ('pc', 'Personal Computer'),
        ('nb', 'Notebook'),
	('pad', 'PAD'),
	('phone','Phone'),
	('wear', 'Wearable Computer'),
	('pother', 'Personal Other')
    )
    ),
    ('unknown', 'Unknown'),
)




'''
DEMO DATA
'''
RADIO_CHOICES = (
    ('1', 'Radio 1'),
    ('2', 'Radio 2'),
)

MEDIA_CHOICES = (
    ('Audio', (
        ('vinyl', 'Vinyl'),
        ('cd', 'CD'),
    )
    ),
    ('Video', (
        ('vhs', 'VHS Tape'),
        ('dvd', 'DVD'),
    )
    ),
    ('unknown', 'Unknown'),
)


class ContactForm(TestForm):
    pass


class ContactBaseFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(ContactBaseFormSet, self).add_fields(form, index)

    def clean(self):
        super(ContactBaseFormSet, self).clean()
        raise forms.ValidationError("This error was added to show the non form errors styling")

ContactFormSet = formset_factory(TestForm, formset=ContactBaseFormSet,
                                 extra=2,
                                 max_num=4,
                                 validate_max=True)


class FilesForm(forms.Form):
    text1 = forms.CharField()
    file1 = forms.FileField()
    file2 = forms.FileField(required=False)
    file3 = forms.FileField(widget=forms.ClearableFileInput)
    file4 = forms.FileField(required=False, widget=forms.ClearableFileInput)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data














'''
Custom form
'''
class SignUpForm(forms.Form):
    """
    Form with a variety of widgets to test bootstrap3 rendering.
    """
    account = forms.CharField(
        max_length=100,
        label='Account',
        required=True,
    )
    password = forms.CharField(widget=forms.PasswordInput)

    required_css_class = 'bootstrap3-req'

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        return cleaned_data





class LoginForm(forms.Form):
    """
    Form with a variety of widgets to test bootstrap3 rendering.
    """
    account = forms.CharField(
        max_length=100,
	label='Account',
        help_text='account is required',
        required=True,
        widget=forms.TextInput(attrs={'Inventec': 'hahaha uccu'}),
    )
    password = forms.CharField(widget=forms.PasswordInput)

    required_css_class = 'bootstrap3-req'

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        return cleaned_data

class ProductNewForm(forms.Form):
    extra_field_count = forms.CharField(widget=forms.HiddenInput())
    productname = forms.CharField(
        max_length=100,
        label='Product Name',
        help_text='Product is required',
        required=True,
    )
    productid = forms.CharField(
        max_length=100,
        label='Product ID',
        help_text='&nbsp',
        required=True,
    )
    bu = forms.ChoiceField(
        choices=BU_CHOICES,
        label='Business Unit',
        help_text='&nbsp',
        required=True,
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        label='Status',
        help_text='&nbsp',
        required=True,
    )
    producttype = forms.MultipleChoiceField(
        choices=PRODUCT_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Product Type',
        help_text='Check your product types',
    )
    pics = MultiFileField(
        min_num=0, max_num=5,
        required=False,
        label='Product Pictures',
        max_file_size=1024*1024*5,
        help_text='Please upload picture (max 5 file)',
    )
    specs = MultiFileField(
        min_num=0, max_num=3,
        required=False,
        label='Product Specs',
        max_file_size=1024*1024*5,
        help_text='Please upload specs (max 3 file)',
    )
    required_css_class = 'bootstrap3-req'

    def clean(self):
        cleaned_data = super(ProductInsertForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)
        super(ProductNewForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields
        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()



class ProductInsertForm(forms.Form):
    productname = forms.CharField(
        max_length=100,
        label='Product Name',
        help_text='Product is required',
        required=True,
    )
    productid = forms.CharField(
	max_length=100,
	label='Product ID',
	help_text='&nbsp',
        required=True,
    )
    bu = forms.ChoiceField(
        choices=BU_CHOICES,
        label='Business Unit',
	help_text='&nbsp',
        required=True,
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        label='Status',
        help_text='&nbsp',
        required=True,
    )
    producttype = forms.MultipleChoiceField(
        choices=PRODUCT_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
	required=False,
	label='Product Type',
        help_text='Check your product types',
    )
    pics = MultiFileField(
	min_num=0, max_num=5, 
	required=False,
	label='Product Pictures',
	max_file_size=1024*1024*5,
	help_text='Please upload picture (max 5 file)',
    )
    specs = MultiFileField(
        min_num=0, max_num=3,
        required=False,
	label='Product Specs',
        max_file_size=1024*1024*5,
        help_text='Please upload specs (max 3 file)',
    )
    required_css_class = 'bootstrap3-req'

    def clean(self):
        cleaned_data = super(ProductInsertForm, self).clean()
        return cleaned_data




'''

class TestForm(forms.Form):
    """
    Form with a variety of widgets to test bootstrap3 rendering.
    """
    date = forms.DateField(required=False)
    subject = forms.CharField(
        max_length=100,
        help_text='my_help_text',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'placeholdertest'}),
    )
    password = forms.CharField(widget=forms.PasswordInput)
    message = forms.CharField(required=False, help_text='<i>my_help_text</i>')
    sender = forms.EmailField(
        label='Sender © unicode',
        help_text='E.g., "me@example.com"')
    secret = forms.CharField(initial=42, widget=forms.HiddenInput)
    cc_myself = forms.BooleanField(
        required=False,
        help_text='cc stands for "carbon copy." '
                  'You will get a copy in your mailbox.'
    )
    select1 = forms.ChoiceField(choices=RADIO_CHOICES)
    select2 = forms.MultipleChoiceField(
        choices=RADIO_CHOICES,
        help_text='Check as many as you like.',
    )
    select3 = forms.ChoiceField(choices=MEDIA_CHOICES)
    select4 = forms.MultipleChoiceField(
        choices=MEDIA_CHOICES,
        help_text='Check as many as you like.',
    )
    category1 = forms.ChoiceField(
        choices=RADIO_CHOICES, widget=forms.RadioSelect)
    category2 = forms.MultipleChoiceField(
        choices=RADIO_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        help_text='Check as many as you like.',
    )
    category3 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=MEDIA_CHOICES)
    category4 = forms.MultipleChoiceField(
        choices=MEDIA_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        help_text='Check as many as you like.',
    )
    addon = forms.CharField(
        widget=forms.TextInput(attrs={'addon_before': 'before', 'addon_after': 'after'}),
    )

    required_css_class = 'bootstrap3-req'

    def clean(self):
        cleaned_data = super(TestForm, self).clean()
        raise forms.ValidationError(
            "This error was added to show the non field errors styling.")
        return cleaned_data


'''
