from django import forms
from .models import Category  # Import your Category model
from .models import Post  # Import your Post model


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'content', 'url', 'category', 'image']
