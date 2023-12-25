from django.shortcuts import render

# Create your views here.
from .forms import ProfileForm
from .models import Profile

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def my_profile_view(request):

    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('navbar')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
    }


    return render(request, 'profiles/main.html', context)