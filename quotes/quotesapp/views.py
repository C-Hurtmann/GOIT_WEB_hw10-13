from django.shortcuts import render, redirect
from .forms import TagForm

# Create your views here.
def main(request):
    return render(request, 'quotesapp/index.html')

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main') #  if form filled correctly
        else:
            return render(request, 'quotesapp/tag.html', {'form': form}) #  if form filled with mistakes
    return render(request, 'quotesapp/tag.html', {'form': TagForm()}) #  first enter to page
