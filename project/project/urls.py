from django.urls import path
from django.urls import include,path
from . import views

from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index, name="index"),
    
    
    path('contact',views.contact, name="contact"),
    path('mt',views.mtcontact,name ="mtcontact"),

    path('adminpanel',views.adminpanel,name="adminpanel"),

    path('contact2',views.contact2, name="contact2"),

    path('bizgurukul',views.index2, name="index2"),
    path('biz',views.bizcontact,name ="bizcontact"),
    
         

    

    
    
    ]

