from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.http import is_safe_url


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)

        redirect_to = request.GET.get('next')
        if redirect_to and is_safe_url(url=redirect_to, host=request.get_host()):
            return HttpResponseRedirect(redirect_to)
        else:
            return HttpResponseRedirect(reverse('dashboard:index'))

    raise PermissionDenied


def logout(request):
    auth_logout(request)

    return HttpResponseRedirect(reverse('logout:index'))
