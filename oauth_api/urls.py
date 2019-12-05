from django.urls import path, include
from oauth_api.models import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]