from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def userAccount(request):
    user_object = request.user
    # if user_object.email == 'cls@gmail.com':
    #     return redirect('admin')
    context = {'user': user_object}
    return render(request, 'Profile/user_account.html', context)


def userProfile(request, pk):
    return render(request, 'Profile/user_profile.html')

