from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from renattop.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def page_400(request, exception):
    return render(request, '400.html')


def page_403(request, exception):
    return render(request, '403.html')


def page_404(request, exception):
    context = {'exc': exception}
    return render(request, '404.html', context)


def page_500(request):
    return render(request, '500.html')
