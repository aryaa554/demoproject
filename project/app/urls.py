from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('app.urls')),
    path('',include('contact.urls')),
    path('',include('bizcontact.urls')),
    path('',include('biz.urls'))
    
]

