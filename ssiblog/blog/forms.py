from django import forms
from django.forms import TextInput
from .models import Comments, Post
from tinymce.widgets import TinyMCE



class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class CommentForm(forms.ModelForm):
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
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'image', 'tags',]

