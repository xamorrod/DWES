from django import forms


class PostForm(forms.Form):
    titulo = forms.CharField(label="Título", max_length=200)
    
