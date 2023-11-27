from django import forms
from reservas_app.models import Reserva

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'telefono', 'fecha_reserva', 'hora', 'cantidad_personas', 'email', 'estado', 'observacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un teléfono'}),
            'fecha_reserva': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Seleccione la fecha'}),
            'hora': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la hora'}),
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minimo 1 persona y maximo 15 personas'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el estado'}),
        }

    observacion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese observaciones (opcional)', 'rows': '3'}))