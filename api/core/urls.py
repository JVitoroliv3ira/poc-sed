from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/tokens/', include('apps.tokens.urls')),
    path('api/v1/emails/', include('apps.emails.urls')),
]
