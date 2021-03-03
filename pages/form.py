from django import forms

class formClient(forms.Form):
    nom = forms.CharField(label = 'nom')
    prenom = forms.CharField(label = 'prenom')
    
