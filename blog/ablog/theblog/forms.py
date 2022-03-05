from logging import PlaceHolder
from django import forms
from .models import Post, Category

#choices = [('coding', 'coding'), ('sports', 'sports') , ('dupa', 'dupa')]
choices = Category.objects.all().values_list('name', 'name')

choise_list = []

for item in choices:
    choise_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_TAG', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'title_TAG': forms.TextInput(attrs={'class': 'form-control'}),  
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choise_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_TAG', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'title_TAG': forms.TextInput(attrs={'class': 'form-control'}),  
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choise_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }