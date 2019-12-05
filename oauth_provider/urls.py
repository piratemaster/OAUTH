from django.urls import path, include
from .views import ApiEndpoint, ApiSecret


urlpatterns = [
    path(r'hello/', ApiEndpoint.as_view()),
    path(r'secret/', ApiSecret.as_view()),
]

