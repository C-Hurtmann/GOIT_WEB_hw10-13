from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('quote_detail/<int:quote_id>', views.quote_detail, name='quote_detail'),
    path('author_detail/<int:author_id>', views.author_detail, name='author_detail')
    ]