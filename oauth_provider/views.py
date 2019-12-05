from django.shortcuts import render

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator


class ApiEndpoint(ProtectedResourceView):

    def get(self, request, *args, **kwargs):
        return HttpResponse()


class ApiSecret(LoginRequiredMixin, ProtectedResourceView):
    login_url = '/auth'

    @staticmethod
    def get(request, *args, **kwargs):
        return HttpResponse("Secret contents!")

