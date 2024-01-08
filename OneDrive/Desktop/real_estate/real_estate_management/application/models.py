from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()

    def __str__(self):
        return str("{} - {}".format(self.features, self.address))


class Unit(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.PROTECT)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    bedroom_type = models.CharField(max_length=10, choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')])
    
    def clean(self):
         if self.rent_cost <=0:
              raise ValidationError("Rent cost must be a positive number")
         
    def __str__(self):
        return str(self.bedroom_type)

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    DOCUMENT_CHOICES = [
        ('aadhar', 'Aadhar Card'),
        ('pancard', 'PAN Card'),
        ('passport', 'Passport'),
    ]
    document_proofs = models.CharField(max_length=10, choices=DOCUMENT_CHOICES)
    document_image = models.FileField(null=True,upload_to='tenant_documents/')


class Lease(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveIntegerField()

    def clean_monthly_rent_date(self):
        if not (1 <=self.monthly_rent_date <=31):
            raise ValidationError("Monthly rent date must be between 1 and 31.")
          

