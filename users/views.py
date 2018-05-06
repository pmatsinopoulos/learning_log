from django.shortcuts import render
import django.contrib.auth.views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required
def logout(request):
    django.contrib.auth.views.logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('learning_logs:index'))

    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # we need to register user
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()

            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
