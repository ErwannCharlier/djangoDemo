from django import forms
from .models import Comment, Post, Character

class CommentForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Ajouter un commentaire...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Comment
        fields = ['body']

class PostForm(forms.ModelForm):
    characters = forms.ModelMultipleChoiceField(
        queryset=Character.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Utilisez CheckboxSelectMultiple pour permettre la sélection multiple
    )
    class Meta:
        model = Post
        fields = ['description', 'image','characters']
