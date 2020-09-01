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


# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#     success_url = "/accounts/login/"
#     template_name = "registration/register.html"

#     def form_valid(self, form):
#         form.save()
#         return super(RegisterFormView, self).form_valid(form)
