from django.shortcuts import render


def userProfile(request, pk):
    return render(request, 'Profile/user_profile.html')

