from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.form import RegisterForm,LoginForm
from django.contrib import messages
# Create your views here.

def login_views(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'account/login.html')
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if '@' in username:
                kwargs = {'email': username.lower()}
            else:
                kwargs = {'username': username}
            try:
                username = User.objects.get(**kwargs).username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'warning that invalid Username/Eimail and pssword')
                return render(request, 'account/login.html')    
    messages.add_message(request, messages.ERROR, 'warning that might need attention.')
    return render(request, 'account/login.html',{'form': form})

@login_required(login_url='/account/login')
def logout_views(request):
    logout(request)
    return redirect('/')


def register_views(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                email = email.lower()
                kwargs = {'email': email}
                try:
                    username = User.objects.get(**kwargs).username
                    messages.add_message(request, messages.ERROR, 'warning that invalid Eimail because used')
                except User.DoesNotExist:
                    form.save()
                    return redirect('/account/login')
        form = RegisterForm()
        return render(request, 'account/register.html',{'form': form})
    else:
        return redirect('/')
