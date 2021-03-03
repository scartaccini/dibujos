from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','imagen','published_date')

        published_date = forms.DateField(
            widget=forms.DateInput(format='%d/%m/%Y'),
            input_formats=('%d/%m/%Y', )
            )