from django.shortcuts import render


def userProfile(request):
    return render(request, 'Profile/user_profile.html')

