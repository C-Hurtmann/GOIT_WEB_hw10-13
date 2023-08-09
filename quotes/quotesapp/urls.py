from django.urls import path
from .views import AddTag, AddAuthor, AddQuote, AuthorDetail, QuotesHome

app_name = 'quotesapp'

urlpatterns = [
    path('', QuotesHome.as_view(), name='main'),
    path('tag/', AddTag.as_view(), name='tag'),
    path('author/', AddAuthor.as_view(), name='author'),
    path('quote/', AddQuote.as_view(), name='quote'),
    path('author/<int:author_id>', AuthorDetail.as_view(), name='author_detail'),
    ]