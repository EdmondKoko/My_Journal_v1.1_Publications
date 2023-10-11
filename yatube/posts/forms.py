from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Создание формы модели Post."""
    text = forms.CharField(widget=forms.Textarea,
                           required=True,
                           label='Текст поста',
                           help_text='Текст нового поста')

    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'group': 'Группа',
        }
        help_texts = {
            'group': 'Группа, к которой будет относиться пост',
        }
