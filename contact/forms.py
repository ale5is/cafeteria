from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(label='Nombre', min_length=3, max_length=100,
    required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Escribe tu nombre.', 'class':'form-control'
    }))
    email= forms.EmailField(label='Email', min_length=3, max_length=100,
    required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Escribe tu email.', 'class':'form-control'
    }))
    message= forms.CharField(label='Contenido', min_length=3, max_length=100,
    required=True, widget=forms.Textarea(attrs={
        'placeholder': 'Escribe tu mensaje.', 'class':'form-control', 'rows':3
    }))