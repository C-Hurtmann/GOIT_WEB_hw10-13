import os
import django

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


if __name__ == '__main__':
    main()

