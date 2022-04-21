from django import forms
from django.forms import TextInput
from .models import Comments, Post, contactForm
from captcha.fields import CaptchaField
from ckeditor.widgets import CKEditorWidget


class CForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = contactForm
        fields = ['formEmail', 'formMessage']


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comments
        fields = ('body',)
        widgets = {
            'body': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Skomentuj tutaj'
            })}


class addPostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'image', 'tags', ]
