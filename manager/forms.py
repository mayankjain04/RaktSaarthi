from django import forms
from django.db import models
from .models import Donor, Recipient

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'medical_history', 'blood_group', 'location', 'availability_status', 'last_donation_date']

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'urgency_level', 'location', 'blood_type_required']