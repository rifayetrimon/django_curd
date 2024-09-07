from django import forms
from .models import Add

class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Enter name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Enter description',
                'rows': 4,
            }),
        }
