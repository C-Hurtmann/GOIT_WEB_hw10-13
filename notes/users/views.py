from django.shortcuts import render, redirect

from . import forms

# Create your views here.
def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='noteapp:main')
    
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'users/signup.html', context={'form': form})
    return render(request, 'users/signup.html', context={'form': forms.RegisterForm()})