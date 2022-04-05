from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import CreateComplaintForm
import Authentication.models as auth_model


@login_required(login_url='login')
def addComplaint(request):
    form = CreateComplaintForm(user=request.user)
    if request.method == 'POST':
        form = CreateComplaintForm(user=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            if str(complaint.against) == str(request.user.email):
                messages.error(request, 'You cannot complain against yourself!')
            elif str(complaint.reviewer) == str(request.user.email):
                messages.error(request, 'You cannot review your own complaint!')
            else:
                complaint.user = request.user
                complaint.status = 'Submitted'
                if complaint.reviewer is None:
                    complaint.reviewer = auth_model.Reviewer.objects.get(user=get_user_model().objects.get(email='projectwork.testemail@gmail.com'))
                user_reviewer = get_user_model().objects.get(email=complaint.reviewer)
                user_against = get_user_model().objects.get(email=complaint.against)
                complaint.save()
                subject = 'Complaint Created!'
                if user_reviewer.email != 'projectwork.testemail@fmail.com':
                    body = 'Hello System Admin, ' + ', a complaint against ' + str(user_against.name) + 'has been submitted by ' + str(request.user.name) + '.'
                    send_mail(
                        subject,
                        body,
                        settings.EMAIL_HOST_USER,
                        ['projectwork.testemail@gmail.com'],
                        fail_silently=False,
                    )
                body = 'Hello ' + str(request.user.name) + ', your complaint against ' + str(user_against.name) + 'has been submitted successfully.'
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [request.user.email],
                    fail_silently=False,
                )
                body = 'Hello ' + str(user_reviewer.name) + ', a complaint has been lodged for you to review.'
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [user_reviewer.email],
                    fail_silently=False,
                )
                messages.success(request, 'Your Complaint was submitted Successfully!')
                return redirect('my-account')
        else:
            messages.error(request, 'Something went wrong! Try again!')
    context = {'form': form}
    return render(request, 'Complaint/add_complaint.html', context)
