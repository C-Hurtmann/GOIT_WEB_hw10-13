from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def main(request):
    return render(request, 'noteapp/index.html')

def tag(request):
    if request.method == 'POST':
        form = forms.TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/tag.html', {'form': form})
    
    return render(request, 'noteapp/tag.html', {'form': forms.TagForm()})

def note(request):
    tags = models.Tag.objects.all()
    
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()
            choise_tags = models.Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choise_tags.iterator():
                new_note.tags.add(tag)
            
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/note.html', {'tags': tags, 'form': form})
    return render(request, 'noteapp/note.html', {"tags": tags, 'form': forms.NoteForm()})


    