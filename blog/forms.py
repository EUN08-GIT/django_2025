from django import forms
from blog.models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','category','author','uploaded_img','uploaded_file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','content']