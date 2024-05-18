from django import forms
from .models import Paciente, Sede , Doctor, ObraSocial

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'direccion', 'telefono']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'apellido', 'especialidad', 'cedula_profesional']

class ObraSocialaForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = ['paciente', 'plan', 'fecha', 'motivo']

class SedeForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = ['dirección', 'ubicacion', 'personal', 'especialidades']

class BusquedaPacienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    fecha_nacimiento = forms.DateField(required=False)

class BusquedaDoctorForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    especialidad = forms.CharField(max_length=100, required=False)

class BusquedaObraSocialForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), required=False)
    plan = forms.ModelChoiceField(queryset=ObraSocial.objects.all(), required=False)
    fecha = forms.DateField(required=False)
    
    
class BusquedaSedeForm(forms.Form):
    ubicacion = forms.CharField(max_length=100, required=False)
    direccion = forms.CharField(max_length=100, required=False)
    especialidades = forms.CharField(max_length=100, required=False)