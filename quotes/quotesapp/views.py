from typing import Any
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote
from .utils import SetUserToModelMixin
# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    
    paginator = Paginator(quotes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotesapp/index.html', {'page_obj': page_obj, 'quotes': quotes})


class QuotesHome(ListView):
    model = Quote
    template_name = 'quotesapp/index.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()


class AuthorDetail(DetailView):
    model = Author
    template_name = 'quotesapp/author_detail.html'
    pk_url_kwarg = 'author_id'


class AddTag(LoginRequiredMixin, SetUserToModelMixin, CreateView):
    form_class = TagForm
    template_name = 'quotesapp/tag.html'
    success_url = reverse_lazy('quotesapp:main')


class AddAuthor(LoginRequiredMixin, SetUserToModelMixin, CreateView):
    form_class = AuthorForm
    template_name = 'quotesapp/author.html'
    pk_url_kwarg = 'author_id'


class AddQuote(LoginRequiredMixin, SetUserToModelMixin, CreateView):
    form_class = QuoteForm
    template_name = 'quotesapp/quote.html'
    success_url = reverse_lazy('quotesapp:main')
