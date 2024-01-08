# forms.py
from django import forms
from .models import Tenant, Lease,Property,Unit
from django.contrib.auth.models import User

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"

        widgets = {
            'property_id': forms.HiddenInput(),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['property_id'].required = False
        



class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = "__all__"

class LeaseForm(forms.ModelForm):
    agreement_end_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=True)
    monthly_rent_date = forms.IntegerField(required=True, min_value=1, max_value=31)

    class Meta:
        model = Lease
        fields = ['agreement_end_date', 'monthly_rent_date', 'unit', 'tenant_id']
        widgets = {
            'unit': forms.HiddenInput(),
            'tenant_id': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make unit and tenant_id not required
        self.fields['unit'].required = False
        self.fields['tenant_id'].required = False


class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']