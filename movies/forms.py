from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'content', 'release', 'genre', 'nation', 'showtime', 'rating', 'director', 'actor', 'grade', 'imgfile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname', 'text']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nickname을 작성하세요'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': '댓글 내용을 작성하세요'}),
        }