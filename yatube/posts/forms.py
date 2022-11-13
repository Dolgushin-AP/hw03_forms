from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = (
            'Введите какой-нибудь текст, плиииз 😥'
        )
        self.fields['group'].empty_label = (
            'Тут можно выбрать группу 🙂'
        ) 

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
