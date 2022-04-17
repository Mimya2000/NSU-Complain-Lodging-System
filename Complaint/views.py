from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import CreateComplaintForm, EditComplaintReviewerForm, EditComplaintNonReviewerForm, MakeCommentForm
from .models import Complaints, Comments, History


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
                    complaint.reviewer = get_user_model().objects.get(email='projectwork.testemail@gmail.com')
                user_reviewer = get_user_model().objects.get(email=complaint.reviewer)
                user_against = get_user_model().objects.get(email=complaint.against)
                if complaint.against_2 is None and complaint.against_3 is not None:
                    messages.error(request, 'Please select first two fields if complaining against two people!')
                else:
                    if complaint.against_2 is not None:
                        user_against2 = get_user_model().objects.get(email=complaint.against_2)
                        if user_against2 == user_against:
                            messages.error(request, 'You cannot select same person multiple times to complaint against!')
                            context = {'form': form}
                            return render(request, 'Complaint/add_complaint.html', context)
                    if complaint.against_3 is not None:
                        user_against3 = get_user_model().objects.get(email=complaint.against_3)
                        if user_against2 == user_against3 or user_against3 == user_against:
                            messages.error(request, 'You cannot select same person multiple times to complaint against!')
                            context = {'form': form}
                            return render(request, 'Complaint/add_complaint.html', context)
                    complaint.save()
                    subject = 'Complaint Created!'
                    if user_reviewer.email != 'projectwork.testemail@gmail.com':
                        body = 'Hello System Admin, ' + ', a complaint against ' + str(user_against.name) + ' has been submitted by ' + str(request.user.name) + '.'
                        send_mail(
                            subject,
                            body,
                            settings.EMAIL_HOST_USER,
                            ['projectwork.testemail@gmail.com'],
                            fail_silently=False,
                        )
                    names = str(user_against.name)
                    if complaint.against_2 is not None:
                        names += ', '
                        names += str(user_against2.name)
                    if complaint.against_3 is not None:
                        names += ', '
                        names += str(user_against3.name)
                    body = 'Hello ' + str(request.user.name) + ', your complaint against ' + names + ' has been submitted successfully.'
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


@login_required(login_url='login')
def complaintCard(request, pk):
    form = MakeCommentForm()
    complaint_obj = Complaints.objects.get(id=pk)
    if complaint_obj.reviewer == request.user or complaint_obj.user == request.user or request.user.email == 'projectwork.testemail@gmail.com':
        messages.error(request, 'You are not authorized to see this complaint!')
        return redirect('my-account')
    comments = Comments.objects.all().filter(complaint_id=pk)
    if request.method == 'POST':
        form = MakeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.complaint_id = pk
            comment.save()
            messages.success(request, 'Your comment has been posted successfully.')
        else:
            messages.error(request, 'Something went wrong with your comment!')
    context = {'complaint': complaint_obj, 'form': form, 'comments': comments}
    return render(request, 'Complaint/complaint_card.html', context)


@login_required(login_url='login')
def complaintStatus(request):
    complaints = Complaints.objects.all()
    if request.user.type == 'Student' or request.user.type == 'Staff':
        lodged = complaints.filter(user=request.user)
        lodged_open = lodged.exclude(status='Reviewed').exclude(status='Declined')
        lodged_close = lodged.exclude(status='In progress').exclude(status='Submitted')
        context = {'lodged_open': lodged_open, 'lodged_close': lodged_close}
        return render(request, 'Complaint/status.html', context)
    else:
        lodged = complaints.filter(user=request.user)
        lodged_open = lodged.exclude(status='Reviewed').exclude(status='Declined')
        lodged_close = lodged.exclude(status='In progress').exclude(status='Submitted')
        review = complaints.filter(reviewer=request.user)
        review_open = review.exclude(status='Reviewed').exclude(status='Declined')
        review_close = review.exclude(status='In progress').exclude(status='Submitted')
        context = {'lodged_open': lodged_open, 'lodged_close': lodged_close, 'review_open': review_open, 'review_close': review_close}
        return render(request, 'Complaint/status.html', context)


@login_required(login_url='login')
def editComplaint(request, pk):
    complaint = Complaints.objects.get(id=pk)
    reviewer = complaint.reviewer
    lodger = complaint.user
    if request.user == reviewer:
        form = EditComplaintReviewerForm(instance=complaint)
        if request.method == 'POST':
            form = EditComplaintReviewerForm(request.POST, instance=complaint)
            if form.is_valid():
                complaint = form.save(commit=False)
                if complaint.reviewer is None:
                    complaint.reviewer = reviewer
                complaint.save()
                messages.success(request, 'Your complaint review has been updated!')
                names = str(complaint.against.name)
                if complaint.against_2 is not None:
                    names += ', '
                    names += str(complaint.against_2.name)
                if complaint.against_3 is not None:
                    names += ', '
                    names += str(complaint.against_3.name)
                subject = 'Complaint Updated!'
                body = 'Hello ' + str(lodger.name) + ', your complaint against ' + names + ' has been updated by ' + reviewer.name + ' successfully.'
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [lodger.email],
                    fail_silently=False,
                )
                body = 'Hello ' + str(reviewer.name) + ', your update has been saved successfully.'
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [reviewer.email],
                    fail_silently=False,
                )
                if reviewer is not complaint.reviewer:
                    body = 'Hello ' + str(complaint.reviewer.name) + ', you have been assigned to review a complaint by ' + reviewer.name + '.'
                    send_mail(
                        subject,
                        body,
                        settings.EMAIL_HOST_USER,
                        [complaint.reviewer.email],
                        fail_silently=False,
                    )
                return redirect('my-account')
            else:
                messages.error(request, 'Something went wrong!')
    else:
        form = EditComplaintNonReviewerForm(instance=complaint)
        if request.method == 'POST':
            form = EditComplaintNonReviewerForm(request.POST, instance=complaint)
            if form.is_valid():
                complaint = form.save(commit=False)
                complaint.save()
                messages.success(request, 'Your complaint has been updated!')
                names = str(complaint.against.name)
                if complaint.against_2 is not None:
                    names += ', '
                    names += str(complaint.against_2.name)
                if complaint.against_3 is not None:
                    names += ', '
                    names += str(complaint.against_3.name)
                subject = 'Complaint Updated!'
                body = 'Hello ' + str(lodger.name) + ', your complaint against ' + names + ' has been updated successfully.'
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [lodger.email],
                    fail_silently=False,
                )
                body = 'Hello ' + str(reviewer.name) + ', one of the complaints you are reviewing has been updated.'
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [reviewer.email],
                    fail_silently=False,
                )
                return redirect('my-account')
            else:
                messages.error(request, 'Something went wrong!')
    context = {'form': form, 'complaint': complaint}
    return render(request, 'Complaint/edit_complaint.html', context)


@login_required(login_url='login')
def seeHistory(request, pk):
    complaint_obj = Complaints.objects.get(id=pk)
    if complaint_obj.reviewer == request.user or complaint_obj.user == request.user or request.user.email == 'projectwork.testemail@gmail.com':
        messages.error(request, 'You are not authorized to see this complaint!')
        return redirect('my-account')
    history = History.objects.all().filter(complaint_id=pk)
    context = {'history': history}
    return render(request, 'Complaint/history.html', context)
