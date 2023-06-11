import os
import django
from pprint import pprint

import mongoDB.connection
from mongoDB import models as mongo

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
django.setup()

from quotesapp.models import Tag, Author, Quote


def main():
    # delete all rows from django database
    Tag.objects.all().delete()
    Author.objects.all().delete()
    Quote.objects.all().delete()
    
    mongo_authors = mongo.Authors.objects.all()

    for i in mongo_authors:
        row_dict = i.to_mongo().to_dict()
        del row_dict['_id']
        new_author = Author(**row_dict)
        new_author.save()
    
    mongo_quotes = mongo.Quotes.objects.all()
    
    for i in mongo_quotes:
        quote = i.quote
        tags = i.tags
        author_dbref = i.author
        author_name = mongo.Authors.objects.get(pk=author_dbref.id).fullname
        author = Author.objects.get(fullname=author_name)
        new_quote = Quote(quote=quote, author=author)
        new_quote.save()
        # add tags separately
        for tag in tags:
            try:
                tag = Tag.objects.get(name=tag)
            except Tag.DoesNotExist:
                tag = Tag(name=tag)
                tag.save()
            finally:
                new_quote.tags.add(tag)

def testing():
    from django.db.models import Count
    tags = Tag.objects.prefetch_related('quotes').all()
    tags = tags.annotate(quotes_count=Count('quotes'))
    tags = tags.order_by('-quotes_count')
    most_common_tags = tags[:10]
    for tag in most_common_tags:
        quotes = tag.quotes.all()
        quotes_qty = len([q for q in quotes])
        print(tag.name, quotes_qty)

if __name__ == '__main__':
    main()
    testing()
