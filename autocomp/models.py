from django.utils.translation import gettext as _
from django.db import models

SHORT_STRING = 12

class Customer(models.Model):
    name = models.CharField(max_length=SHORT_STRING, verbose_name=_('customer name'), null=True, blank=True, help_text=_('Please input full name, that way system will recognize recurring customer'))
    email = models.EmailField(null=True, blank=True)
    address_street = models.CharField(max_length=100, verbose_name=_('Street'))
    address_house = models.CharField(max_length=10, verbose_name=_('House'))
    address_flat = models.CharField(max_length=20, verbose_name=_('Flat'), null=True, blank=True)
    address_postal_code = models.CharField(max_length=20, verbose_name=_('Postal code'), null=True, blank=True)
    address_comment = models.CharField(max_length=SHORT_STRING, verbose_name=_('Comments'), null=True, blank=True, default="")
    phone = models.CharField(max_length=SHORT_STRING, verbose_name=_('phone'))
