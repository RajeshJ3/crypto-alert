from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    path('api/alerts/', include('alerts.urls')),
]
