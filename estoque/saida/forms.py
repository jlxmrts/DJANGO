from django.forms import ModelForm
from .models import Saidas

class SaidaForm(ModelForm):
    class Meta:
        model = Saidas
        fields = ['produto', 'quantidade']