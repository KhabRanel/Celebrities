from django import forms
from .models import Stars, Category


class AddPostForm(forms.ModelForm):

    class Meta:
        cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана",
                                     label="Категории")

        model = Stars
        fields = ['name', 'country', 'birth_date', 'cat', 'full_content',
                  'is_published', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Леонардо Дикаприо'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'cat': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Кино'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'США'}),
            'full_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите биографию'})
        }


