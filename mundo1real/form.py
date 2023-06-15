from django import forms

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Pesquisar produto', max_length=100)
