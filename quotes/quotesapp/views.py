from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote

# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    
    paginator = Paginator(quotes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotesapp/index.html', {'page_obj': page_obj, 'quotes': quotes})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main') #  if form filled correctly
        else:
            return render(request, 'quotesapp/tag.html', {'form': form}) #  if form filled with mistakes
    return render(request, 'quotesapp/tag.html', {'form': TagForm()}) #  first enter to page

@login_required
def author(request):
    if request.method =='POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/author.html', {'form': form})
    return render(request, 'quotesapp/author.html', {'form': AuthorForm()})

@login_required
def quote(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

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
