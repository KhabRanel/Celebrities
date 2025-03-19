from django import forms
from .models import Stars, Category


class AddPostForm(forms.ModelForm):

    class Meta:
        cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана",
                                     label="Категории")

        model = Stars
        fields = ['name', 'country', 'birth_date', 'cat', 'full_content', 'slug', 'is_published']
        labels = {'slug': 'URL'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'birth_date': forms.SelectDateWidget(years=range(1900, 2026)),
            'is_published': forms.CheckboxInput(),
        }


