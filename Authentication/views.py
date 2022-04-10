from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import CustomUserCreationForm
from .models import CustomUser, Faculty, Staff, Student, Administrator
from .token import account_activation_token


def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            email_id = user.email
            email_id = email_id.split('@', 1)[-1]
            if user.type == 'Staff' and email_id != 'gmail.com':
                messages.error(request, 'Enter a valid email address')
            elif user.type != 'Staff' and email_id != 'northsouth.edu':
                messages.error(request, 'Enter your NSU email address')
            else:
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_subject = 'NSU-CLS account activation'
                message = render_to_string('Authentication/account_activation.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.nsu_id)),
                    'token': account_activation_token.make_token(user),
                })
                email = EmailMessage(
                    email_subject, message, to=[user.email]
                )
                email.send()
                context = {'user': user}
                return render(request, 'Authentication/confirm_email.html', context)

            # messages.success(request, 'Account was created!')
            # login(request, user)
        else:
            messages.error(request, 'An error has occurred during registration.')
    context = {'form': form}
    return render(request, 'Authentication/signup.html', context)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(nsu_id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        if user.type == 'Faculty':
            profile = Faculty.objects.create(
                user=user,
            )
        elif user.type == 'Student':
            profile = Student.objects.create(
                user=user,
            )
        elif user.type == 'Administrator':
            profile = Administrator.objects.create(
                user=user,
            )
        else:
            profile = Staff.objects.create(
                user=user,
            )
        messages.success(request, 'Your account is successfully activated')
        login(request, user)
        return redirect('my-account')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        messages.error(request, 'Please activate your account by clicking on the link sent to your email')
        context = {'user': user}
        return render(request, 'Authentication/confirm_email.html', context)


def resend_link(request, pk):
    User = get_user_model()
    user = User.objects.get(nsu_id=pk)
    current_site = get_current_site(request)
    email_subject = 'NSU-CLS account activation'
    message = render_to_string('Authentication/account_activation.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.nsu_id)),
        'token': account_activation_token.make_token(user),
    })
    email = EmailMessage(
        email_subject, message, to=[user.email]
    )
    email.send()
    context = {'user': user}
    return render(request, 'Authentication/confirm_email.html', context)


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
