# -*- coding: utf-8 -*-
from django import forms

class UploadFileForm(forms.Form):
    docfile = forms.FileField(label='Insert a text file')
