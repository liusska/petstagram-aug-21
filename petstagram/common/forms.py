from petstagram.common.models import Comment
from petstagram.common.models import Pet
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


