from django import forms


class PostForm(forms.Form):
    titulo = forms.CharField(label="Título", max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    fechaPublicado = forms.DateField(label="Fecha de publicación")

class PostEdit(forms.Form):
    titulo = forms.CharField(label="Título", max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    fechaPublicado = forms.DateField(label="Fecha de publicación")
