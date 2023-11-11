from django.forms import ModelForm
from .models import Blog, Comment

class NewBlog(ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "content_image"]
        labels = {
            'content_image' : 'Image'
        } 

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
