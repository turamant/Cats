from django import forms
from django.core.exceptions import ValidationError

from posts.models import Tag, Post


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title','url']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_url(self):
        new_url = self.cleaned_data['url'].lower()

        if new_url == 'create':
            raise ValidationError('Url не может быть создан')
        if Tag.objects.filter(url__iexact=new_url).count():
            raise ValidationError(f'Url должен быть unique.Такой {new_url} уже существует')
        return new_url

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'url', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_url(self):
        new_url = self.cleaned_data['url'].lower()

        if new_url == 'create':
            raise ValidationError('Url не может быть создан')
        return new_url
