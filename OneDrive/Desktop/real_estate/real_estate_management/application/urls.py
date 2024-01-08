
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('a_property/',views.add_property, name='a_property'),
    path('property_listing/', views.property_listing, name='property_listing'),
    path('add_unit/<int:property_id>/',views.add_unit),
    path('tenant_management/', views.tenant_management, name='tenant_management'),
    path('add_tenant/', views.add_tenant, name='add_tenant'),
    path('unit_detail/<int:id>/',views.unit_view,name='unit_detail'),
    path('thank/',views.thank,name="thank"),
    path('logout/', views.logout_view,),
    path('signup/',views.signup_view),
    path('lease/',views.lease_details,name="lease"),
    path('property_thanks/',views.perperty_thanks)

]
