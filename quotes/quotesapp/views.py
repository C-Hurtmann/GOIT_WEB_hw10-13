from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote
from .utils import SetUserToModelMixin
# Create your views here.


class QuotesHome(ListView):
    model = Quote
    template_name = 'quotesapp/index.html'
    paginate_by = 5
    
    def get_queryset(self) -> QuerySet[Any]:
        quotes = Quote.objects.all()
        q = self.request.GET.get('q')
        if q:
            quotes = quotes.filter(
                  Q(quote__icontains=q)
                | Q(author__fullname__icontains=q)
                | Q(tags__name__icontains=q)
                )

        return quotes
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        context['q'] = q
        return context


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


def page_not_found_handler(request, exception):
    return render(request, '404.html', status=404)