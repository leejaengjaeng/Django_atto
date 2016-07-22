# -*- coding: utf-8 -*-
from django import forms

class TestImageUploadForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )