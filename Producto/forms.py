from django import forms

class SearchForm(forms.Form):
    producto = forms.CharField(max_length=100)
    producto.widget.attrs.update({'placeholder': 'ingrese producto'})
    