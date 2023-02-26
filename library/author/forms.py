from django.forms import ModelForm

from author.models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']

