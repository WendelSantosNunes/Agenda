from django import forms
from django.forms import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({
            'class': 'class-a class-b',
            'placeholder': 'Escreva aqui'
        })
        
        self.fields['first_name'].label='Primeiro nome'
        
        self.fields['first_name'].help_text='Texto de ajuda para seu usuário'
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone' , 'email', 'description', 'category'
        )
    
    def clean(self):
        cleaned_data = self.cleaned_data
        
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'
                )
            
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite Abc nesse campo',
                    code='invalid'
                )
            )
        return first_name
        