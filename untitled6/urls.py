"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#import oauth2_provider as oap
from oauth_provider import urls as OA_urls
from oauth_api import urls as OApi_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path(r'api/', include(OA_urls)),
    path(r'', include(OApi_urls)),
    path(r'api/doc/', schema_view)
]
