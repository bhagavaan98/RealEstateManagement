# views.py
from django.shortcuts import render, redirect
from .models import Property, Unit, Tenant, Lease
from .forms import TenantForm, LeaseForm,SignUpForm,PropertyForm,UnitForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home_page(request):
    return render(request,'application/base.html')


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_instance = form.save()
            return redirect(f"/add_unit/{property_instance.id}/")
    else:
        form = PropertyForm()
    return render(request, 'application/add_property.html', {'form': form})


def add_unit(request,property_id):
    if request.method == 'POST':
        # import pdb;pbd.set_trace()
        data={"rent_cost":request.POST.get('rent_cost'),"bedroom_type":request.POST.get('bedroom_type'),"property_id":property_id}
        form = UnitForm(data)

        if form.is_valid():
            form.save()
            return redirect("/property_thanks/")
    else:
        form = UnitForm()
    return render(request, 'application/add_unit.html', {'form': form})

def perperty_thanks(request):
    return render(request, 'application/add_perperty_thanks.html')

@login_required
def property_listing(request):
    properties = Property.objects.all()
    return render(request, 'application/property_listing.html', {'properties': properties})

def tenant_management(request):
    tenants = Tenant.objects.all()
    return render(request, 'application/tenant_management.html', {'tenants': tenants})

@login_required
def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST,request.FILES)
        if form.is_valid():
            tenant_instance = form.save()
            form.save()
            request.session['tenant_id'] = tenant_instance.id
            return redirect('property_listing')
    else:
        form = TenantForm()
    return render(request, 'application/add_tenant.html', {'form': form})


def unit_view(request,id):
    data=Unit.objects.get(id=id)
    request.session['unit_id'] = data.id
    return render(request,"application/unit.html",{"data":data})

def lease_details(request):
    unit_id = request.session.get('unit_id')
    unit = Unit.objects.get(id=unit_id)

    if request.method == 'POST':
        form = LeaseForm(request.POST, initial={'unit': unit})
        if form.is_valid():
            tenant_id = request.session.get('tenant_id')
            tenant_instance = Tenant.objects.get(id=tenant_id)
            form.initial['tenant_id'] = tenant_id
            # import pdb;pbd.set_trace()


            lease = form.save(commit=False)
            lease.property_id = unit.property_id 
            lease.tenant_id = tenant_instance
            lease.save()
            return redirect("/")  
        else:
            return render(request, "application/lease.html", {'form': form})
    else:
        form = LeaseForm(initial={'unit': unit})
        return render(request, "application/lease.html", {'form': form})

def thank(request):
    return render(request,"application/thanks.html")

def signup_view(request):
    form = SignUpForm()
    # import pdb;pbd.set_trace()
    if request.method == "POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect("/accounts/login") 
    return render(request,"application/signup.html",{"form":form})

def logout_view(request):
    logout(request)
    return render(request,"application/logout.html")