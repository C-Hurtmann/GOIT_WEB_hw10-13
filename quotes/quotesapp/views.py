from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote

# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    authors = Author.objects.all()
    return render(request, 'quotesapp/index.html', {'quotes': quotes, 'authors': authors})

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main') #  if form filled correctly
        else:
            return render(request, 'quotesapp/tag.html', {'form': form}) #  if form filled with mistakes
    return render(request, 'quotesapp/tag.html', {'form': TagForm()}) #  first enter to page

def author(request):
    if request.method =='POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/author.html', {'form': form})
    return render(request, 'quotesapp/author.html', {'form': AuthorForm()})

def quote(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
           # choise_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
           # for tag in choise_tags.iterator():
           #     new_quote.tags.add(tag)
            
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/quote.html', {'tags': tags, 'form': form})
    return render(request, 'quotesapp/quote.html', {'tags': tags, 'form': QuoteForm()})


def quote_detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotesapp/quote_detail.html', {'quote': quote})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotesapp/author_detail.html', {'author': author})
