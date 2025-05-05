from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','category']    

        widgets = {
            'body': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }



class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','category']    

        widgets = {
            'body': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }