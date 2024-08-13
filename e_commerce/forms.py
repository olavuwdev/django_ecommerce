from django import forms

class ContactForm(forms.Form):
    Nome_Completo = forms.CharField(
        error_messages={'required' : 'Nome completo é obrigatorio!'},
            widget=forms.TextInput(
                attrs={
                        "class": "form-control", 
                        "placeholder": "Seu nome completo"
                    }
                )
            )
    email = forms.EmailField(
        error_messages={'required' : 'Informe um email valido'},
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    comentario = forms.CharField(
        error_messages={'required' : 'Texto é obrigatorio!'},
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("O email deve ser gmail.com")
        return email   
