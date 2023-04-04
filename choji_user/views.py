from django.http import HttpResponse
from django.shortcuts import render
from .forms import AccountCreationForm
from .models import Account, Chat, Group_account, Group_chat, Trade


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def login(request, *args, **kwargs):
    return render(request, 'login.html')


def register(request):
    form = AccountCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AccountCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def user_profile(request):
    return render(request, 'profile.html')

