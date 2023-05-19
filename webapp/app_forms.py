from django import forms
from .models import Doctor, Patient


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialization', 'education', 'location', 'experience', 'email', 'contact_number', 'password']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'location',  'email', 'phone_number', 'password']
