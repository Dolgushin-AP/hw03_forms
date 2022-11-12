from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': 'Содержимое поста',
            'group': 'Группа'
        }
        help_texts = {
            'text': 'Содержимое нового поста',
            'group': 'Выберите группу поста'
        }
