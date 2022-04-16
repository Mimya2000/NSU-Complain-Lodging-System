from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, FacultyForm, AdminEmployeeForm, HelpingStaffForm
from django.contrib.auth import get_user_model


@login_required(login_url='login')
def userAccount(request):
    user_object = request.user
    # print(user_object.type)
    if user_object.type == 'Student':
        profile = user_object.student
    elif user_object.type == 'Faculty':
        profile = user_object.faculty
    elif user_object.type == 'Staff':
        profile = user_object.staff
    else:
        profile = user_object.administrator
    context = {'user': user_object, 'profile': profile}
    return render(request, 'Profile/user_account.html', context)


@login_required(login_url='login')
def updateProfile(request):
    if request.user.type == 'Student':
        student = request.user.student
        form = StudentForm(instance=student)
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your information has been updated!')
                return redirect('my-account')
    elif request.user.type == 'Faculty':
        faculty = request.user.faculty
        form = FacultyForm(instance=faculty)
        if request.method == 'POST':
            form = FacultyForm(request.POST, request.FILES, instance=faculty)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your information has been updated!')
                return redirect('my-account')
    elif request.user.type == 'Administrator':
        admin_employee = request.user.adminemployee
        form = AdminEmployeeForm(instance=admin_employee)
        if request.method == 'POST':
            form = AdminEmployeeForm(request.POST, request.FILES, instance=admin_employee)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your information has been updated!')
                return redirect('my-account')
    else:
        staff = request.user.helpingstaff
        form = HelpingStaffForm(instance=staff)
        if request.method == 'POST':
            form = HelpingStaffForm(request.POST, request.FILES, instance=staff)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your information has been updated!')
                return redirect('my-account')
    context = {'form': form}
    return render(request, 'Profile/update_profile.html', context)


def userProfile(request, pk):
    user_object = get_user_model().objects.get(email=pk)
    if request.user == user_object:
        return redirect('my-account')
    if user_object.type == 'Student':
        profile = user_object.student
    elif user_object.type == 'Faculty':
        profile = user_object.faculty
    elif user_object.type == 'Staff':
        profile = user_object.staff
    elif user_object.type == 'Administrator':
        profile = user_object.administrator
    else:
        context = {'user': user_object}
        return render(request, 'Profile/user_profile.html', context)
    context = {'user': user_object, 'profile': profile}
    return render(request, 'Profile/user_profile.html', context)

