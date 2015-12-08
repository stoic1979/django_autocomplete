from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

from autocomp.forms import CustomerForm
from autocomp.models import Customer
from django.core import serializers
from django.http import HttpResponse

import json

def home(request):
    c = {'frmCustomer': CustomerForm()}
    return render_to_response('index.html', c, context_instance=RequestContext(request))

def address_lookup(request):
    c = {}
    return render_to_response('auto_address.html', c, context_instance=RequestContext(request))

def customer_lookup(request, phone):
    data = []
    try:
        data = serializers.serialize("json", Customer.objects.filter(phone__startswith=phone))
        print "data=", data
    except Exception, exp:
        print exp
        print "Customer Not Found !" 
    return HttpResponse(data)

def get_phones(request):
    phones = []
    try:
        for customer in Customer.objects.all():
            phones.append(customer.phone)
    except Exception, exp:
        print exp
        print "Phone Not Found !" 
    print "phones=", phones
    return HttpResponse(json.dumps(phones))
    
