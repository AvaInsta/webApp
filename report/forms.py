from django import forms
from .models import Report
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['titleReport', 'descriptionReport', 'store_instagram_report']

        widgets = {
            'titleReport': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptionReport': forms.Textarea(attrs={'class': 'form-control'}),
            'store_instagram_report': forms.TextInput(attrs={'class': 'form-control'}),
        }
