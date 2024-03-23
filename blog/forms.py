from django import forms

from .models import BlogPost

class SendCountryForm(forms.Form):
    country = forms.CharField(label="Tell me what country you live in!", max_length=50)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [ 'title', 'content' ]
