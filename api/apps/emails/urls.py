from django.urls import path

from apps.emails.views import SendEmailView

urlpatterns = [
    path('', SendEmailView.as_view(), name='send-email'),
]
