from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def main(request):
    return render(request, 'noteapp/index.html')

def tag(request):
    if request.method == 'POST':
        form = forms.TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='moteapp:main')
        else:
            return render(request, 'noteapp/tag.html', {'form': form})
    
    return render(request, 'noteapp/tag.html', {'form': forms.TagForm()})
    