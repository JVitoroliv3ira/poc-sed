from django.urls import path
from .views import TokenCreateView

urlpatterns = [
    path('', TokenCreateView.as_view(), name='create-token'),
]
