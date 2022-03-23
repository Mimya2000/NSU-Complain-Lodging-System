from django.shortcuts import render
from .forms import CustomUserCreationForm


def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            return render(request, 'Authentication/signup.html')
    context = {'form': form}
    return render(request, 'Authentication/signup.html', context)
