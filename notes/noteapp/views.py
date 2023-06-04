from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models
# Create your views here.

def main(request):
    notes = models.Note.objects.all() if request.user.is_authenticated else []
    return render(request, 'noteapp/index.html', {'notes': notes})

@login_required
def tag(request):
    if request.method == 'POST':
        form = forms.TagForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/tag.html', {'form': form})
    
    return render(request, 'noteapp/tag.html', {'form': forms.TagForm()})

@login_required
def note(request):
    tags = models.Tag.objects.filter(user=request.user).all()
    
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            choise_tags = models.Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choise_tags.iterator():
                new_note.tags.add(tag)
            
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/note.html', {'tags': tags, 'form': form})

    return render(request, 'noteapp/note.html', {"tags": tags, 'form': forms.NoteForm()})

def detail(request, note_id):
    note = get_object_or_404(models.Note, pk=note_id, user=request.user)
    return render(request, 'noteapp/detail.html', {'note': note})

def set_done(request, note_id):
    models.Note.filter(pk=note_id, user=request.user).update(done=True)
    return redirect(to='noteapp:main')

def delete_note(request, note_id):
    models.Note.objects.get(id=note_id, user=request.user).delete()
    return redirect(to='noteapp:main')

