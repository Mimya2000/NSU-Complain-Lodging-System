from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser



def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        email_id = str(form['email'])
        email_id = email_id.split('@', 1)[-1]
        if form['type'] == 'Staff' and email_id != 'gmail.com':
            messages.error(request, 'Enter a valid email address')
        elif form['type'] != 'Staff' and email_id != 'northsouth.edu':
            messages.error(request, 'Enter your NSU email address')
        elif form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            email_subject = 'NSU-CLS account activation'
            email_body = ''
            messages.success(request, 'Account was created!')
            login(request, user)
        else:
            messages.error(request, 'An error has occurred during registration.')
    context = {'form': form}
    return render(request, 'Authentication/signup.html', context)


def userLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, 'Email does not exist!')
            return render(request, 'Authentication/login.html')
        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, "Email or Password is incorrect!")
        else:
            login(request, user)
            return redirect('my-account')
    return render(request, 'Authentication/login.html')


@login_required(login_url='login')
def userLogout(request):
    logout(request)
    messages.info(request, 'You were logged out!')
    return redirect('login')
