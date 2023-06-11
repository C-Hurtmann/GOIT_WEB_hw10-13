from django import template
from django.db.models import Count

from quotesapp.models import Tag, Quote


register = template.Library()

@register.simple_tag()
def get_top_tags():
    tags = Tag.objects.prefetch_related('quotes').all()
    tags = tags.annotate(quotes_count=Count('quotes'))
    tags = tags.order_by('-quotes_count')
    most_common_tags = tags[:10]
    return most_common_tags